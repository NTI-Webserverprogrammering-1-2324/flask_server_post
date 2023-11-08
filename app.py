from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application.
app = Flask(__name__)

# A global list to store tasks.
tasks = []

# Define the routes for the application.


@app.route("/")
def home():
    """
    Serve the index page.

    Returns:
        Rendered 'index.html' template.
    """
    return render_template("index.html")


@app.route("/todo", methods=["GET"])
def todo():
    """
    Serve the todo list page.

    Retrieve all tasks and pass them to the 'todo.html' template for display.

    Returns:
        Rendered 'todo.html' template with all tasks.
    """
    return render_template("todo.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    """
    Add a new task to the list.

    Retrieve task details from the form data and append it to the tasks list.

    Returns:
        Redirect to the 'todo' route.
    """
    title = request.form.get("title")
    content = request.form.get("content")
    tasks.append({"title": title, "content": content, "editing": False})
    return redirect(url_for("todo"))


@app.route("/search_task/", methods=["POST"])
def search_task():
    """Searches for a task by ID and redirects to its view page.

    Returns:
        A redirect to the view_task function with the task_id parameter.
    """
    task_id = request.form.get("task_id", type=int)
    return redirect(url_for("view_task", task_id=task_id))


@app.route("/view_task/<int:task_id>", methods=["GET"])
def view_task(task_id):
    """
    Display a single task by its ID.

    Parameters:
        task_id (int): The ID of the task to display.

    Returns:
        Rendered 'todo.html' template with the specified task if found, otherwise, an indication that the task was not found.
    """
    if 0 <= task_id < len(tasks):
        # Display only the task that matches the given ID.
        found_task = [tasks[task_id]]
        task_found = True
    else:
        # If the task isn't found, pass an empty list and a flag to indicate this.
        found_task = []
        task_found = False

    return render_template("todo.html", tasks=found_task, task_found=task_found)


@app.route("/edit_task/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    """Edit a task in the tasks list.

    Args:
        task_id (int): The ID of the task to be edited.

    Returns:
        redirect: A redirect to the todo function.
    """
    # Extract form data
    title = request.form.get("title")
    content = request.form.get("content")

    # Update task in list
    current_task = tasks[task_id]
    if "editing" in current_task:
        if current_task["editing"] is True:
            current_task["title"] = title
            current_task["content"] = content
            current_task["editing"] = False
        else:
            for task in tasks:
                task["editing"] = False
            current_task["editing"] = True
    else:
        for task in tasks:
            task["editing"] = False
        current_task["editing"] = True

    return redirect(url_for("todo"))


@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """
    Delete a task from the list.

    Parameters:
        task_id (int): The ID of the task to be deleted.

    Returns:
        Redirect to the 'todo' route.
    """
    # Remove the task with the given ID from the list.
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("todo"))


# The main entry point for the application.
if __name__ == "__main__":
    # Start the Flask application with debugging enabled.
    app.run(debug=True)
