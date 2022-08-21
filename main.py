import decimal
from rich import print
from rich.prompt import Prompt

time = 0.0
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

segment = int(Prompt.ask("How many Segments are there in the Video"))
for _ in range(segment):
    print("\n")
    for _ in range(1):
        blank = Prompt.ask("(Debug Info) What is the Starting Frame?")
        for _ in range(4):
            blank = input(" ")
        debug_info_start = input(" ")
        for _ in range(61):
            blank = input(" ")
        if not blank == "}":
            blank = input(" ")
            if not blank == "}":
                blank = input(" ")
                if not blank == "}":
                    blank = input(" ")
                    if not blank == "}":
                        blank = input(" ")
                        if not blank == "}":
                            blank = input(" ")
                            if not blank == "}":
                                blank = input(" ")
                                if not blank == "}":
                                    blank = input(" ")
                                    if not blank == "}":
                                        blank = input(" ")
                                        if not blank == "}":
                                            blank = input(" ")
                                            if not blank == "}":
                                                blank = input(" ")
                                                if not blank == "}":
                                                    blank = input(" ")
                                                    if not blank == "}":
                                                        blank = input(" ")
                                                        if not blank == "}":
                                                            blank = input(" ")
                                                            if not blank == "}":
                                                                blank = input(" ")
                                                                if not blank == "}":
                                                                    blank = input(" ")
                                                                    if not blank == "}":
                                                                        blank = input(" ")
                                                                        if not blank == "}":
                                                                            blank = input(" ")
                                                                            if not blank == "}":
                                                                                blank = input(" ")
                                                                                if not blank == "}":
                                                                                    blank = input(" ")
                                                                                    if not blank == "}":
                                                                                        blank = input(" ")
                                                                                        if not blank == "}":
                                                                                            blank = input(" ")
                                                                                            if not blank == "}":
                                                                                                blank = input(" ")
                                                                                                if not blank == "}":
                                                                                                    blank = input(" ")
                                                                                                    if not blank == "}":
                                                                                                        blank = input(
                                                                                                            " ")
                                                                                                        if not blank == "}":
                                                                                                            blank = input(
                                                                                                                " ")
                                                                                                            if not blank == "}":
                                                                                                                blank = input(
                                                                                                                    " ")
                                                                                                                if not blank == "}":
                                                                                                                    blank = input(
                                                                                                                        " ")
                                                                                                                    if not blank == "}":
                                                                                                                        blank = input(
                                                                                                                            " ")
                                                                                                                        if not blank == "}":
                                                                                                                            blank = input(
                                                                                                                                " ")
    print("\n")
    for _ in range(1):
        blank = Prompt.ask("(Debug Info) What is the Ending Frame?")
        for _ in range(4):
            blank = input(" ")
        debug_info_end = input(" ")
        for _ in range(61):
            blank = input(" ")
        if not blank == "}":
            blank = input(" ")
            if not blank == "}":
                blank = input(" ")
                if not blank == "}":
                    blank = input(" ")
                    if not blank == "}":
                        blank = input(" ")
                        if not blank == "}":
                            blank = input(" ")
                            if not blank == "}":
                                blank = input(" ")
                                if not blank == "}":
                                    blank = input(" ")
                                    if not blank == "}":
                                        blank = input(" ")
                                        if not blank == "}":
                                            blank = input(" ")
                                            if not blank == "}":
                                                blank = input(" ")
                                                if not blank == "}":
                                                    blank = input(" ")
                                                    if not blank == "}":
                                                        blank = input(" ")
                                                        if not blank == "}":
                                                            blank = input(" ")
                                                            if not blank == "}":
                                                                blank = input(" ")
                                                                if not blank == "}":
                                                                    blank = input(" ")
                                                                    if not blank == "}":
                                                                        blank = input(" ")
                                                                        if not blank == "}":
                                                                            blank = input(" ")
                                                                            if not blank == "}":
                                                                                blank = input(" ")
                                                                                if not blank == "}":
                                                                                    blank = input(" ")
                                                                                    if not blank == "}":
                                                                                        blank = input(" ")
                                                                                        if not blank == "}":
                                                                                            blank = input(" ")
                                                                                            if not blank == "}":
                                                                                                blank = input(" ")
                                                                                                if not blank == "}":
                                                                                                    blank = input(" ")
                                                                                                    if not blank == "}":
                                                                                                        blank = input(
                                                                                                            " ")
                                                                                                        if not blank == "}":
                                                                                                            blank = input(
                                                                                                                " ")
                                                                                                            if not blank == "}":
                                                                                                                blank = input(
                                                                                                                    " ")
                                                                                                                if not blank == "}":
                                                                                                                    blank = input(
                                                                                                                        " ")
                                                                                                                    if not blank == "}":
                                                                                                                        blank = input(
                                                                                                                            " ")
                                                                                                                        if not blank == "}":
                                                                                                                            blank = input(
                                                                                                                                " ")
    #this is possibily the worst way and most inaccurate way to do this shit but here i am :)
    a = 'cmt\": \"'
    lct_start = debug_info_start.split(a, 1)
    if len(lct_start) > 0:
        lct_start = lct_start[1]
    lct_end = debug_info_end.split(a, 1)
    if len(lct_end) > 0:
        lct_end = lct_end[1]
    a = '\",'
    lct_start = lct_start.split(a, 1)[0]
    lct_end = lct_end.split(a, 1)[0]
    time = (decimal.Decimal(lct_end) - decimal.Decimal(lct_start)) + decimal.Decimal(time)
#formats the time
time = str(time)
time = time.split(".", 1)
if len(time) > 0:
    seconds = time[0]
    milliseconds = time[1]
    milliseconds = str(milliseconds)
    seconds = int(seconds)
def seconds_to_time(seconds):
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
            return (f"0{seconds}.{milliseconds}")
        else:
            return (f"{seconds}.{milliseconds}")
    elif hours == "0":
        return (f"{minutes}:{seconds}.{milliseconds}")
    else:
        return (f"{hours}:{minutes}:{seconds}.{milliseconds}")
formatted_time = seconds_to_time(seconds)
#prints the time
message = Prompt.ask("How would you like the output to be formatted?", choices=["Mod Note", "Just Time", "Both"])
if message == "Mod Note":
    print("Mod Note: Retimed to", formatted_time, "using PyTime")
elif message == "Just Time":
    print("Your final time is:", formatted_time)
elif message == "Both":
    print("Mod Note: Retimed to", formatted_time, "using PyTime")
    print("Your final time is:", formatted_time)
#prompts the user to close the program
close = Prompt.ask("Would you like to close the program?", choices=["Yes"])