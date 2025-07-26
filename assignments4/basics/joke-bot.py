def main():
    user_input = input("We can make you smile by telling joke. For that you need to type 'Joke': ")
    if user_input == "Joke" or user_input == "joke" or user_input == "JOKE":
        print("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
    else:
        print("Sorry I only tell jokes.")

if __name__ == '__main__':
    main()