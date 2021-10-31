import random
for x in range(1):
    number = random.randint(1,201)
guess_number = input("Guess a number:")
val = int(guess_number)
if (number - val > 10 and number - val > 0) or (val - number > 10 and val - number > 0):
    print(number)
    print("try again, you are far")
elif(val- number < 10 and val - number > 0) or (number - val < 10 and val - number > 0):
    print(number)
    print("you are near")
else:
    print(number)
    print("you got it right")

