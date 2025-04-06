from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
tasks = []
achievement_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global achievement_count
    if request.method == 'POST':
        task = request.form['task']
        due = request.form['due']
        if task:
            tasks.append({'task': task, 'due': due, 'done': False})
    return render_template('index.html', tasks=tasks, achievements=achievement_count)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    global achievement_count
    tasks[task_id]['done'] = True
    achievement_count += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
