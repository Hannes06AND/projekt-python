summa = 0
for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        summa = summa + i
print("Summa från 1 till 9:",summa)

summan = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        summan = summan + i
print("Summa från 1 till 999:",summan)