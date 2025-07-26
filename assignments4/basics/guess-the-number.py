import random

def guess_number(number:int):
    random_number = random.randint(0,99)
    while True:
     if number == random_number:
         print("Congtrats! You have guessed the right number....")
         break
     elif number < random_number:
         print("Your guess is too low!")
         number = int(input("Enter a new number: "))
     elif number > random_number:
         print("Your guess is too high!")
         number = int(input("Enter a new number: "))

def main():
    while True:
      try:
        user_input = int(input("I m thinking of a number between 0 and 99...Enter a guess: "))
        break
      except ValueError:
        print("Please enter a number...")
    guess_number(user_input)


if __name__ == '__main__':
   main()