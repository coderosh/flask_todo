from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

from todo.models import Todo
from todo.extensions import db

from todo.forms import TodoForm

todos = Blueprint('todos', __name__)


@todos.route('/')
@login_required
def index():
    all_todos = Todo.query.all()
    return render_template('todos/index.html', todos=all_todos)


@todos.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = TodoForm()

    if form.validate_on_submit():
        todo = Todo(task=form.task.data,
                    completed=form.completed.data, creator=current_user)

        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')

    return render_template('todos/new.html', form=form)


@todos.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)

    form = TodoForm(obj=todo)

    if form.validate_on_submit():
        todo.task = form.task.data
        todo.completed = form.completed.data
        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')

    return render_template('todos/edit.html', form=form)


@todos.route('/completed')
@login_required
def completed():
    return "All Completed todos"


@todos.route('/remaining')
@login_required
def remaining():
    return "All remaining todos"
