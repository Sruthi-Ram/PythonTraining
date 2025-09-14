from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# -------------------------------
# Database Models
# -------------------------------
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="pending")  # pending, in-progress, done
    priority = db.Column(db.String(10), default="medium")  # low, medium, high

# -------------------------------
# API Routes
# -------------------------------

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        status=data.get("status", "pending"),
        priority=data.get("priority", "medium")
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task added", "id": task.id})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "priority": t.priority
        } for t in tasks
    ])

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.priority = data.get("priority", task.priority)
    db.session.commit()
    return jsonify({"message": "Task updated"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
