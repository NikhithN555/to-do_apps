import functions
import FreeSimpleGUI as sg  # use other people's code
import time
import os

if not os.path.exists("todos.txt"):  # decision
    with open("todos.txt", "w") as file:
        pass

sg.theme("Dark Amber 5")

clock = sg.Text('', key='clock')  # variable
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10, mouseover_colors="LightBlue", tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:  # loop
    event, values = window.read(timeout=200)

    if event == sg.WIN_CLOSED:
        break  # Exit loop if window is closed

    # Update clock in the window
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:  # decision
        case "Add":
            new_todo = values['todo'].strip()  # Strip input to remove leading/trailing spaces
            if new_todo:  # Only add if the todo is not empty
                todos = functions.get_todos()
                todos.append(new_todo + "\n")  # Add newline for formatting
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # Update the list box
                window['todo'].update(value="")  # Clear input box
            else:
                sg.popup("Please enter a valid todo", font=("Helvetica", 20))  # Notify user for empty todo

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # Get selected todo
                new_todo = values['todo']
                if new_todo.strip():  # Only edit if the new todo is not empty
                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value="")
                else:
                    sg.popup("Please enter a valid todo to edit", font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))  # Handle case if no item is selected

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]  # Get selected todo
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))  # Handle case if no item is selected

        case 'todos':
            if values['todos']:  # Only update if a todo is selected
                window['todo'].update(value=values['todos'][0])  # Show the selected todo in the input box

        case 'Exit':
            break  # Exit the loop and close the window

window.close()
