# import necessary modules for the alarming service
from datetime import datetime
from re import match
from time import sleep
from tkinter import messagebox

# Throws a box at the person
def call_box():
    messagebox.showinfo("Alert", "This is your simple alert.\nWe hope that we helped.")

# Deploys the call_box function after the remaining time
def alert_deploy(remaining_time):
    sleep(remaining_time)
    call_box()

# Checks for the difference in time between the current time and the next timestamp
def time_diff():
    # used to check whether or not the time is in the right format also takes the time
    while True:
        print("Enter the time in the format HH:MM.")
        alert_time = input("> ")
        time_format = '[0-2][0-9]:[0-6][0-9]'
        if match(time_format,alert_time):
            break
        print("Perhaps you made a mistake in the format?")

    # finds out the current time
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')

    #finds the remaining hours and minutes before the alert
    hour_difference = int(alert_time[0:2]) - int(current_datetime.strftime('%H'))
    min_difference = int(alert_time[3:5]) - int(current_datetime.strftime('%M'))
    sec_difference = 60 - int(current_datetime.strftime('%S'))

    time_rem = hour_difference*60*60 + (min_difference-1)*60 + sec_difference
    print(time_rem)
    alert_deploy(time_rem)

if __name__ == "__main__":
    time_diff()