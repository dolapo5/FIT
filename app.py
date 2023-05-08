from flask import Flask, render_template, request, redirect, flash, url_for
import os.path
import json
app = Flask(__name__)
app.secret_key = 'qweqweqwe'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save', methods=['GET', 'POST'])
def save():
    task = {}
    if request.method == 'POST':
        if os.path.exists('tasks.json'):
            with open('tasks.json') as file:
                task = json.load(file)

        if request.form['task'] in task.keys():
            flash('This task already exist please use another or delete task')
            return redirect(url_for('home'))

        task[request.form['task']] = request.form['taskd']
        with open('tasks.json', 'w') as file:
            json.dump(task, file)
        flash("Task as been added succesfully")
        return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))


@app.route('/view', methods=['GET'])
def view():
    task = {}
    if os.path.exists('tasks.json'):
        with open('tasks.json') as file:
            task = json.load(file)
        return render_template('view.html', name=task)


@app.route('/delete/<key>/')
def delete(key):
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            data = json.load(file)
    if key in data:
        del data[key]
    else:
        flash('There is an error I can not delete this task')
        return redirect(url_for('view'))

    with open('tasks.json', 'w') as file:
        json.dump(data, file)

    flash('Task has been deleted succesfully')
    return redirect(url_for('view'))


def main():
    app.run(host="0.0.0.0" , port=3000)


if __name__ == '__main__':
    main()
