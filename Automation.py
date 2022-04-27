"""
Run This Code Snippet In The Terminal:-
    pythonw.exe automation.py
"""
"""
    Change The app_icon in every notifications.
"""
'''
    This program will do the automated task predefined in the program.
    The Task Are Sending Reminders About Homework Or Reminders Of
        Drinking Water, Going Outside To Play, Sleep etc.
    It will also remind you about tomorrow's school and to pack your bags.
'''

# import module
import time
from plyer import notification
import schedule

# Print Some Text
print()
print("-------------------------Reminder App-------------------------")
print("Notifying..")
print("Please Wait For Some Time..")
print()

# Creating Functions
def notifyAboutHomeWork():
    notification.notify(
        title = "Time To Homework!",
        message = "Doing Homework is a good exercise for your mind. So, Do HOMEWORK!!",
        app_icon = "B:\Bhavya\Automation\images\homework.ico",
        timeout = 5,
    )
    print("Do Your Homework!")
    print()

def notifyToDrinkWater():
    notification.notify(
        title = "Time To Drink Water!",
        message = "Drinking Water makes you fit & is a beneficial thing for your body!! So, Drink WATER!!",
        app_icon = "B:\Bhavya\Automation\images\water.ico",
        timeout = 5,
    )
    print("Drink Water!")
    print()

def notifyToPlay():
    notification.notify(
        title = "Time To Play!",
        message = "Playing outside is a good exercise for our physical body. "
                  "It keeps your mind and body healthy. So, PLAY OUTSIDE!!",
        app_icon = "B:\Bhavya\Automation\images\play.ico",
        timeout = 5,
    )
    print("Go Outside To Play!")
    print()

def notifyToPackBag():
    notification.notify(
        title = "Time To Pack Your Bag!",
        message = "Packing your Bag daily reduces your bag weight making it easiar to carry. "
                  "So, PACK YOUR BAG!!",
        app_icon = "B:\Bhavya\Automation\images\packBag.ico",
        timeout = 5,
    )
    print("Pack Your Bag!")
    print()

def notifyToSleep():
    notification.notify(
        title = "Time To Sleep!",
        message = "Sleeping makes you feel relaxed and also removes all your stress throughout the day. "
                  "So, GO TO BED!!",
        app_icon = "B:\Bhavya\Automation\images\sleep.ico",
        timeout = 5,
    )
    print("Time To Sleep!")
    print()

# Creating Main Funcion
def main():
    # Notifying To Drink Water
    schedule.every(90).minutes.do(notifyToDrinkWater)

    # Notifying About Doing Homework
    schedule.every().day.at("15:00").do(notifyAboutHomeWork)
    schedule.every().day.at("16:30").do(notifyAboutHomeWork)
    schedule.every().day.at("19:00").do(notifyAboutHomeWork)

    # Notifying To Going Outside For Playing
    schedule.every().day.at("17:00").do(notifyToPlay)
    schedule.every().day.at("17:30").do(notifyToPlay)
    schedule.every().day.at("18:00").do(notifyToPlay)

    # Notifying To Pack Your Bags
    schedule.every().day.at("19:00").do(notifyToPackBag)
    schedule.every().day.at("19:30").do(notifyToPackBag)

    # Notifying To Go To Bed
    schedule.every().day.at("21:45").do(notifyToSleep)
    schedule.every().day.at("22:15").do(notifyToSleep)
    schedule.every().day.at("22:30").do(notifyToSleep)

    while True:
        schedule.run_pending()
        time.sleep(10)

main()
