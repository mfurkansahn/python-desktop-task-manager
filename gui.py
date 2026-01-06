import functions
import FreeSimpleGUI as GUI

label = GUI.Text("Type in to-do")
input_box = GUI.InputText(tooltip="Enter a todo", key='todo')
add_button = GUI.Button("Add")
list_box = GUI.Listbox(values=[todo.strip() for todo in functions.get_todos()], key='todos',
                      enable_events=True, size=(45,10))
edit_button = GUI.Button("Edit")

window = GUI.Window('My ToDo App',
                    layout=[[label],[input_box, add_button], [list_box, edit_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(
                values=[todo.strip() for todo in todos])
        case "Edit":
            if not values['todos']:
                GUI.popup("Please select a task to edit")
                continue

            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit + "\n")
            todos[index] = new_todo

            functions.write_todos(todos)
            window['todos'].update(
                values=[todo.strip() for todo in todos]
            )

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case GUI.WIN_CLOSED:
            break


window.close()