import PySimpleGUI as sg

def create(data_array, headings):

    contact_information_window_layout = [
        [sg.Table(values=data_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Data Table')]
    ]

    contact_information_window = sg.Window("Data Information", 
    contact_information_window_layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    contact_information_window.close()