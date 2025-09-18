# file for establishing database and its connections

import sqlite3  # file for sql connection


# make a DB connection
def create_connection():
    conn = sqlite3.connect("storage/tasks.sql")
    cur = conn.cursor()
    return conn, cur


# make structure of the DB - unless exists already
def makeStructure():
    conn, cur = create_connection()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)"
    )
    conn.commit()

    conn.close()


# ... ["todo", "pending", "done"]


# if task exists
def task_exists(id):
    conn, cur = create_connection()

    cur.execute = ("SELECT 1 FROM tasks WHERE id = (?)", [id])


# count tasks
def count_tasks():
    conn, cur = create_connection()
    cur.execute("SELECT COUNT(*) FROM tasks")
    n = cur.fetchone()
    conn.close()
    return n[0]


def add_task(task, status="todo"):
    conn, cur = create_connection()
    if status not in ["todo", "pending", "done"]:
        status = "todo"  # just in case
    cur.execute("INSERT INTO tasks (task, status) VALUES((?),(?))", (task, status))
    conn.commit()
    added = cur.rowcount > 0
    conn.close()
    if added:
        print("Added task.")
    return added


def remove_task(id):
    conn, cur = create_connection()
    cur.execute("DELETE FROM tasks WHERE id = (?)", (id,))
    conn.commit()
    removed = cur.rowcount > 0
    conn.close()
    if removed:
        print("Removed task.")


def remove_task_by_status(status):
    if status not in ["todo", "pending", "done"]:
        print("Incorrect Status")
        return  # just in case

    conn, cur = create_connection()
    cur.execute("DELETE FROM tasks WHERE status = (?)", (status,))
    conn.commit()
    conn.close()


# update task only
def update_task(task_id, new_task):
    conn, cur = create_connection()
    cur.execute("UPDATE tasks SET task = (?) WHERE id = (?)", (new_task, task_id))
    conn.commit()
    update = cur.rowcount > 0
    conn.close()
    if update:
        print("Updated task.")


# update task status
def update_task_status(task_id, updated_status):
    conn, cur = create_connection()
    cur.execute(
        "UPDATE tasks SET status = (?) WHERE id = (?)", (updated_status, task_id)
    )
    conn.commit()
    update = cur.rowcount > 0
    conn.close()
    if update:
        print(f"Updated task status to: {updated_status}")


# return  tasks with ID (for mapping)
def get_tasks_with_id():
    conn, cur = create_connection()
    cur.execute("SELECT id, task, status from tasks")
    results = cur.fetchall()  # stores a list of tuples
    conn.close()
    return results


def fetch_id_from_task(task):
    conn, cur = create_connection()
    cur.execute("SELECT id FROM tasks WHERE task = (?)", (task))


# normal return a tuple and such
def get_tasks():
    conn, cur = create_connection()
    cur.execute("SELECT task, status from tasks")
    results = cur.fetchall()  # stores a list of tuples
    return results
