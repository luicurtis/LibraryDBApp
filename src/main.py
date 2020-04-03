import sys
import sqlite3
conn = sqlite3.connect('library.db')
#from src.itemActions import searchByTitle,
from eventActions import FindanEvent
#from src.libraryActions import

print("Hello, Welcome to the library!\n Please Select one of the following options by typing the associated number.\n")
print("Choose from the following: \n 1. Search \n 2. Borrow \n 3. Return \n 4. Donate an item \n 5. Find an Event \n 6. Register for an Event \n 7. Volunteer \n 8. Ask for help\n 9. Exit\n")

choice = input("Please enter your decision: ")
done = '0'
while (done != '1'):

    if (choice == '9'):
        done = '1'

    elif (choice == '5'):
        FindanEvent()

##Loop has ended
print("Thank you for coming! See you soon.")
