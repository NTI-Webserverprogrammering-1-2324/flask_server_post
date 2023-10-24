from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


# ==================== Routes ====================


@app.route("/")
def index():
    return render_template("index.html")


# Server Rendered Routes using only Flask and Jinja Templates


@app.route("/todo_static", methods=["GET"])
def todo_page_static():
    return render_template("todo_static.html", tasks=tasks)

## Create
@app.route("/add_task_static", methods=["POST"])
def add_task_static():
    title = request.form.get("title")
    content = request.form.get("content")
    tasks.append({"title": title, "content": content, "editing": False})
    return redirect(url_for("todo_page_static"))

## Update
@app.route("/edit_task_static/<int:task_id>", methods=["POST"])
def edit_task_static(task_id):
    title = request.form.get("title")
    content = request.form.get("content")
    if "editing" in tasks[task_id] and tasks[task_id]["editing"]:
        tasks[task_id] = {"title": title, "content": content, "editing": False}
    else:
        for task in tasks:
            task["editing"] = False
        tasks[task_id]["editing"] = True
    return redirect(url_for("todo_page_static"))

## Delete
@app.route("/delete_task_static/<int:task_id>", methods=["POST"])
def delete_task_static(task_id):
    tasks.pop(task_id)
    return redirect(url_for("todo_page_static"))


# Hybrid Rendered Routes using htmx, flask and Jinja Templates


@app.route("/todo_dynamic", methods=["GET"])
def todo_page_dynamic():
    return render_template("todo_dynamic.html")


@app.route("/add_task_dynamic", methods=["POST"])
def add_task_dynamic():
    title = request.form.get("title")
    content = request.form.get("content")

    task = {"title": title, "content": content}
    tasks.append(task)

    # Return the new task as a card to be added to the UI
    return render_template("task_card.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
