"""
The Report classes create current state informatiion about the progress in the Lectures, Lessons or Overall for
a single User or all Users.
"""
from pyedu.models import User, Lecture


class UserReport:
    """

    """
    def __init__(self, user_id):
        self.user = User.query.get_or_404(user_id)

    def lesson_progress(self, lesson):
        return lesson.progress(student=self.user) / lesson.task_count

    def lecture_progress(self, lecture):
        return sum([lesson.progress(student=self.user) for lesson in lecture.lessons])

    @property
    def progress(self):
        return sum([self.lecture_progress(lecture) for lecture in Lecture.query.all() if lecture.is_enrolled(self.user)])


    def lesson_total_tasks(self, lesson):
        return lesson.task_count

    def lecutre_total_tasks(self, lecture):
        return sum([lesson.task_count for lesson in lecture.lessons])

    @property
    def total_tasks(self):
        return sum([self.lecutre_total_tasks(lecture) for lecture in Lecture.query.all() if lecture.is_enrolled(self.user)])