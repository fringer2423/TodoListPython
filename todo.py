from tkinter import Tk, Button, Scrollbar, Listbox, StringVar, W, N
from tkinter import ttk

from db_tools import TodoApp

db = TodoApp()


def get_selected_row(event):
    global selected_task
    index = list_bx.curselection()[0]
    selected_task = list_bx.get(index)
    title_entry.delete(0, 'end')
    title_entry.insert('end', selected_task[1])


def view_task():
    list_bx.delete(0, 'end')
    for row in db.view():
        list_bx.insert('end', row)


def add_task():
    db.insert(title_text.get())
    list_bx.delete(0, 'end')
    list_bx.insert('end', title_text.get())
    title_entry.delete(0, 'end')
    db.con.commit()
    view_task()
    clear_screen()


def delete_task():
    db.delete(selected_task[0])
    db.con.commit()
    view_task()
    clear_screen()


def clear_screen():
    title_entry.delete(0, 'end')


def update_task():
    db.update(selected_task[0], title_text.get())
    title_entry.delete(0, 'end')
    db.con.commit()
    view_task()
    clear_screen()


root = Tk()  # Создаем окно приложения

root.title("My Todo List App")  # Задаем заголовок окна
root.geometry("550x500")  # Задаем размеры окна
root.resizable(width=False, height=False)  # Задаем параметры изменяемости размера окна

# Создаем Labels и entry widgets

title_label = ttk.Label(root, text="Title")
title_label.grid(row=0, column=0, sticky=W, padx=10)
title_text = StringVar()
title_entry = ttk.Entry(root, width=35, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

# Создаем кнопку для добавления введенных данных в базу данных

add_btn = Button(root, text="Add task", command=add_task)
add_btn.grid(row=0, column=2, sticky=W)

# Создаем ListBox для отображения данных из базы данных

list_bx = Listbox(root, height=16, width=40, border=False)
list_bx.grid(row=1, column=1, columnspan=14, sticky=W, padx=3, pady=20)
list_bx.bind('<<ListboxSelect>>', get_selected_row)

# Создаем ScrollBar

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=2, rowspan=14, sticky=W + N, padx=19, pady=20)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

# Создаем прочие кнопки

modify_btn = Button(root, text="Modify Task", command=update_task)
modify_btn.grid(row=15, column=0, padx=10)

delete_btn = Button(root, text="Delete Task", command=delete_task)
delete_btn.grid(row=15, column=1, sticky=W)

exit_btn = Button(root, text="Exit App", command=root.destroy)
exit_btn.grid(row=15, column=2, sticky=W)

view_task()

root.mainloop()
