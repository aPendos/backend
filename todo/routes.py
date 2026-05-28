from flask import Blueprint, render_template, redirect, request

task_bp = Blueprint('tasks', __name__, template_folder='templates')

tasks_db = [
    {'id': 1, 'title': 'Купить хлеб', 'description': 'Успеть до закрытия'},
    {'id': 2, 'title': 'Купить масло', 'description': 'Успеть до закрытия'},
    {'id': 3, 'title': 'Выполнить дз', 'description': 'До след. урока'},
    {'id': 4, 'title': 'Реализовать CRUD', 'description': 'Дедлайн до завтра'}
]


@task_bp.route('/')
def get_all_tasks():
    return render_template('tasks.html', tasks_db= tasks_db)


@task_bp.route('/task/<int:id>')
def detail_task(id):
    task_one = []
    for task in tasks_db:
        if task.get('id') == id:
            task_one.append(task)
    return render_template('detail.html', task_one=task_one)


@task_bp.route('/update/<int:id>', methods=['GET','POST'])
def update_task(id):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')


    task_one = []
    for task in tasks_db:
        if task.get('id') == id:
            task_one.append(task)
    return render_template('update.html', task_on=task_one)


@task_bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    for task in tasks_db:
        if task.get('id') == id:
            tasks_db.remove(task)
            break
    return redirect(url_for('tasks.get_all_tasks'))
