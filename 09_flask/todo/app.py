from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def load_todos():
    try:
        with open("todos.txt", "r") as file:
            todos = [line.strip() for line in file]
    except FileNotFoundError:
        todos = []
    return todos

def save_todos(todos):
    with open("todos.txt", "w") as file:
        file.write("\n".join(todos))

@app.route("/", methods=["GET", "POST"])
def index():
    todos = load_todos()
    if request.method == "POST":
        new_todo = request.form.get("todo")
        if new_todo:
            todos.append(new_todo)
            save_todos(todos)
        return redirect(url_for("index"))
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>", methods=["GET"])
def delete(todo_id):
    if request.method == 'GET':
        todos = load_todos()
        if 0 <= todo_id < len(todos):
            del todos[todo_id]
            save_todos(todos)
        return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug=True)