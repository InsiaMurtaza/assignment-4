def get_weight():
    while True:
        try:
            ask_user = int(input("Enter your weight on Earth: "))
            break
        except ValueError:
            print("Please enter weight in number...")
    
    mars_weight = ask_user * (37.8/100)

    return round(mars_weight,2)

def main():
    mars_weight = get_weight()
    print("Your equivalent weight on Mars is",mars_weight)

if __name__ == '__main__':
    main()

