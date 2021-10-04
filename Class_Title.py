#Class Title

import PySimpleGUI as sg

import DBServer as DB

sg.theme('DarkBlack1')

class Title: # That class represents notes for one studeing metter

    def __init__(self, titleName, user = 'user',*spentTime):
        self.titleName = titleName
        self.user = user
        self.spentTime = spentTime

    #gef get_data_from_db(self): # That function is in control of reading data from the data base

    def appirance(self): # That function returnes the look of the note

        topic = 'Notes for: ' + self.titleName
        timeInvolved = f'Studyed for {self.spentTime[0]} days, {self.spentTime[1]} hours and {self.spentTime[2]} minutes.'

        litTableName = DB.input_modifier(self.titleName, self.user)+'topicTitles'
        litDict = {}
        litDict = DB.get_literature_dict(litTableName) # !! We need a func that going to resive title-name and open exact file. So title-name is 'key' and path to the file is 'value'
        
        layout = [
            [sg.Text(Text =topic, auto_size_text=True)],
            [sg.Text(Text =timeInvolved, auto_size_text=True), sg.Button('-TSTART-')],
            [sg.Combo(DB.get_literature_list(litTableName), bind_return_key=True, enable_events=True, readonly=True, k='-COMBO-')],
            [sg.Multiline(default_text='Tipe your notes in here.', size=(200,200,),  key='-LOG-')],
            [sg.Input(key='-IN-', size=(10,1)), sg.CalendarButton('Choose date', close_when_date_chosen=True,  target='-IN-', location=(0,0), format='%d.%m.%Y', no_titlebar=False, )]
            ]

        return sg.Tab(self.titleName, layout)

    #def save_result(self): # That function updates data in datdbase.
