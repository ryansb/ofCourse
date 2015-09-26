from __future__ import print_function
import os
from itertools import chain

from flask import Blueprint

from ofcourse.render import render_template
from ofcourse.util import app_path


homework = Blueprint('homework', __name__,
                     template_folder=app_path('templates'))
lectures = Blueprint('lectures', __name__,
                     template_folder=app_path('templates'))
quizzes = Blueprint('quizzes', __name__,
                    template_folder=app_path('templates'))


@homework.route('/', defaults={'page': 'index'})
@homework.route('/<page>')
def display_homework(page):
    if page == 'index':
        # Old way of generating list (for backwards compatibility)
        hws = os.listdir(app_path('static', 'hw'))
        hws.extend(os.listdir(app_path('templates', 'hw')))
        hws = [hw for hw in sorted(hws) if not hw == "index.mak"]
        # New, cleaner-in-the-template way to do it
        hwd = [(hw, os.path.join('/static', 'hw'))
               for hw in os.listdir(app_path('static', 'hw'))]
        hwd.extend([(os.path.splitext(hw)[0], '/hw')
                    for hw in os.listdir(app_path('templates', 'hw'))])
        hwd = {os.path.basename(hw): os.path.join(loc, hw)
               for hw, loc in hwd
               if os.path.splitext(os.path.basename(hw))[0] != "index"}
    else:
        hws = None
        hwd = None

    return render_template(os.path.join("hw", page),
                           hws=hws, os=os, assignments=hwd)


@lectures.route('/', defaults={'page': 'index'})
@lectures.route('/<page>')
def display_lecture(page):
    if page == 'index':
        lecture_list = os.listdir(app_path('templates', 'lectures'))
        # Old way of generating list (for backwards compatibility)
        lectures = [note for note in sorted(lecture_list)
                    if note != "index.mak"]
        # New, cleaner-in-the-template way to do it
        lecture_notes = [
                (note, os.path.splitext(os.path.join("/lectures", note))[0])
                for note in sorted(lecture_list)
                if os.path.splitext(note)[0] != "index"]
    else:
        lecture_notes = None
        lectures = None

    return render_template(os.path.join('lectures', page),
                           lecture_notes=lecture_notes, lectures=lectures)


@quizzes.route('/<quiz_num>')
def show_quiz(quiz_num):
    return render_template(os.path.join('quiz', quiz_num))
