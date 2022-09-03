import curses, pyperclip, json
from time import sleep
from decimal import Decimal
from curses import wrapper
from curses.textpad import Textbox, rectangle
#something for curses idk
def main(stdscr):
    time = 0
    menu_current = 0
    in_menu = True
    #Prints Logo for 2.5 seconds
    logo = """

                                 d8,                     
                          d8P   `8P                      
                        d888888P                          
    ?88,.d88b,?88   d8P   ?88'    88b  88bd8b,d88b  d8888b
    `?88'  ?88d88   88    88P     88P  88P'`?8P'?8bd8b_,dP
      88b  d8P?8(  d88    88b    d88  d88  d88  88P88b    
      888888P'`?88P'?8b   `?8b  d88' d88' d88'  88b`?888P'
      88P'           )88                                  
     d88            ,d8P                                  
     ?8P         `?888P'                                  

    """
    stdscr.clear()
    stdscr.addstr(6, 0, logo, curses.A_BOLD)
    stdscr.refresh()
    sleep(2.5)
    stdscr.clear()
    seg_win = curses.newwin(1, 8, 3, 2)
    seg_box = Textbox(seg_win)
    rectangle(stdscr, 2, 1, 4, 10)
    #Asks for number of segments
    stdscr.addstr(1, 1, "How many Segments are there in this video?", curses.A_BOLD)
    stdscr.refresh()
    seg_box.edit()
    segment_count = seg_box.gather()
    segment_count = int(segment_count)
    stdscr.clear()
    #Uses the number of segments to repeat debug info collection
    for i in range(segment_count):
        #Asks for debug info and stores the JSON in a variable to be parsed later
        stdscr.addstr(1, 1, "Copy the Debug Info of the Starting Frame", curses.A_BOLD)
        stdscr.addstr(2, 1, "Once this is done Press Any Key", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        #hijacks the clipboard to make it easier to copy debug info
        debug_info_start = pyperclip.paste()
        stdscr.clear()
        #copies debug info and stores the JSON in a variable to be parsed later again
        stdscr.addstr(1, 1, "Copy the Debug Info of the Ending Frame", curses.A_BOLD)
        stdscr.addstr(2, 1, "Once this is done Press Any Key", curses.A_BOLD)
        stdscr.getch()
        #hijacks the clipboard to make it easier to copy debug info again
        debug_info_end = pyperclip.paste()
        stdscr.refresh()
        stdscr.clear()
        #parses the previously sorted JSON
        debug_info_start_dict = json.loads(debug_info_start)
        debug_info_end_dict = json.loads(debug_info_end)
        #calculates the time difference between the start and end of the segment
        time = (Decimal(debug_info_end_dict['cmt']) - Decimal(debug_info_start_dict['cmt'])) + Decimal(time)
    #prints menu
    stdscr.addstr(1, 2, "[1] Just Time")
    stdscr.addstr(2, 2, "[2] Mod Note")
    stdscr.refresh()
    time = str(time)
    time = time.split(".", 1)
    #formats the time to be more than seconds and milliseconds
    if len(time) > 0:
        #takes the milliseconds and the time and stores them in different strvariables
        seconds = time[0]
        milliseconds = time[1]
        milliseconds = str(milliseconds)
        seconds = int(seconds)
    def format_time(seconds):
        seconds = int(seconds)
        minutes = seconds//60
        hours = minutes//60
        seconds = str(seconds)
        minutes = str(minutes)
        hours = str(hours)
        if seconds == "0":
            return ("0." + milliseconds)
        elif minutes == "0":
            if len(seconds) == 1:
                return (f"0{seconds}s {milliseconds}ms")
            else:
                return (f"{seconds}s {milliseconds}ms")
        elif hours == "0":
            return (f"{minutes}m {seconds}s {milliseconds}ms")
        else:
            return (f"{hours}h {minutes}m {seconds}s {milliseconds}ms")
    formatted_time = format_time(seconds)
    while in_menu:
        menu_select = stdscr.getkey()
        #menu selection
        if menu_select == "1":
            menu_current = 1
            stdscr.clear()
            stdscr.addstr(1, 2, "[1] Just Time", curses.A_REVERSE)
            stdscr.addstr(2, 2, "[2] Mod Note")
            stdscr.refresh()
        elif menu_select == "2":
            menu_current = 2
            stdscr.clear()
            stdscr.addstr(1, 2, "[1] Just Time")
            stdscr.addstr(2, 2, "[2] Mod Note", curses.A_REVERSE)
            stdscr.refresh()
        elif menu_select == "q":
            if menu_current == 0:
                continue
            elif menu_current == 1:
                #prints just the time
                in_menu = False
                stdscr.clear()
                stdscr.addstr(1, 1, f"The Final Time is {formatted_time}", curses.A_BOLD)
                stdscr.addstr(2, 1, "Press Any Key to Exit", curses.A_BOLD)
                stdscr.refresh()
            elif menu_current == 2:
                #prints the mod note and copies it to clipboard
                in_menu = False
                stdscr.clear()
                pyperclip.copy(f"Mod Note: Retimed to [b]{formatted_time}[/b] using [url=https://github.com/ConnerConnerConner/PyTime]PyTime[/url]")
                stdscr.addstr(1, 1, f"Mod Note: Retimed to {formatted_time} using PyTime", curses.A_BOLD)
                stdscr.addstr(2, 1, "Mod Note Has Been Copied to Clipboard", curses.A_BOLD)
                stdscr.addstr(3, 1, "Press Any Key to Exit", curses.A_BOLD)
                stdscr.refresh()
        else:
           continue
    stdscr.getch()

wrapper(main)