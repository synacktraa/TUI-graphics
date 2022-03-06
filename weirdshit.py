import time
from sys import stdout
from colorama import Fore, Style

def weird_stdout(data, color=Fore.LIGHTWHITE_EX):

    stdout.write(f"{color}{data}{Style.RESET_ALL}")

def get_cavity(data_len):
    
    spaces = str().expandtabs(8)

    while data_len:
        if(data_len<8):
            spaces += '\t'
            for _ in range(8-data_len):
                spaces += '\b'
            data_len = 0
        else:
            spaces += '\t'
            data_len -= 8
    return spaces
    
def weirdShit(): 

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
                  
    spinner = spinning_cursor()

    data = "[+] your message"
    upperstr = data.upper()

    for _ in range(3):
        for x in range(len(data)):
            s = '\r' + data[0:x] + upperstr[x] + data[x+1:] + '\r'
            weird_stdout(s, Fore.GREEN)
            weird_stdout(f"{get_cavity(len(data))}...")
            weird_stdout(next(spinner)) 
            weird_stdout("\r")
            stdout.flush()
            time.sleep(0.1/0.8)

if __name__ == '__main__':
    weirdShit()