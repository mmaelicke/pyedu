"""
This file collects the different lecture views including list, enroll or unroll.

"""
from flask import render_template
from pyedu.student import stud
from pyedu.models import Lecture


@stud.route('/lectures/view')
def lecture_view_all():
    lectures = Lecture.query.all()
    return render_template('student/lectures.html', lectures=lectures)

@stud.route('/lecture/view/<int:lecture_id>')
def lecture_view(lecture_id):
    # load the lecture or abort
    lecture = Lecture.query.get_or_404(lecture_id)
    return render_template('student/view_lecture.html', lecture=lecture, lessons=lecture.lessons)