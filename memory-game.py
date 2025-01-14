import random
sekvens = []
for i in range(3):
    sekvens.append(random.randint(1, 9))
start = input("Vill du spela? j/n: ")
if start == "j":
    print(sekvens)
else: 
    print("Kom tillbaka senare! ")