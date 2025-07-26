def double_the_number(number:int):
    while number <= 100:
        number = number * 2
        print(number)

def main():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            break
        except ValueError:
           print("Please enter a number....")
    double_the_number(user_input)

if __name__ == '__main__':
    main()
