import time
import threading

class CountdownThread(threading.Thread):
    def __init__(self, t):
        threading.Thread.__init__(self)
        self.t = t
        self.running = True

    def run(self):
        while self.t and self.running:
            mins, secs = divmod(self.t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.t -= 1

        if not self.running:
            print("Countdown stopped.")
        else:
            print("Time's up!")

def countdown(t):
    countdown_thread = CountdownThread(t)
    countdown_thread.start()
    while countdown_thread.is_alive():
        input_str = input("")
        if input_str == "stop":
            countdown_thread.running = False
            countdown_thread.join()
            break

print("Welcome to the Countdown Timer!")
while True:
    try:
        time_input = int(input("Enter the number of seconds to countdown: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    countdown(time_input)
    answer = input("Would you like to restart the timer? (y/n) ")
    if answer.lower() == "y":
        while True:
            try:
                time_input = int(input("Enter the number of seconds to countdown: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif answer.lower() == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
