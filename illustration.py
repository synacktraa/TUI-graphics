from weirdshit import weirdShit, weird_print, cdict, os
import threading, random
from time import sleep
from sys import argv

os.system("")

def data_generate(data):

    """
        This is just an example file for illustration and showcasing
    """

    file_list = ["joemama", "steal_your_momma", "sinister", "heheboi", "whyareyougay", "spaghetti"]
    ext_list = ["png", "jpg", "mp4", "mov"]
    

    for file in file_list:
        ext = random.choice(ext_list)
        weird_print(f"[+] Attaching {file}.{ext}{' '*len(data)}", cdict['LIGHTBLACK_EX'])
        sleep(0.8)

def main(data, sdl, thrust):

    thread2 = threading.Thread(target=weirdShit, args=(data, sdl, thrust))
    thread1 = threading.Thread(target=data_generate, args=(data,))

    threads =[thread1, thread2]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main(argv[1], int(argv[2]), int(argv[3]))