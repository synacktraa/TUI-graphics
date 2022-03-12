from weirdshit import graphic_gen, print_fcw
import threading, random
from time import sleep
from sys import argv
from colorext import fore

def data_generator(data):

    """
        This is just an exemplar script for illustration and showcasing
    """

    file_list = ["mom_spaghetti", "sinister", "static", "venom", "deadpool"]
    ext_list = ["js", "go", "c", "asm"]
    

    for file in file_list:
        ext = random.choice(ext_list)
        print_fcw(f"[+] Attaching {file}.{ext}{' '*len(data)}", fore.LIGHTBLACK_EX)
        sleep(0.8)

def main(data, sdl, thrust):

    thread2 = threading.Thread(target=graphic_gen, args=(data, sdl, thrust))
    thread1 = threading.Thread(target=data_generator, args=(data,))

    threads =[thread1, thread2]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main(argv[1], int(argv[2]), int(argv[3]))