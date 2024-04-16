import random
from time import sleep
from os import system
num = random.randint(1,100)
answ = 0
answ = int(input("ievada cipars 1 lidz 100:"))
while answ != num:
    if answ < num:
        system("cls")
        print("  __ ")
        print(" / / ")
        print("/ / ")
        print("\ \ ")
        print(" \_\ ")
        answ = int(input("Šaja cipars ir mazaks neka atbilde:"))
    if answ > num:
        system("cls")
        print("__  ")
        print("\ \  ")
        print(" \ \ ")
        print(" / / ")
        print("/_/ ")
        answ = int(input("Šaja cipars ir lielaks neka atbilde:"))
system("cls")
print('  ____                            _         _       _   _                 ')
print(" / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___")
print("| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|")
print("| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ ")
print(" \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/ ")
print("                  |___/                                               ")