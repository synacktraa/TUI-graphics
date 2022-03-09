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
	

def weird_stdout(data, color=cdict['LIGHTWHITE_EX']):

    stdout.write(f"{color}{data}{RESET}")

def weird_print(data, color=cdict['LIGHTWHITE_EX']):

        print(f"{color}{data}{RESET}")    
    

def weirdShit(data_string="[+] loading script", schedule=3, thrust=4): 

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
            weird_stdout(s, cdict['LIGHTGREEN_EX'])
            weird_stdout(f"{indent}...")
            weird_stdout(next(spinner)) 
            weird_stdout("\r")
            stdout.flush()
            time.sleep(0.5/thrust)

