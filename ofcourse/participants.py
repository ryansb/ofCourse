import os

from datetime import datetime, date, timedelta
from six.moves.urllib.parse import urlparse
import yaml

from flask import Blueprint, redirect

import ofcourse
from .util import app_path, get_hw_keys
from .render import render_template

participants_bp = Blueprint('participants_bp',
                            __name__,
                            template_folder=app_path('templates'))


currentYear = str(date.today().year)
currentTerm = "fall" if date.today().month > 7 else "spring"


@participants_bp.route('/')
def participants_blank():
    """
    This is the default landing
    for the participants listing page.
    It will list all of the participants
    in the current term for HFOSS
    """
    return participants_year_term(currentYear, currentTerm)


@participants_bp.route('/<year_or_nick>')
def participants_year(year_or_nick):
    """
    This will get all the participants
    within a given year
    """
    p_url = find_participant(year_or_nick)
    if p_url is not None:
        # render individual page
        return redirect(p_url)
    # otherwise render as a year
    return participants(year_or_nick + '/')


@participants_bp.route('/<year>/<term>')
def participants_year_term(year, term):
    """
    This will get all the participants
    within a given year and term
    """
    return participants(year + '/' + term + '/')


@participants_bp.route('/all')
def participants_all():
    return participants('')
"""
This will get all the participants
who have taken HFOSS
"""


def participants(root_dir):
    """
    Render the participants page,
    which shows a directory of all
    the students with their forge
    links, blog posts, assignment
    links, and etc.

    """

    yaml_dir = app_path('people', root_dir)

    student_data = []
    for dirpath, dirnames, files in os.walk(yaml_dir):
        dirpath = dirpath.rstrip("/")
        for fname in sorted(files):
            if fname.endswith('.yaml'):
                with open(dirpath + '/' + fname) as students:
                    contents = yaml.safe_load(students)
                    contents['yaml'] = dirpath + '/' + fname
                    year_term_data = dirpath.split('/')
                    contents['participant_page'] = "{y}/{t}/{u}".format(
                        y=year_term_data[-2],
                        t=year_term_data[-1],
                        u=os.path.splitext(fname)[0]
                    )

                    for forge in contents['forges']:
                        url = urlparse(forge)
                        if "github.com" in url.netloc:
                            contents['github'] = url.path[1:]

                    contents['isActive'] = (currentYear in year_term_data and
                                            currentTerm in year_term_data)

                    student_data.append(contents)

    assignments = get_hw_keys()
    elapsed = (datetime.today() - ofcourse.site.COURSE_START).total_seconds()
    target_number = int(elapsed / timedelta(weeks=1).total_seconds() + 1 +
                        len(assignments))

    return render_template(
        'blogs',
        student_data=student_data,
        gravatar=ofcourse.site.gravatar,
        target_number=target_number,
        hw_keys=assignments
    )


def find_participant(nick):
    yaml_dir = app_path('people')

    for dirpath, dirnames, files in os.walk(yaml_dir):
        for fname in files:
            if (fname.lower().startswith(nick.lower()) and
                    fname.endswith('.yaml')):
                participant = os.path.join(
                    dirpath,
                    fname
                ).replace(yaml_dir, '')
                participant = participant.replace('.yaml', '')
                return 'participants' + participant
