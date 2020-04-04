# 5.Find Event, 6. Register for an Event
import sqlite3
conn = sqlite3.connect('library.db')

def FindanEvent():
    EventSearch = '0'

    while (EventSearch != '1'):
        print("1. Search 'EventName' Information\n2. List all Event Names\n3. Go back")
        UserDecision = input("Enter Decision: ")

        if (UserDecision == '3'):
            EventSearch = '1'
            break

        elif (UserDecision == '2'):
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM LibraryEvents")
                rows = cur.fetchall()
                for row in rows:
                    print("\n")
                    print(row[0])
                print("\n")
        elif (UserDecision == '1'):
            UserEventName = input("Enter the Event's name: ")
            with conn:
                cur = conn.cursor()
                myQuery = "SELECT * FROM LibraryEvents WHERE EventName=:Blank"

                cur.execute(myQuery,{"Blank" : UserEventName})

                row = cur.fetchone()
                if row:
                    print("We do have the following Event occuring called, " + UserEventName + ": ")
                    print(row[0])
                    print("Date: ")
                    print(row[1])
                    print("Fee: ")
                    print(row[2])
                    print("Location: ")
                    print(row[3])
                    print("\n")
                else:
                    print("Unfortunately, we do not have any Events called " + UserEventName + "!\n")
        else:
            print("Not a Valid Choice, Please Try Again.")

    return None

def RegForEvent():
    Registration = '0'

    while(Registration != '1'):
        print("1. Register for an Event\n2. Go back")
        UserDecision = input("Enter Decision: ")

        if (UserDecision == '2'):
            EventSearch = '1'
            break

        elif (UserDecision == '1'):
            EventName = input("Please enter the Event Name: ")
            EventDate = input("Please enter the Event Date (Format: '0000-00-00'): ")
            UserCardNumber = input("Please enter your Library Card Number: ")
            UFirstname = input("Please enter your First Name: ")
            ULastname = input("Please enter your Last Name: ")
            with conn:
                cur = conn.cursor()

                try:
                    cur.execute("""
                        INSERT INTO Attending(EventName, DateOfEvent, CardNumber, FirstName, LastName)
                        VALUES (?,?,?,?,?)
                        """, (EventName, EventDate, UserCardNumber,UFirstname, ULastname))

                except sqlite3.IntegrityError:
                    print("ERROR: There was a problem registering!\n")
                    break

                conn.commit()
                print('\n')
                print ( '##############Registered successfully##############' )
                print('\n')

        else:
            print("Not a Valid Choice, Please Try Again.")

    return None
