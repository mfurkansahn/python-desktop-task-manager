import functions
import FreeSimpleGUI as Gui
import time
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ADD_ICON = resource_path(os.path.join("Tools Png", "add.png"))
COMPLETE_ICON = resource_path(os.path.join("Tools Png", "complete.png"))


Gui.theme("DarkPurple3")

clock = Gui.Text('',key="Clock")

label = Gui.Text("Type in to-do")

input_box = Gui.InputText(tooltip="Enter a todo", key='todo')
add_button = Gui.Button(image_size=(30,30), image_source=ADD_ICON, mouseover_colors="LightBlue2", tooltip="Add a Todo", key="Add")

list_box = Gui.Listbox(values=[todo.strip() for todo in functions.get_todos()], key='todos',
                      enable_events=True, size=(45,10))
edit_button = Gui.Button("Edit")
complete_button = Gui.Button(image_size=(30,30), image_source=COMPLETE_ICON, mouseover_colors="white", tooltip="Complete a todo", key="Complete")

exit_button = Gui.Button("Exit")

window = Gui.Window('My ToDo App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)

    if event in (Gui.WIN_CLOSED, "Exit"):
        break

    window["Clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))

    match event:
        case "Add":
            if values['todo'].strip() != "":
                todos = functions.get_todos()
                new_todo = values['todo'].strip() + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(
                    values=[todo.strip() for todo in todos])
            else:
                Gui.popup("Please enter a to-do", font=("Helvetica", 20))

        case "Edit":
            try:
                if not values['todo'].strip():
                    Gui.popup("Please enter a new value.", font=("Helvetica", 20))
                    continue

                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit.strip() + "\n")
                todos[index] = new_todo

                functions.write_todos(todos)
                window['todos'].update(
                    values=[todo.strip() for todo in todos]
                )
            except IndexError:
                Gui.popup("Please select an item to edit.", font=("Helvetica", 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete + "\n")
                functions.write_todos(todos)
                window['todos'].update(
                    values=[todo.strip() for todo in todos]
                )
                window['todo'].update("")
            except IndexError:
                Gui.popup("Please select an item to complete.", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()