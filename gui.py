from modules.files import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[
    [label], [input_box, add_button],
])

# Read suspends the application
window.read()
window.close()