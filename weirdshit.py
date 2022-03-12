import time
from sys import stdout
import os

"""
🥴 Ansi codes weren't working in linux terminal, after using os.system("") it works like a charm 🥴
"""
os.system("")


cdict = {
    
    "BLACK":'\u001b[30m',
    "RED":'\u001b[31m',	
    "WHITE":'\u001b[37m',
    "YELLOW":'\u001b[33m',
    "BLUE":'\u001b[34m',
    "GREEN":'\u001b[32m',	
    "MAGENTA":'\u001b[35m',	
    "CYAN":'\u001b[36m',	
    "LIGHTGREEN_EX":'\u001b[32;1m',
    "LIGHTCYAN_EX":'\u001b[36;1m',
    "LIGHTBLUE_EX":'\u001b[34;1m',
    "LIGHTRED_EX":'\u001b[31;1m',
    "LIGHTMAGENTA_EX":'\u001b[35;1m',
    "LIGHTYELLOW_EX":'\u001b[33;1m',
    "LIGHTWHITE_EX":'\u001b[37;1m',
    "LIGHTBLACK_EX":'\u001b[30;1m'
}

RESET = '\u001b[0m'
	

def stdout_cw(data, color=cdict['LIGHTWHITE_EX']):

    stdout.write(f"{color}{data}{RESET}")

def print_cw(data, color=cdict['LIGHTWHITE_EX']):

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
            stdout_cw(s, cdict['LIGHTGREEN_EX'])
            stdout_cw(f"{indent}...")
            stdout_cw(next(spinner)) 
            stdout_cw("\r")
            stdout.flush()
            time.sleep(0.5/thrust)

if __name__ == '__main__':
    graphic_gen()