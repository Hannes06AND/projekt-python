'''import random
import os
from time import sleep

# börja tal med 3 siffror
# visa
# vänta 5 sec
# ta bort
# mata in gissning
# om rätt fortsätt, men en extra siffra i tal
# om fel slut eller börja om

def randomnum(x):
    for i in range(x):
        text += str(random.randint(1, 9))
        return text
    
antal_siffror = 3
svarat_rätt = True

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
                        print("Så nära! Du kom till sista nivån!")
            else:
                print("Bra kämpat!")
        else:
            print("Fel svar! Börja om från början.")
    else:
        print("Fel svar! Börja om från början.")
else: 
    print("Kom tillbaka senare!")'''

import random
import os
from time import sleep

def clear_console():
    """Rensar terminalen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_numbers(length):
    """Genererar en sträng med slumpmässiga siffror."""
    return ''.join(str(random.randint(1, 9)) for _ in range(length))

def memory_game():
    """Huvudfunktionen för memory-spelet."""
    level = 1  # Startnivå
    max_level = 5  # Antal nivåer
    play = input("Vill du spela? j/n: ")

    if play.lower() != 'j':
        print("Kom tillbaka senare!")
        return

    while level <= max_level:
        # Generera en sekvens baserat på nivån
        sequence = generate_numbers(level + 2)
        print(f"Nivå {level}: Memorera följande siffror:")
        print(sequence)
        
        # Vänta i 5 sekunder och rensa sedan terminalen
        sleep(5)
        clear_console()

        # Fråga spelaren vad siffrorna var
        guess = input("Vilka siffror såg du? ")

        # Kontrollera om svaret är rätt
        if guess == sequence:
            print("Grattis, du svarade rätt!")
            level += 1  # Gå vidare till nästa nivå
            if level <= max_level:
                continue_playing = input("Vill du fortsätta? j/n: ")
                if continue_playing.lower() != 'j':
                    print("Bra kämpat!")
                    break
        else:
            print("Fel svar! Du kom till nivå", level)
            break
    else:
        print("Grattis! Du klarade alla nivåer!")

# Starta spelet
memory_game()
