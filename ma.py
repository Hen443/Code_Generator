import random
from pynput.keyboard import Key, Controller

keyboard = Controller()


numeric = int(input("Gago "))
i = 1
q = 0

if numeric != 0000:

    while i == 1 :
        num = random.randrange(1, 10**4)
        numer = '{:04}'.format(num)
        numer = str(num).zfill(4)
        print(numer)

        q += 1

        if int(numer) == numeric:
            print("Your Result Is " + str(numer))
            break
else:
    q = 1
    numer = '{:04}'.format(numeric)
    print(str(numer))
        

print("Time " + str(q))

inputi = input()
if inputi == "":
    exit()