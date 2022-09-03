import decimal, json, pyperclip, pyautogui
end_check = True
debug_info_start = ""
debug_info_end = ""
time = 0.0
exist = False
segment = int(pyautogui.prompt("How many Segments are there in the Video?", title="PyTime"))
for _ in range(segment):
    debug_info_start = pyautogui.prompt("\n(Debug Info) What is the Starting Frame", title="PyTime")
    debug_info_end = pyautogui.prompt("\n(Debug Info) What is the Ending Frame", title="PyTime")
    #Atleast JSON parsing is here now
    debug_info_start_dict = json.loads(debug_info_start)
    debug_info_end_dict = json.loads(debug_info_end)
    cmt_start = debug_info_start_dict['cmt']
    cmt_end = debug_info_end_dict['cmt']
    #todo Make this shit accurate :)
    time = (decimal.Decimal(cmt_end) - decimal.Decimal(cmt_start)) + decimal.Decimal(time)
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
pyperclip.copy(f"Mod Note: Retimed to [b]{formatted_time}[/b] using [url=https://github.com/ConnerConnerConner/PyTime]PyTime[/url]")
pyautogui.alert(f"Final Time: {formatted_time} \nMod Note copied to Clipboard", title="PyTime")