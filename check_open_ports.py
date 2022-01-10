import os


if 'asas.txt.gnmap' in os.listdir():
    if 'ssh_local.txt' in os.listdir(): os.remove('ssh_local.txt')
    file_open = open('asas.txt.gnmap', 'r').readlines()
    result_list = []
    for el in file_open:
        if '#' not in el.rstrip() and 'Status: Up' not in el.rstrip():
            result_list.append(el.rstrip())


    for el in result_list:
        ip = (el.split('Ports: ')[0].replace('()', ''))
        print(ip.split('Host: ')[1].replace('\t', ''))
        ports = (el.split('Ports: ')[1])
        f = open('ssh_local.txt', 'a')
        for i in ports.split(', '):
            if 'open' in i:
                if 'ssh' in str(i):
                    f.write(f"{ip.split('Host: ')[1]}\n")
                print(i)
        print('-------------')