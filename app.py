from flask import Flask,redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    important = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        important = 'important' in request.form
        todo = Todo(title=title, description=description , important=important)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)


@app.route("/task")
def show_task():
    allTodo = Todo.query.all()
    print(allTodo)
    return "this is your tasks page"

@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    if request.method=='POST':
        title = request.form["title"]
        description = request.form["description"]
        important = 'important' in request.form
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.description=description
        todo.important=important
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)



@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False, port=8000)