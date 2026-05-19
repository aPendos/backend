from flask import Blueprint

task_bp = Blueprint('tasks', __name__, template_folder='templates')


@task_bp.route('/all_tasks')
def get_all_tasks():
    return 'Все задачи!'