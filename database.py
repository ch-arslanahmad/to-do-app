# file for establishing database and its connections

import sqlite3  # file for sql connection


def create_connection():
    conn = sqlite3.connect("storage/tasks.db")
    cur = conn.cursor()
    return conn, cur


def makeStructure():
    conn, cur = create_connection()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)"
    )
    conn.commit()

    conn.close()


def addTask():
    conn, cur = create_connection()
    cur.execute = ""
    conn.close()


makeStructure()
