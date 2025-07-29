import random

def rock_paper_scissor():
    choices:list = ["rock","paper","scissor"]
    comp_choice = random.choice(choices)
    print("I choose",comp_choice)
    
    while True:
        try:
            num = int(input(f"""Choose any one number from following:
                                1.
                                2.
                                3."""))
            break
        except ValueError:
            print("Invalid input....")

    if num in [1, 2, 3]:
        user_choice = random.choice(choices)
        print("You have chosen",user_choice)
        if user_choice == comp_choice:
            print("It's a tie!")
        elif user_choice == choices[1] and comp_choice == choices[0]:
            print("Congratulations! You win...")
        elif user_choice == choices[0] and comp_choice == choices[1]:
            print("Oops! You loose...")
        elif user_choice == choices[2] and comp_choice == choices[1]:
            print("Congratulations! You win...")  
        elif user_choice == choices[1] and comp_choice == choices[2]:
            print("Oops! You loose...")
        elif user_choice == choices[0] and comp_choice == choices[2]:
            print("Congratulations! You win...")  
        elif user_choice == choices[2] and comp_choice == choices[0]:
            print("Oops! You loose...")
    else:
        print("You have entered invalid number!")

def main():
    rock_paper_scissor()

if __name__ == "__main__":
    main()
    


    
        