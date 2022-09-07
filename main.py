import json
import pyperclip
import PySimpleGUI as sg
from decimal import Decimal as d

sg.theme('DarkGrey12')

class timer:
    def format(time):
        time = str(time)
        time = time.split('.', 1)
        if len(time) > 0:
            seconds = time[0]
            milliseconds = time[1]
            milliseconds = str(milliseconds)
            seconds = int(seconds)
        def seconds_to_time(seconds):
            seconds = int(seconds)
            minutes = seconds//60
            hours = minutes//60
            if seconds > 59:
                seconds = seconds - 60
            seconds = str(seconds)
            minutes = str(minutes)
            hours = str(hours)
            if seconds == '0':
                return ('0.' + milliseconds)
            elif minutes == '0':
                if len(seconds) == 1:
                    return (f'0{seconds}.{milliseconds}')
                else:
                    return (f'{seconds}.{milliseconds}')
            elif hours == '0':
                return (f'{minutes}:{seconds}.{milliseconds}')
            else:
                return (f'{hours}:{minutes}:{seconds}.{milliseconds}')
        return seconds_to_time(seconds)

    def load(dbi, dbe):
        try:
            dbi_dict = json.loads(dbi)
        except:
            sg.popup('Error (Start)', 'Debug Info is not valid.', title = 'Error')
            return False
        try:
            dbe_dict = json.loads(dbe)
        except:
            sg.popup('Error (End)', 'Debug Info is not valid.', title = 'Error')
            return False
        loads = d(dbe_dict['cmt']) - d(dbi_dict['cmt'])
        return loads

    def final(dbi, dbe, loads):
        try:
            dbi_dict = json.loads(dbi)
        except:
            sg.popup('Error (Start)', 'Debug Info is not valid.', title = 'Error')
            return
        try:
            dbe_dict = json.loads(dbe)
        except:
            sg.popup('Error (End)', 'Debug Info is not valid.', title = 'Error')
            return
        if 'time' in locals() or 'time' in globals():
            time = (d(dbe_dict['cmt']) - d(dbi_dict['cmt'])) + d(time)
        else:
            time = (d(dbe_dict['cmt']) - d(dbi_dict['cmt']))
        time_loads = time
        time = time - loads
        no_loads = format(time)
        with_loads = format(time_loads)
        if loads == 0:
            final_confirm = sg.popup_yes_no(f'Without Loads: {no_loads}', 'Would you like the Mod Note to be Copied to the Clipboard?', title = 'Results')
            if final_confirm == 'Yes':
                pyperclip.copy(f'Mod Note: Retimed to [b]{no_loads}[/b] using [url = https://github.com/ConnerConnerConner/PyTime]PyTime[/url]')
            elif final_confirm == 'No':
               return 
        else:
            final_confirm = sg.popup_yes_no(f'Without Loads: {no_loads}, With Loads: {with_loads}', 'Mod Note Copied to Clipboard', title = 'Results')
        if final_confirm == 'Yes':
            pyperclip.copy(f'Mod Note: Retimed to [b]{no_loads}[/b] using [url = https://github.com/ConnerConnerConner/PyTime]PyTime[/url]')
        elif final_confirm == 'No':
             return

main_layout = [
    [sg.Text('PyTime', font = ('Helvetica', 36))],
    [sg.InputText(key = 'dbi', font = ('Helvetica', 16), pad = ((5, 0), (0, 0)), size = (20, 1)), sg.Text('  Debug Info Start', font = ('Helvetica', 16), justification = 'right')],
    [sg.InputText(key = 'dbe', font = ('Helvetica', 16), pad = ((5, 0), (0, 0)), size = (20, 1)), sg.Text('  Debug Info End', font = ('Helvetica', 16), justification = 'right')],
    [sg.InputText(key = 'dbi_loads', font = ('Helvetica', 14), pad = ((5, 0), (0, 0)), size = (15, 1)), sg.Text('   Debug Info Start (Loads)', font = ('Helvetica', 14), justification = 'right')],
    [sg.InputText(key = 'dbe_loads', font = ('Helvetica', 14), pad = ((5, 0), (0, 0)), size = (15, 1)), sg.Text('   Debug Info End (Loads)', font = ('Helvetica', 14), justification = 'right')],
    [sg.Button('Calculate', font = ('Helvetica', 16)), sg.Button('Add Loads', font = ('Helvetica', 16)), sg.Button('Remove All Loads', font = ('Helvetica', 16))]
]

main_window = sg.Window('PyTime', main_layout, resizable = False, element_justification = 'left', size=(447, 253),  icon='PyTime.ico')

while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Remove All Loads':
        lr_confirm = sg.popup_yes_no('Are you sure you want to remove all loads?', title = 'Remove All Loads', font = ('Helvetica', 16))
        if lr_confirm == 'Yes':
            main_window['dbi_loads'].update('')
            main_window['dbe_loads'].update('')
            loads = 0
        elif lr_confirm == 'No':
            continue
    if event == 'Add Loads':
        dbil = values['dbi_loads']
        dbel = values['dbe_loads']
        if not 'loads' in globals():
            loads = timer.load(dbil, dbel)
        else:
            loads = timer.load(dbil, dbel) + loads
    if event == 'Calculate':
        dbi = values['dbi']
        dbe = values['dbe']
        if not 'loads' in globals():
            loads = 0
        timer.final(dbi, dbe, loads)

main_window.close()