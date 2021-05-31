from random import randint

def numberGame():
  number = randint(1, 100)
  print("I am thinking of a number between 1 and 100")
  guess = int(input("What is your guess? "))
  
  while True:
    if number == guess:
      print("That's the correct number!")
      break
    elif number > guess:
      print("Too low!")
    else:
      print("Too high!")
    guess = int(input("What is your guess? "))

def greet():
  name = input("What is your name? ")
  if name == "Justin":
    print("That's my name too!")
  else:
    print("Hello,", name)

greet()
numberGame()
