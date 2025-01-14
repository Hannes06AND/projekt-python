import random
import os
from time import sleep
sekvens = []
text1 = ""
for i in range(3):
    text1 += str(random.randint(1, 9))
start = input("Vill du spela? j/n: ")
text2 = ""
for i in range(4):
    text2 += str(random.randint(1, 9))
text3 = ""
for i in range(5):
    text3.append(random.randint(1, 9))
text4 = ""
for i in range(6):
    text4.append(random.randint(1, 9))
text5 = ""
for i in range(7):
    text5.append(random.randint(1, 9))
seconds = int("5")

if start == "j":
    print(text1)

    while seconds > 0:
            sleep(1)
            seconds = seconds - 1

    os.system('cls') 
    fraga1 = input()

else: 
    print("Kom tillbaka senare!")