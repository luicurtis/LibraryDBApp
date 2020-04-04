import sys
import sqlite3
conn = sqlite3.connect('library.db')
#from src.itemActions import searchByTitle,
from eventActions import FindanEvent, RegForEvent
#from src.libraryActions import

print("Hello, Welcome to the library!\nPlease Select one of the following options by typing the associated number.\n")

done = '0'

while (done != '1'):

    print("Choose from the following: \n 1. Search \n 2. Borrow \n 3. Return \n 4. Donate an item \n 5. Find an Event \n 6. Register for an Event \n 7. Volunteer \n 8. Ask for help\n 9. Exit\n")
    choice = input("Please enter your decision: ")

    if (choice == '9'):
        done = '1'

    elif (choice == '5'):
        FindanEvent()

    elif (choice == '6'):
        RegForEvent()

    elif (choice == '4'):
        DonateItem()


    else:
        print("Please input a valid choice, Please try again \n")



##Loop has ended
print("Thank you for coming! See you soon.")
if conn:
    conn.close()
    print("Closed database successfully")
