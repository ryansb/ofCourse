import os

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
        hws = os.listdir(app_path('static', 'hw'))
        hws.extend(os.listdir(app_path('templates', 'hw')))
        hws = [hw for hw in sorted(hws)
               if os.path.splitext(hw)[0] == "index"]
    else:
        hws = None

    return render_template(os.path.join('hw', page), hws=hws)


@lectures.route('/', defaults={'page': 'index'})
@lectures.route('/<page>')
def display_lecture(page):
    if page == 'index':
        lecture_notes = os.listdir(app_path('templates', 'lectures'))
        lecture_notes = [note for note in sorted(lecture_notes)
                         if os.path.splitext(note)[0] != "index"]
    else:
        lecture_notes = None

    return render_template(os.path.join('lectures', page),
                           lectures=lecture_notes)


@quizzes.route('/<quiz_num>')
def show_quiz(quiz_num):
    return render_template(os.path.join('quiz', quiz_num))
