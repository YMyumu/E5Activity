import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time remaining: {seconds//60} minutes {seconds%60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time is up! Good job focusing.")
