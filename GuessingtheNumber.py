import random
number=random.randrange(1,10)
chances=0
guess=int(input("Guess a number between 1 and 9 ="))

while chances<5 :
    for i in guess:
      chances=chances+1
    if guess!=number:
        if guess< number:
            print("You need to guess Higher.")
            guess=int(input("Guess a number between 1 and 9"))
            print("Chances Remaing:",chances)
        else:
            print("You need to guess Lower.")
            guess=int(input("Guess a number between 1 and 9"))
            print("Chances Remaing:",chances)
            
if guess==number & chances<5 :
    print("Congratulation YOU WON!!!")

if chances>5 | chances==5:
    print("You LOSE!!! The Number is",number)

