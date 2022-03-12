from types import SimpleNamespace
from os import system

"""
🥴 Ansi codes weren't working in linux terminal, after using os.system("") it works like a charm 🥴
"""
system("")

fore_cdict = {
    
    "BLACK":'\u001b[30m',
    "RED":'\u001b[31m',	
    "GREEN":'\u001b[32m',	
    "YELLOW":'\u001b[33m',
    "BLUE":'\u001b[34m',
    "MAGENTA":'\u001b[35m',	
    "CYAN":'\u001b[36m',	
    "WHITE":'\u001b[37m',
    "LIGHTBLACK_EX":'\u001b[30;1m',
    "LIGHTRED_EX":'\u001b[31;1m',
    "LIGHTGREEN_EX":'\u001b[32;1m',
    "LIGHTYELLOW_EX":'\u001b[33;1m',
    "LIGHTBLUE_EX":'\u001b[34;1m',
    "LIGHTMAGENTA_EX":'\u001b[35;1m',
    "LIGHTCYAN_EX":'\u001b[36;1m',
    "LIGHTWHITE_EX":'\u001b[37;1m'
}

back_cdict = {
    
    "BLACK":'\u001b[40m',
    "RED":'\u001b[41m',	
    "GREEN":'\u001b[42m',	
    "YELLOW":'\u001b[43m',
    "BLUE":'\u001b[44m',
    "MAGENTA":'\u001b[45m',	
    "CYAN":'\u001b[46m',	
    "WHITE":'\u001b[47m',
    "LIGHTBLACK_EX":'\u001b[40;1m',
    "LIGHTRED_EX":'\u001b[41;1m',
    "LIGHTGREEN_EX":'\u001b[42;1m',
    "LIGHTYELLOW_EX":'\u001b[43;1m',
    "LIGHTBLUE_EX":'\u001b[44;1m',
    "LIGHTMAGENTA_EX":'\u001b[45;1m',
    "LIGHTCYAN_EX":'\u001b[46;1m',
    "LIGHTWHITE_EX":'\u001b[47;1m'
}

RESET = '\u001b[0m'


fore = SimpleNamespace(**fore_cdict)
back = SimpleNamespace(**back_cdict)