import os

import pyautogui
from netifaces import interfaces, ifaddresses, AF_INET

my_local_ip = []
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}])]
    my_local_ip.append(addresses[0])

# if we already have these files, then they need to be deleted
if 'targets.txt' in os.listdir(): os.remove('targets.txt')
if 'pingsweep.txt' in os.listdir(): os.remove('pingsweep.txt')
if 'asas.txt.gnmap' in os.listdir(): os.remove('asas.txt.gnmap')

# my local ip
my_local_ip = ('.'.join(my_local_ip[-1].split('.')[:3]))
# open terminal
os.system(f'gnome-terminal')
os.getcwd()
# cd to our directory
pyautogui.typewrite(f"cd {os.getcwd()}")
pyautogui.press('enter')
pyautogui.typewrite('clear')
pyautogui.press('enter')
# make command ping for all pc's
pyautogui.typewrite("for octet in {1..254}; do ping -c 1 " + my_local_ip + ".$octet -W 1 >> pingsweep.txt & done")
pyautogui.press('enter')
pyautogui.typewrite('clear')
pyautogui.press('enter')
# sorted these pc's
pyautogui.typewrite('cat pingsweep.txt |grep "bytes from" |cut -d " " -f4 |cut -d ":" -f1 > targets.txt')
pyautogui.press('enter')
pyautogui.typewrite('clear')
pyautogui.press('enter')
pyautogui.typewrite('nmap -Pn -n -p 22,25,53,80,443,445,1433,3306,3389,5800,5900,8080,8443 -iL targets.txt -oA asas.txt')
pyautogui.press('enter')
document_read_local_ip = open('targets.txt').readlines()
print('IP"s in your local net: \n')
for el in document_read_local_ip:
    print(el.rstrip())

for el in os.listdir():
    if 'asas' in el and el != 'asas.txt.gnmap':
        os.remove(el)