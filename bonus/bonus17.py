import PySimpleGUI as sg
from zip_extractor import extract_archive

label1 = sg.Text('Select archive:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Extract')
output_label = sg.Text(key="output")

window = sg.Window('Archive Extractor',
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [compress_button, output_label]
                   ])

while True:
    event, values = window.read()
    filepath = values['archive']
    folder = values['folder']
    extract_archive(filepath, folder)
    window['output'].update(value='Extraction completed!')

    if event == sg.WIN_CLOSED:
        break


window.close()