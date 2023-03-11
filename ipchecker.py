import socket
from tkinter import messagebox
import time as t

wt = t.sleep(3)


##main
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    messagebox.showinfo('IP CHECKER', message=f'''your IP: {s.getsockname()}''')
    print(f'''your IP: {s.getsockname()}''')
    wt
def login():
    rs = '31223'
    print('введите код')
    code = input('код:')
    if code == rs:
        print('вы успешно вошли в систему!')
        rootopen = open('root.png', 'w')
        ro = rootopen
        ro.write(code)
        wt
    else:
        print('код не верный!')
        wt


##root

wt = t.sleep(3)
rs = '31223'

rootopen = open("root.png", 'r')

if rootopen.read() == rs:
    rootopen.close()
    main()
else:
    print('вы не вошли в систему!')
    print('хотите войти? y/n')
    if input('y/n:') == 'y':
        login()
        



