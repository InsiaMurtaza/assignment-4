import random

def main():
    MIN_VALUE:int = 1
    MAX_VALUE:int = 100
    for i in range(10):
        num = random.randint(MIN_VALUE,MAX_VALUE)
        print(num)

if __name__ == '__main__':
    main()
