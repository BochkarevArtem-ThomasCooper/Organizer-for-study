#DBServer

import sqlite3
import PySimpleGUI as sg

import Class_Title as CTitle

sg.theme('DarkBlack1')

con = sqlite3.connect('Study_Notes.db')
cur = con.cursor()

def input_modifier(title, user='user'): # func to make user input robust   
    safeName = title.replace(' ','_') + user
    return safeName


def first_run(): # That func. creates the main table we use to store our users login information.
 
    try:
        cur.execute('CREATE TABLE if not exists PasswordTable (User text, Password text)')
    except Exception as e:
        sg.popup('Unexpected exception!\n', e)

def new_user(user,password): # creating new user
    safeUser = user.replace(' ','_')+'Table'
    cur.execute(f'INSERT INTO PasswordTable VALUES ({user},{password})')
    cur.execute(f'CREATE TABLE if not exists {safeUser} (Topic text, TimeSpent text)')

def new_title(title, user='user'): # Creates tables to store information about new title, studyng by user. 

    try:
        cur.execute('CREATE TABLE if not exists %s (Date text, Note text)' %(input_modifier(title, user)+'topicLog'))
        cur.execute('CREATE TABLE if not exists %s (TiteName text, Path text)' %(input_modifier(title, user)+'topicTitles'))
        con.commit()
    except Exception as e:
        sg.popup('Unexpected exception!\n', e)

def get_literature_dict(tablename): # making a dictionaty object from table
    litDict = {}
    try:
        for name, path in cur.execute(f'SELECT * FROM {tablename}'):
            litDict[name] = path
    except Exception as e:
        sg.popup('Unexpected exception!\n', e)
    return litDict

def get_literature_list(tablename): # making a list object with title names onely, from table
    litList = []
    try:
        for name in cur.execute(f'SELECT TiteName FROM {tablename}'):
            litList.append(name)
    except Exception as e:
        sg.popup('Unexpected exception!\n', e)
    return litList

def initiating_instances(User): # Initiates instances of class Title using data from data base
    tablename = input_modifier(title, user)
    titleList = []
    try:
        for title, timeS in cur.execute(f'SELECT TiteName FROM {tablename}'):
            titleList.append(CTitle.Title())
    except Exception as e:
        sg.popup('Unexpected exception!\n', e)
    return titleList
