import random
tal1=random.randint(0,100)
tal2=random.randint(0,100)
print("Vad blir",tal1,"*",tal2,"?")

svar=int(input("Svar: "))
if svar==tal1*tal2:
    print("Du ar duktig!!")
else:
    print("Du suger kuk")

