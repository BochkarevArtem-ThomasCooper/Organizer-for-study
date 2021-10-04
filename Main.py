# Main

# Things TO DO
# 1. Designing the UI.
# 2. Fresh up SQLite3 library knolege:
# - How to store a tuple object it chart (in one cell)
# - How to store a dictionary object in chart (in one cell)
# 3. Think of a way to encrypt and decrypt text data in a simpe but efficient way.
# 4. Finde a way to recive and use system paths to provide ability of calling for a needed book right from the app.
# 5. Follow PEP8 standard.
# 6. Provide documentation for the code.

import sqlite3
import PySimpleGUI as sg

import Class_Title
import DBServer as DB

layoutWelcome = [
    [sg.Input(default_text='user name', k='-UN-')],
    [sg.Input(default_text='password', k='-PASS-')],
    [sg.Button('Log in', size=(100,1))],
    [sg.Button('New user', size=(100,1))]
]

login = sg.Window('Hello!', layoutWelcome, size=(200,130))

def main(): # That func. is the entrance point

    # WINDOW with options [New user, log in]
    while True:
        
        event, values = login.read()
        if event == 'Log in':
            pass
        if event == 'New user':
            DB.new_user(values['-UN-'], values['-PASS-'])
        if event == sg.WIN_CLOSED:
            break

    #allTitles = # Here we store insances of class Title

    #allTabs = # Here we store all the ready made tabs

    #layout = [[sg.TabGroup([[
        #allTabs
    #]])]]
main()
login.close()