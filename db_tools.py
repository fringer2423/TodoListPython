import psycopg2 as psy

from tkinter import messagebox

from local_settings import db_config


class TodoApp:

    def __init__(self):
        self.con = psy.connect(**db_config)
        self.cursor = self.con.cursor()
        print("You have connected to database")

    def __del__(self):
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM todo")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, title):
        sql = "INSERT INTO todo(title) VALUES (%s)"
        values = [title]
        self.cursor.execute(sql, values)
        self.con.commit()
        messagebox.showinfo(title="TodoList database", message="New Task added to database")

    def update(self, id, title):
        tsql = "UPDATE todo SET title = %s WHERE id=%s"
        self.cursor.execute(tsql, [title, id])
        self.con.commit()
        messagebox.showinfo(title="TodoList database", message="Task Updated")

    def delete(self, id):
        delquery = "DELETE FROM todo WHERE id = %s"
        self.cursor.execute(delquery, [id])
        self.con.commit()
        messagebox.showinfo(title="TodoList database", message="Task Deleted")
