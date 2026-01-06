import functions
import FreeSimpleGUI as GUI

label = GUI.Text("Type in to-do")
input_box = GUI.InputText(tooltip="Enter a todo", key='todo')
add_button = GUI.Button("Add")

window = GUI.Window('My ToDo App',
                    layout=[[label],[input_box, add_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)

        case GUI.WIN_CLOSED:
            break


window.close()