from flask import render_template
from flask_login import current_user

from pyedu.main import main
from pyedu.models import Lecture
from pyedu.util import sysinfo


@main.route('/')
def index():
    lectures = Lecture.query.all()
    continue_task = current_user.get_next_task()
    return render_template('index.html', sysinfo=sysinfo(), lectures=lectures, continue_task=continue_task)
