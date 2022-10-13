def main():
    from pyfiglet import figlet_format
    from decimal import Decimal as d
    from os import name, system
    import json

    logo = figlet_format('PyTime', font='univers')
    logo = f'\033{logo}\033[00m'

    print(f'{logo}\n\n\n')

    def frame_round(time_pre, framerate):
        return d(round(d(d(time_pre) - d(time_pre) % (d(1) / int(framerate))), 3))

    fps_prompt = '\033[00mWhat is the FPS of the Video? :\033[1;00m'
    while True:
        try:
            fps = int(input(fps_prompt))
        except ValueError:
            fps_prompt = '\033[1;31mPlease Enter a Valid Number :\033[1;00m'
        else:
            break

    def format_time(pre_time):
        pre_time = str(pre_time)
        pre_time = pre_time.split('.', 1)
        seconds = int(pre_time[0])
        milliseconds = str(pre_time[1])
        minutes = seconds // 60
        hours = minutes // 60
        if seconds > 59.999:  # makes sure that the seconds are less than 60
            seconds = seconds - (minutes * 60)
        if minutes > 59.999:  # makes sure that the minutes are less than 60
            minutes = minutes - (hours * 60)
        # Converts Integers to Strings
        # Combines the time into a single string
        if seconds == '0':
            return f'0s {milliseconds}ms'
        elif minutes == '0':
            if len(seconds) == 1:
                return f'0{str(seconds)}s {milliseconds}ms'
            else:
                return f'{str(seconds)}s {milliseconds}ms'
        elif hours == '0':
            return f'{str(minutes)}m {str(seconds)}s {milliseconds}ms'
        else:
            return f'{str(hours)}h {str(minutes)}m {str(seconds)}s {milliseconds}ms'

    def get_time(prompt, framerate):
        while True:
            start_json = ''
            part = input(prompt)
            while True:
                start_json = start_json + part
                part = input('')
                if part == '}':
                    start_json = start_json + part
                    break
            prompt = f'\033[1;31m{prompt}\033[00m'
            try:
                return d(frame_round(json.loads(start_json)['cmt'], framerate))
            except json.decoder.JSONDecodeError:
                print('\033[1;31mError: JSON is Invalid\033[00m')
            except KeyError:
                print('\033[1;31mError: No CMT in Json\033[00m')
            else:
                break

    start_time = get_time('\033[00mWhat is the Starting Frame? :\033[1;00m', fps)

    end_time = get_time('\033[00mWhat is the Ending Frame? :\033[1;00m', fps)

    time = format_time(frame_round(end_time - start_time, fps))

    if name == 'nt':
        system('cls')
    else:
        system('clear')

    print(figlet_format(time, font='big'))

    input('Press \"Enter\" to Exit.')


if __name__ == '__main__':
    main()
else:
    print(f'\033[1;31mError: Please Run as \"__main__\" instead of {__name__}\033[00m')
