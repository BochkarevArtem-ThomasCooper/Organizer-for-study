#DBServer

import sqlite3
import PySimpleGUI as sg

con = sqlite3.connect('Study_Notes.db')
cur = con.cursor()

def first_run(): # That func. should be runned if first run detected.
 
    try:
        cur.execute('CREATE TABLE PasswordTable (User text, Password text)')
    except Exception as e:
        sg.popup('Unexpected exception!', e)
