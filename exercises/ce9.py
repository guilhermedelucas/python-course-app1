import PySimpleGUI as sg
from bonus.converters14 import convert as feet_inches_to_meters


sg.theme('Black')

label1 = sg.Text('Enter feet: ')
input1 = sg.Input(key="feet")

label2 = sg.Text('Enter inches: ')
input2 = sg.Input(key="inches")

convert_button = sg.Button('Convert', key='convert')
exit_button = sg.Button('Exit', key="exit")
output_text = sg.Text(key="output_text")

window = sg.Window('Convertor', layout=[
    [label1, input1],
    [label2, input2],
    [convert_button, exit_button, output_text]
])


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'exit':
        break

    try:
        feet = int(values['feet'])
        inches = int(values['inches'])
        meters = feet_inches_to_meters(feet, inches)
        window['output_text'].update(value=f"{'{:.2f}'.format(round(meters, 2))}m", text_color="white")
    except ValueError:
        sg.popup('Please provide two numbers.')

window.close()