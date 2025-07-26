import time

def countdown_timer(t:int):
    
    countdown_time = int(t)

    while countdown_time:
        mins, secs = divmod(countdown_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countdown_time -= 1

    print("Time's up!")

def main():
    t = input("Enter time in seconds: ")
    countdown_timer(t)

if __name__ == "__main__":
    main()
