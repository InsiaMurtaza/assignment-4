import random

def main():
    number = int(input("I m thinking of a number between 0 and 99...Enter a guess: "))
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
         
if __name__ == '__main__':
    main()