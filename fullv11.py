from asyncio.windows_events import NULL
import PySimpleGUI as sg
from BFS_Trackerv2 import breadthFirst, multiHop
from  create_window import create
from dayLocationContact import singleHop
from dayLocationContactv3 import singleHopv2
from singleHop import funcSingleHop
from Filebrowser import browsing, convert_csv_array
import os
import startGenv3
import graphGen
import clearall
import psycopg2

text = ""

# ----------- Create the layouts this Window will display -----------
layout1 = [[sg.Text('MAIN MENU', font=("Helvetica", 25))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('SELECT PROJECT FOLDER', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('INFECTED TRACING', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('INFECTION SIMULATION', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('PLOT GRAPH', size=(25,3), font=("Helvetica", 15))]
            
        #    [sg.Button('RUN COMPARE', size=(25,3), font=("Helvetica", 15))]
           ]

layout2 = [[sg.Text('SELECT SINGLE HOP OR MULTI HOP', font=("Helvetica", 25))],
            [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('SINGLE HOP', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('MULTI HOP', size=(25,3), font=("Helvetica", 15))]]

layout3 = [[sg.Text('SINGLE HOP CONTACT TRACING', font=("Helvetica", 25))],
            [sg.Text('', font=("Helvetica", 15))],
           [sg.Text('Enter ID: ', font=("Helvetica", 15)), sg.Input(s=15,key='_SINGLENUM_', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('Single Hop Tracker', size=(25,3), font=("Helvetica", 15))]]

layout4 = [[sg.Text('MULTI HOP CONTACT TRACING', font=("Helvetica", 25))],
            [sg.Text('', font=("Helvetica", 15))],
           [sg.Text('Enter ID:', font=("Helvetica", 15)),sg.Input(s=15,key='_MULTINUM_', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Text('Enter Day:', font=("Helvetica", 15)),sg.Input(s=15,key='_DAYNUM_', size=(25,3), font=("Helvetica", 15))],
           [sg.Text('', font=("Helvetica", 15))],
           [sg.Button('Multi Hop Tracker', size=(25,3), font=("Helvetica", 15))]]


layout5sub1 = [
            [sg.Text("Enter Infection Percentage",font='Lucida'),
            sg.Input(key='stVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='stSlider', range=(1,100))],

            [sg.Text("Enter Incubation Period", font='Lucida'),
            sg.Input(key='enVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='endSlider',range=(1,10))],

            [sg.Text("Enter Number of Suburbs", font='Lucida'),
            sg.Input(key='groupVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='GroupSlider',range=(1,10))],

            [sg.Text("Enter Number of people", font='Lucida'),
            sg.Input(key='peopleVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='peopleSlider',range=(1,10000))],

            [sg.Text("Enter Number of days", font='Lucida'),
            sg.Input(key='daysVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='daysSlider',range=(1,30))],

            [sg.Text("Enter Number of locations", font='Lucida'),
            sg.Input(key='numLocVal',size=(3, 1))],
            [sg.Slider(orientation ='horizontal', key='numLocSlider',range=(1,200))]]

layout5sub2 = [
            
            [sg.Button('SIMULATE', size=(25,3), font=("Helvetica", 15))],
            [sg.Text('', font=("Helvetica", 15))],
            [sg.Button('SET VALUES', size=(25,3), font=("Helvetica", 15))]]

layout5 = [[sg.Text('INFECTION SIMULATION', font=("Helvetica", 25))],[sg.Column(layout5sub1),
     sg.VSeperator(),
     sg.Column(layout5sub2),]]
            

layout6 = [[sg.Text('Please choose a folder path', size=(25,3), font=("Helvetica", 25))],
           [sg.Button('RETURN', size=(25,3), font=("Helvetica", 15))]]

layout7 = [[sg.Text('SELECT A FILE PATH', size=(25,3), font=("Helvetica", 25))],
            [sg.Button('SELECT FILE TO LOAD', size=(25,3), font=("Helvetica", 15))],
           [sg.Button('GET CONTACTS', size=(25,3), font=("Helvetica", 15))]]

layout8 = [[sg.Text('Graph Choices', size=(25,3), font=("Helvetica", 25))],
            [sg.Checkbox('Susceptible',key='Susceptible', font=("Helvetica", 15)), sg.Checkbox('Exposed',key='Exposed', font=("Helvetica", 15)),
            sg.Checkbox('Infected',key='Infected', font=("Helvetica", 15)),sg.Checkbox('Removed',key='Removed', font=("Helvetica", 15)),
            sg.Checkbox('Group1',key='Group1_dis', font=("Helvetica", 15)),
             sg.Checkbox('Group2',key='Group2_dis', font=("Helvetica", 15)),sg.Checkbox('Group3',key='Group3_dis', font=("Helvetica", 15)),
             sg.Checkbox('Group4',key='Group4_dis',visible=False)],
             [sg.Text('', size=(25,3), font=("Helvetica", 25))],
            [sg.Button('CONFIRM GRAPH SELECTION', size=(30,3), font=("Helvetica", 15))]]



layoutMain = [[
    sg.Button('BACK', size=(15,2), font=("Helvetica", 15)), 
    # sg.Button('MAIN MENU', size=(15,2), font=("Helvetica", 15)), 
    # sg.Button('Confirm selection', size=(15,2), font=("Helvetica", 15))
    # sg.Button('Single Hop', size=(15,2), font=("Helvetica", 15)), 
    # sg.Button('Multi Hop', size=(15,2), font=("Helvetica", 15)), 
    # sg.Button('Simulation', size=(15,2), font=("Helvetica", 15)), 
    # sg.Button('Exit', size=(10,2), font=("Helvetica", 15))
    ]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[
[sg.Column(layoutMain, key='-COL100-')], 

[sg.Column(layout1, visible=True, key='-COL1-', vertical_alignment='center', justification='center',element_justification='center'), 
sg.Column(layout2, visible=False, key='-COL2-', vertical_alignment='center', justification='center',element_justification='center'), 
sg.Column(layout3, visible=False, key='-COL3-', vertical_alignment='center', justification='center',element_justification='center'),
sg.Column(layout4, visible=False, key='-COL4-', vertical_alignment='center', justification='center',element_justification='center'),
sg.Column(layout5, visible=False, key='-COL5-', vertical_alignment='center', justification='center',element_justification='center'),
sg.Column(layout6, visible=False, key='-COL6-', vertical_alignment='center', justification='center',element_justification='center'),
sg.Column(layout7, visible=False, key='-COL7-', vertical_alignment='center', justification='center',element_justification='center'),
sg.Column(layout8, visible=False, key='-COL8-', vertical_alignment='center', justification='center',element_justification='center')
]
]]
window = sg.Window('COVID-19 Tracking system', layout,size=(1400, 800))

layout = 1  # The currently visible layout
previous = [1]
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'BACK':
        window[f'-COL{layout}-'].update(visible=False)
        try:
            layout = previous.pop(-1)
            window[f'-COL{layout}-'].update(visible=True)
        except:
            window[f'-COL1-'].update(visible=True)
        
    if event == 'MAIN MENU':
        previous.append(layout)
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'INFECTED TRACING':
        if text != "":
            previous.append(layout)
            window[f'-COL{layout}-'].update(visible=False)
            layout = 2
            window[f'-COL{layout}-'].update(visible=True)
        else:
            previous.append(layout)
            window[f'-COL1-'].update(visible=False)
            window[f'-COL{layout}-'].update(visible=False)
            layout = 6
            window[f'-COL{layout}-'].update(visible=True)
            # infection_chance = 30
            # incubation_period = 2
    if event == 'SINGLE HOP':
        previous.append(layout)
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'MULTI HOP':
        previous.append(layout)
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'INFECTION SIMULATION':
        if text != "":
            previous.append(layout)
            window[f'-COL{layout}-'].update(visible=False)
            layout = 5
            window[f'-COL{layout}-'].update(visible=True)
        else:
            previous.append(layout)
            window[f'-COL{layout}-'].update(visible=False)
            layout = 6
            window[f'-COL{layout}-'].update(visible=True)
    if event == 'RETURN':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
    if event == "CONTACT FILE":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 7
        window[f'-COL{layout}-'].update(visible=True)
    if event == "PLOT GRAPH":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 8
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'SELECT PROJECT FOLDER':
        text = sg.popup_get_folder('Please enter a folder name')
    if event == 'SELECT FILE TO LOAD':
        file_name = sg.popup_get_file('Please enter a folder name')

    if event == 'GET CONTACTS':
        pass
    if event == "RUN COMPARE":
        singleHopv2(text,peopleNum)
    if event == "SET VALUES":
        window['stVal'].update(int(values['stSlider']))
        window['enVal'].update(int(values['endSlider']))
        window['groupVal'].update(int(values['GroupSlider']))
        window['peopleVal'].update(int(values['peopleSlider']))
        window['daysVal'].update(int(values['daysSlider']))
        window['numLocVal'].update(int(values['numLocSlider']))
        event,values=window.read()
        window['stVal'].update(int(values['stSlider']))
        window['enVal'].update(int(values['endSlider']))
        window['groupVal'].update(int(values['GroupSlider']))
        window['peopleVal'].update(int(values['peopleSlider']))
        window['daysVal'].update(int(values['daysSlider']))
        window['numLocVal'].update(int(values['numLocSlider']))
        infection_chance=int(values['stVal'])
        incubation_period=int(values['enVal'])
        groupValue = int(values['groupVal'])
        peopleNum = int(values['peopleVal'])
        days = int(values['daysVal'])
        numLoc = int(values['numLocVal'])
    if event == 'SIMULATE':
        clearall.clearAllFiles(text,days,numLoc)
        startGenv3.mainGen(text,infection_chance,incubation_period,groupValue,peopleNum,days,numLoc)
        singleHopv2(text,peopleNum,numLoc)
    if event == 'CONFIRM GRAPH SELECTION':
        if values['Susceptible'] == True:
            Sus = 1
        else:
            Sus = 0
        if values['Exposed'] == True:
            Exp = 1
        else:
            Exp = 0
        if values['Infected'] == True:
            Inf = 1
        else:
            Inf = 0
        if values['Removed'] == True:
            Rem = 1
        else:
            Rem = 0
        if values['Group1_dis'] == True:
            grp1_dis = 1
        else:
            grp1_dis = 0
        if values['Group2_dis'] == True:
            grp2_dis = 1
        else:
            grp2_dis = 0
        if values['Group3_dis'] == True:
            grp3_dis = 1
        else:
            grp3_dis = 0
        if values['Group4_dis'] == True:
            grp4_dis = 1
        else:
            grp4_dis = 0
            graphGen.graphVisual(text,Sus,Exp,Inf,Rem,grp1_dis,grp2_dis,grp3_dis,grp4_dis)
    if event == 'Single Hop Tracker':
        try:
            SingleHopData = funcSingleHop(values['_SINGLENUM_'],text)
            SingleHopheading = ['Person_ID', 'Contact_ID', 'Start', 'End', 'Duration', 'locationNumber', 'day', 'Person_ID_status', 'Contact_ID_status']
            create(SingleHopData, SingleHopheading)
        except:
            pass
    if event == 'Multi Hop Tracker':
        # try:
        entire_tracker = multiHop(text)
        MultiHopData = breadthFirst(entire_tracker,values['_MULTINUM_'],values['_DAYNUM_'],2)
        MultiHopheading = ['Person_ID', 'Day', 'Start', 'Number of Hops']
        create(MultiHopData, MultiHopheading)
        # except:
        #     pass
    # if event == 'Get Trace':
    #     data = []
    #     try:
    #         connection = psycopg2.connect(  host="localhost",
    #                                         database="general_data",
    #                                         user="postgres",
    #                                         password="a1234567890!!!")
    #         cursor = connection.cursor()
    #         postgreSQL_select_Query = "select * from all_info;"

    #         cursor.execute(postgreSQL_select_Query)
    #         print("Selecting rows from mobile table using cursor.fetchall")
    #         row = cursor.fetchone()

    #         while row is not None:
    #             print(row)
    #             new = [row[0], row[1], row[2], row[3], row[4]]
    #             print(new)
    #             data.append(new)
    #             row = cursor.fetchone()

    #         heading = ['Person_ID', 'Contact_ID', 'Location', 'Time_In', 'Time_Out']

    #         create(data, heading)
    #     except (Exception, psycopg2.Error) as error:
    #         print("Error while fetching data from PostgreSQL", error)
            
    #     window[f'-COL{layout}-'].update()

window.close()
