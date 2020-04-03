# 5.Find Event, 6. Register for an Event
import sqlite3
conn = sqlite3.connect('library.db')

def FindanEvent():
    UserEventName = input("Enter the Event's name (If you would like to go back Enter 'X'): ")

    if (UserEventName = 'X')
        

    with conn:
        cur = conn.cursor()
        myQuery = "SELECT * FROM LibraryEvents WHERE EventName=:Blank"

        cur.execute(myQuery,{"Blank" : UserEventName})

        row = cur.fetchone()
        if row:
            print("We do have the following Event occuring called, " + UserEventName + ": ")
        else:
            print("Unfortunately, we do not have any Events called " + UserEventName + "!\n")

        print(row)
