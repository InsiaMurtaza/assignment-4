def get_weight():
    while True:
        try:
            ask_weight = int(input("Enter your weight on Earth: "))
            break
        except ValueError:
            print("Please enter weight in number...")
    

    ask_planet = input("Enter a planet on which you want to convert your weight into: ").lower()

    if ask_planet == "mercury":
        changed_weight = round(ask_weight *(37.6/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "venus":
        changed_weight = round(ask_weight *(88.9/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "mars":
        changed_weight = round(ask_weight *(37.8/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "jupiter":
        changed_weight = round(ask_weight *(236.0/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "saturn":
        changed_weight = round(ask_weight *(108.1/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "uranus":
        changed_weight = round(ask_weight *(81.5/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    elif ask_planet == "neptune":
        changed_weight = round(ask_weight *(114.0/100),2)
        print("Your equivalent weight on",ask_planet,"is",changed_weight)   
    else:
        print("You've not entered a valid planet...")
    
def main():
    get_weight()

if __name__ == "__main__":
    main()
        