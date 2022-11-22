import PySimpleGUI as sg
import csv, os

working_directory = os.getcwd()

def convert_csv_array(csv_address):
    file = open(csv_address)
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)
    file.close()
    return rows

def browsing():
    layout = [  
                [sg.Text("Choose a folder:")],
                [sg.InputText(key="-FILE_PATH-"), 
                sg.FileBrowse(initial_folder=working_directory)],
                [sg.Button('Submit'), sg.Exit()]
            ]

    window = sg.Window("Display CSV", layout)



    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == "Submit":
            csv_address = values["-FILE_PATH-"]
            print(convert_csv_array(csv_address))
    window.close()


    # text = sg.popup_get_folder('Please enter a folder name')
    # sg.popup('Results', 'The value returned from popup_get_folder', text)