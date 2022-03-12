import time
from sys import stdout
from colorext import fore, RESET


def stdout_fcw(data, color=fore.WHITE): #Just for foreground/text color

    stdout.write(f"{color}{data}{RESET}")

def print_fcw(data, color=fore.WHITE): #Just for foreground/text color

        print(f"{color}{data}{RESET}")    
    

def graphic_gen(data_string="[+] loading script", schedule=3, thrust=4): 

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
                  
    spinner = spinning_cursor()

    data = data_string
    upperstr = data.upper()
    data_len = len(data)

    indent = str().expandtabs(8)

    while data_len:
        if(data_len<8):
            indent += '\t'
            for _ in range(8-data_len):
                indent += '\b'
            data_len = 0
        else:
            indent += '\t'
            data_len -= 8

    for _ in range(schedule):
        
        for x in range(len(data)):

            s = '\r' + data[0:x] + upperstr[x] + data[x+1:] + '\r'
            stdout_fcw(s, fore.LIGHTGREEN_EX)
            stdout_fcw(f"{indent}...")
            stdout_fcw(next(spinner)) 
            stdout_fcw("\r")
            stdout.flush()
            time.sleep(0.5/thrust)

if __name__ == '__main__':
    graphic_gen()