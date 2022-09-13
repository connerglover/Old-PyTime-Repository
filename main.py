from json import loads as json_loads
from pyperclip import copy
import PySimpleGUI as sg
from decimal import Decimal as d
from math import floor as round_down

sg.theme('DarkGrey12')

class timer:
    # Rounds to the nearest frame
    def frame_round(time, fps): # Rounds to the nearest frame
        time = d(time)
        time = round(time, 3)
        output = d(time - time%(d(1)/fps)) #Credit to Slush0Puppy for this 1 Line of Code
        return round(output, 3)

    #Formats Time from Seconds to SRC Format
    def format(time):
        time = str(time)
        time = time.split('.', 1)
        seconds = time[0]
        milliseconds = time[1]
        milliseconds = str(milliseconds)
        seconds = int(seconds)
        minutes = seconds//60
        hours = minutes//60
        if seconds > 60: #makes sure that the seconds are less than 60
            seconds = seconds - (minutes * 60)
        if minutes > 60: #makes sure that the minutes are less than 60
            minutes = minutes - (hours * 60)
        seconds = str(seconds)
        minutes = str(minutes)
        hours = str(hours)
        #Combines the time into a single string
        if seconds == '0':
            return (f'0s {milliseconds}ms')
        elif minutes == '0':
            if len(seconds) == 1:
                return (f'0{seconds}s {milliseconds}ms')
            else:
                return (f'{seconds}s {milliseconds}ms')
        elif hours == '0':
            return (f'{minutes}m {seconds}s {milliseconds}ms')
        else:
            return (f'{hours}h {minutes}m {seconds}s {milliseconds}ms')
        
    #Calclates the Loads
    def load(dbi_end, dbi_start, fps):
        try: #Turns JSON into a Dictionary and Checks if it is Valid (Start)
            dbis_dict = json_loads(dbi_start)
        except:
            sg.popup('Error (Start)', 'Debug Info is not valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try: #Turns JSON into a Dictionary and Checks if it is Valid (End)
            dbie_dict = json_loads(dbi_end)
        except:
            sg.popup('Error (End)', 'Debug Info is not valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try: #Calculates the Loads from CMT (Start)
            cmt_start = timer.frame_round(d(dbie_dict['cmt']), fps)
        except:
            sg.popup('Error (CMT Start)', 'CMT is not Valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try:#Calculates the Loads from CMT (End)
            cmt_end = timer.frame_round(d(dbis_dict['cmt']), fps)
        except:
            sg.popup('Error (CMT End)', 'CMT is not Valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        loads = timer.frame_round((d(cmt_end) - d(cmt_start))) #Calculates the Loads
        if -abs(loads) == loads: #Checks if the Loads are Negative
            sg.popup('Error', 'The start is greater than the end.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        #Clears Loads Input Box
        main_window['dbis_loads'].update('')
        main_window['dbie_loads'].update('')
        sg.popup(f'Loads Added', title = 'Loads', font = ('Helvetica', 16), icon='PyTime.ico') #Success Message
        return loads #Returns Loads

    #Calculates the Final Time
    def final(dbi_start, dbi_end, loads, fps):
        try: #Turns JSON into a Dictionary and Checks if it is Valid (Start)
            dbis_dict = json_loads(dbi_start)
        except:
            sg.popup('Error (Start)', 'Debug Info is not valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try: #Turns JSON into a Dictionary and Checks if it is Valid (End)
            dbie_dict = json_loads(dbi_end)
        except:
            sg.popup('Error (End)', 'Debug Info is not valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try: #Calculates the Loads from CMT (Start)
            cmt_start = timer.frame_round(d(dbie_dict['cmt']), fps)
        except:
            sg.popup('Error (CMT Start)', 'CMT is not Valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        try: #Calculates the Loads from CMT (End)
            cmt_end = timer.frame_round(d(dbis_dict['cmt']), fps)
        except:
            sg.popup('Error (CMT End)', 'CMT is not Valid.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        time_loads = (d(cmt_end) - d(cmt_start)) #Calculates the Time with Loads
        if -abs(time_loads) == time_loads: #Checks if the Loads are Negative
            sg.popup('Error', 'The start is greater than the end.', title = 'Error', icon='PyTime.ico') #Error Message
            return
        time_noloads = time_loads - loads #Takes away the loads from the Time
        #Formats the Time
        no_loads = timer.format(time_noloads)
        with_loads = timer.format(time_loads)
        if loads == 0: #Check if there's loads
            final_confirm = sg.popup_yes_no(f'Without Loads: {no_loads}', 'Would you like the Mod Note to be Copied to the Clipboard?', title = 'Results', icon='PyTime.ico') #Copy Confirmation #Success Message
            if final_confirm == 'Yes':
                copy(f'Mod Note: Retimed to {no_loads} https://github.com/ConnerConnerConner/PyTime') #Copies the Mod Note to the Clipboard
            elif final_confirm == 'No':
               return 
        else:
            final_confirm = sg.popup_yes_no(f'Without Loads: {no_loads}, With Loads: {with_loads}', 'Mod Note Copied to Clipboard', title = 'Results', icon='PyTime.ico') #Copy Confirmation #Success Message
        if final_confirm == 'Yes':
            copy(f'Mod Note: Retimed to {no_loads} using https://github.com/ConnerConnerConner/PyTime') #Copies the Mod Note to the Clipboard
        elif final_confirm == 'No':
             return

#GUI Layout

main_layout = [
        [sg.Text('PyTime', font = ('Helvetica', 36)), sg.Text('   FPS', font = (' Helvetica', 30)), sg.InputText('60', size = (5, 1), key = 'fps', font = ('Helvetica', 30))],
        [sg.InputText(key = 'dbis', font = ('Helvetica', 16), pad = ((5, 0), (0, 0)), size = (20, 1)), sg.Text('  Debug Info Start', font = ('Helvetica', 16), justification = 'right')],
        [sg.InputText(key = 'dbie', font = ('Helvetica', 16), pad = ((5, 0), (0, 0)), size = (20, 1)), sg.Text('  Debug Info End', font = ('Helvetica', 16), justification = 'right')],
        [sg.InputText(key = 'dbis_loads', font = ('Helvetica', 14), pad = ((5, 0), (0, 0)), size = (15, 1)), sg.Text('   Debug Info Start (Loads)', font = ('Helvetica', 14), justification = 'right')],
        [sg.InputText(key = 'dbie_loads', font = ('Helvetica', 14), pad = ((5, 0), (0, 0)), size = (15, 1)), sg.Text('   Debug Info End (Loads)', font = ('Helvetica', 14), justification = 'right')],
        [sg.Button('Calculate', font = ('Helvetica', 16)), sg.Button('Add Loads', font = ('Helvetica', 16)), sg.Button('Remove All Loads', font = ('Helvetica', 16))]
    ]

main_window = sg.Window('PyTime', main_layout, resizable = False, element_justification = 'left', size=(447, 253),  icon='PyTime.ico') #Creates the Window

#Main Loop

while True:
    event, values = main_window.read() #Reads the Window's Boxes
    if event == sg.WIN_CLOSED: #Checks if the Window is Closed
        break
    if event == 'Remove All Loads': #Checks if the Remove All Loads Button is Pressed
        lr_confirm = sg.popup_yes_no('Are you sure you want to remove all loads?', title = 'Remove All Loads', font = ('Helvetica', 16), icon='PyTime.ico') #Confirmation
        if lr_confirm == 'Yes':
            #Clears Loads Input Box
            main_window['dbis_loads'].update('')
            main_window['dbie_loads'].update('')
            #Clears Loads Variable
            loads = 0
        elif lr_confirm == 'No':
            continue #Continues the Loop
    if event == 'Add Loads': #Checks if the Add Loads Button is Pressed
        #Gets the Values from the Loads Input Boxes
        dbis_loads = values['dbis_loads'] 
        dbiel_loads = values['dbie_loads']
        fps = values['fps']
        try: #Checks if FPS is Valid
            fps = d(fps)
        except:
            sg.popup('Error (FPS)', 'FPS is not a valid number.', title = 'Error', icon='PyTime.ico') #Error Message
            continue
        if not 'loads' in globals(): #Checks if the Loads Variable Exists
            loads = timer.load(dbis_loads, dbiel_loads, fps) #Calculates the Loads
        else:
            try:
                loads = timer.load(dbis_loads, dbiel_loads, fps) + loads #Calculates the Loads
            except:
                continue
    if event == 'Calculate':
        #Gets the Values from the Input Boxes
        dbi_start = values['dbis']
        dbi_end = values['dbie']
        fps = values['fps']
        try: #Checks if FPS is Valid
            fps = d(fps)
        except:
            sg.popup('Error (FPS)', 'FPS is not an valid number.', title = 'Error', icon='PyTime.ico')
            continue
        if not 'loads' in globals(): #Checks if the Loads Variable Exists
            loads = 0 #Sets Loads to 0 if it doesn't
        #Changes input boxes
        main_window['dbis'].update('')
        main_window['dbie'].update('')
        timer.final(dbi_start, dbi_end, loads, fps) #Calculates the Time

main_window.close()

#Credit to Rekto for Helping Me With Everything
#Credit to Slush0Puppy for Frane Rounding
#Made by Conner Speedrunning