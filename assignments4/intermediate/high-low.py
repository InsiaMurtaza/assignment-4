import random

def get_number():
    score = 0
    for i in range(5):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        print("Round",i + 1)
        print("Your number is",num1)
        ask_user = input("Do you think your number is higher or lower than the computer's: ").lower()
        if ask_user == "higher" and num1 > num2:
            score +=1
            print("You were right! The computer's number was",num2)
            print("Your score is now",score)
        elif ask_user == "lower" and num1 < num2:
            score +=1
            print("You were right! The computer's number was",num2)
            print("Your score is now",score)
        elif ask_user == "higher" and num1 <= num2:
            print("Aww, that's incorrect. The computer's number was",num2)
            print("Your score is still",score)
        elif ask_user == "lower" and num1 >=num2:
            print("Aww, that's incorrect. The computer's number was",num2)
            print("Your score is still",score)
        else:
            print("Invalid input!")

def main():
    get_number()

if __name__ == "__main__":
    main()
