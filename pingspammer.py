import pyautogui, time, os
user = input("Please put the username of the person you would like to spam. ")
interval = input("How many seconds between each spam would you like? ")
try:
    print("Get ready.")
    time.sleep(5)
    while True:
        time.sleep(int(interval) - 1)
        pyautogui.typewrite("@")
        time.sleep(0)
        pyautogui.typewrite(user)
        pyautogui.press("enter")
        pyautogui.press("enter")
except:
    print("An error has occured.")
