import random
from time import sleep
sekvens = []
for i in range(3):
    sekvens.append(random.randint(1, 9))
start = input("Vill du spela? j/n: ")
seconds = int("5")

if start == "j":
    print(sekvens)
    if seconds > 0:
        while seconds > 0:
            sleep(1)
            seconds = seconds - 1 
else: 
    print("Kom tillbaka senare!")