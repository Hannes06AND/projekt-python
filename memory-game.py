import random
import os
from time import sleep

text1 = ""
for i in range(3):
    text1 += str(random.randint(1, 9))

text2 = ""
for i in range(4):
    text2 += str(random.randint(1, 9))

text3 = ""
for i in range(5):
    text3 += str(random.randint(1, 9))

text4 = ""
for i in range(6):
    text4 += str(random.randint(1, 9))

text5 = ""
for i in range(7):
    text5 += str(random.randint(1, 9))

seconds = int("5")
start = input("Vill du spela? j/n: ")

if start == "j":
    print(text1)

    while seconds > 0:
            sleep(1)
            seconds = seconds - 1
    os.system('cls') 
    fraga1 = input("Vilka siffror såg du? ")
    seconds = int("5")
    if fraga1 == text1:
        print("Grattis du svarade rätt!")
        level2 = input("Vill du fortsätta? j/n: ")
        if level2 == "j":
                print(text2)
                while seconds > 0:
                    sleep(1)
                    seconds = seconds - 1
        else: 
            print("Bra kämpat!")
        os.system('cls') 
        fraga2 = input("Vilka siffror såg du? ")
        seconds = int("5")
        if fraga2 == text2:
            print("Grattis du svarade rätt!")
            level3 = input("Vill du fortsätta? j/n: ")
            if level3 == "j":
                print(text3)
                while seconds > 0:
                    sleep(1)
                    seconds = seconds - 1
            os.system('cls')
            fraga3 = input("Vilka siffror såg du? ")
            seconds = int("5")
            if fraga3 == text3:
                print("Grattis du svarade rätt!")
                level4 = input("Vill du fortsätta? j/n: ")
                if level4 == "j":
                    print(text4)
                    while seconds > 0:
                        sleep(1)
                        seconds = seconds - 1
                os.system('cls')
                fraga4 = input("Vilka siffror såg du? ")
                seconds = int("5")
                if fraga4 == text4:
                    print("Grattis du svarade rätt!")
                    level5 = input("Vill du fortsätta? j/n: ")
                    if level5 == "j":
                        print(text5)
                        while seconds > 0:
                            sleep(1)
                            seconds = seconds - 1
                    os.system('cls')
                    fraga5 = input("Vilka siffror såg du? ")
                    seconds = int("5")
                    if fraga5 == text5:
                        print("Grattis du svarade rätt!")
                        print("Du klarade ut spelet!")
            else:
                print("Bra kämpat!")
        else:
            print("Fel svar! Börja om från början.")
    else:
        print("Fel svar! Börja om från början.")
else: 
    print("Kom tillbaka senare!")