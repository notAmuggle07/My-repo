from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize Flask app
app = Flask(__name__)
# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
# Initialize Marshmallow for serialization/deserialization
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    deadline = db.Column(db.Date)
    reminder_time = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    priority = db.Column(db.String(20))

    def __init__(self, name, description, deadline, reminder_time, status, priority):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.reminder_time = reminder_time
        self.status = status
        self.priority = priority

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'deadline', 'reminder_time', 'status', 'priority')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/add-task', methods=['POST'])
def add_task():
    name = request.json['name']
    description = request.json['description']
    deadline = request.json['deadline']
    reminder_time = request.json['reminder_time']
    status = request.json['status']
    priority = request.json['priority']

    new_task = Task(name, description, deadline, reminder_time, status, priority)

    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)

# Get a specific task by ID
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

# Update a task
@app.route('/update-task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    task.name = request.json['name']
    task.status = request.json['status']

    db.session.commit()
    return task_schema.jsonify(task)

# Delete a task
@app.route('/delete-task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task with ID ' + id + ' has been deleted.'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
