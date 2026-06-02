from flask import Blueprint, render_template, redirect, request, url_for

from database.engine import db
from database.models.todo import Task


task_bp = Blueprint('tasks', __name__, template_folder='templates')


@task_bp.route('/')
def get_all_tasks():
    return render_template('tasks.html', tasks_db= tasks_db)


@task_bp.route('/task/<int:id>')
def detail_task(id):
    task = Task.query.filter_by(id=id).first()
    return render_template('detail.html', task_one=task)


@task_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()

@task_bp.route('/update/<int:id>', methods=['GET','POST'])
def update_task(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title:
            task.title = title
        if description:
            task.description = description
        db.session.commit()

    return render_template('update.html', task_one=task)


@task_bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))
