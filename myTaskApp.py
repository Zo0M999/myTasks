from flask import Flask, render_template, request, redirect, url_for
from mytasks import MyTasks
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
db = MyTasks()


@app.route('/')
@app.route('/tasks')
def tasks():
    try:
        all_tasks = db.show_tasks()
    except:
        all_tasks = ('Smth went wrong.\nTry restarting app.\nSorry for temporary inconvenience :(',)

    return render_template('tasks.html', title='Tasks', info=f'{tasks.__name__}', tasks=all_tasks)


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        resp = dict(request.form)
        if len(resp['task_desc']) < 2:
            db.add_task(resp['task_name'], 'No description')
        else:
            db.add_task(resp['task_name'], resp['task_desc'])
        return redirect(url_for('tasks'))

    return render_template('add_task.html', title='AddTask', info=f'{add_task.__name__}')


@app.route('/comp_task', methods=['GET', 'POST'])
def comp_task():
    if request.method == 'POST':
        resp = dict(request.form)
        if len(resp['task_name'].split(',')) > 1:
            for r in [x.strip() for x in resp['task_name'].split(',')]:
                db.completed_task(r)
        else:
            db.completed_task(resp['task_name'])

        return redirect(url_for('tasks'))

    return render_template('comp_task.html', title='CompletedTasks', info=f'{comp_task.__name__}')


@app.route('/del_comp_task', methods=['GET', 'POST'])
def del_comp_task():
    if request.method == 'POST':
        db.del_task()
        return redirect(url_for('tasks'))

    return render_template('del_task.html', title='DeleteCompTasks', info=f'{del_comp_task.__name__}')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error404.html', title=f"{pageNotFound.__name__}")

