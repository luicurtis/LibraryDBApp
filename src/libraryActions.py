# 4. Donate, 7. Volunteer 8. ask for help???
import sqlite3
conn = sqlite3.connect('library.db')

def DonateItem():
    conn.execute('pragma foreign_keys=ON')
    donating = '0'

    while (donating != '1'):
            print("1. Donate an Item\n2. Go back")
            UserDecision = input("Enter Decision: ")

            if (UserDecision == '1'):
                with conn:
                    UItemName = input("Please enter the name of your item: ")
                    Utype = input("Please enter the type of the item (ex. Videogame, Book): ")

                    with conn:
                        cur = conn.cursor()
                        try:
                            cur.execute("""
                                INSERT INTO FutureItems(ItemName, Type)
                                VALUES (?,?)
                                """, (UItemName, Utype))
                            conn.commit()

                        except sqlite3.IntegrityError:
                            print("ERROR: There was a problem Donating such item!\n")
                            return
                        except sqlite3.Error:
                            print("ERROR: There was a problem Donating such item!\n")
                            return

                        print('\n')
                        print ( '##############Item Donated Successfully##############' )
                        print('\n')

            elif (UserDecision == '2'):
                donating = 1
                return

            else:
                print("Please enter a valid choice, Please try again! \n")

    return None

def Volunteer():
    conn.execute('pragma foreign_keys=ON')
    Volunteering = '0'
    while (Volunteering != '1'):

        print("1. Volunteer\n2. Go back")
        UserDecision = input("Enter Decision: ")

        if (UserDecision == '1'):
            with conn:
                UserCardNumber = input("Please enter your Library Card Number: ")
                UFirstname = input("Please enter your First Name: ")
                ULastname = input("Please enter your Last Name: ")
                cur = conn.cursor()
                myQuery = "Update LibraryMembers Set Volunteer=TRUE WHERE CardNumber=:Blank AND FirstName=:Blank1 AND LastName=:Blank2"

                try:
                    cur.execute(myQuery,{"Blank" : UserCardNumber, "Blank1" : UFirstname, "Blank2" : ULastname})
                    conn.commit()

                except sqlite3.IntegrityError:
                    print("ERROR: There was a problem, please check the Library CardNumber, First Name, LastName!\n")

                except sqlite3.IntegrityError:
                    print("ERROR: There was a problem, please check the Library CardNumber, First Name, LastName!\n")


                if (cur.rowcount >= 1):
                    print(cur.rowcount, "record(s) affected")
                    print("Volunteer Status is set to True, you will be contacted with further information regarding your hours and task.\n")
                    print("Thank you for Volunteering!\n")

                else:
                    print("Failed to set status to Volunteer, check CardNumber/FirstName/LastName!\n")

        elif (UserDecision == '2'):
            Volunteering = 1
            return

        else:
            print("Please enter a valid choice, Please try again! \n")

    return None

def LibrarianHelp():
    conn.execute('pragma foreign_keys=ON')
    print("1. Library Tech Support Contact\n2. Library Hours\n3. Go back")
    help = '0'

    while (help != '1'):

        UserDecision = input("Enter Decision: ")

        if (UserDecision == '3'):
            help = 1
            return

        elif (UserDecision == '2'):
            print("Mon-Fri 7:00am - 7:00pm || Sat 9:00am - 6:00pm || Sun 9:00am - 3:00pm\n")

        elif (UserDecision == '1'):
            print("TechSupport@Library.com or 604-354-3544 during Library Hours\n")

        else:
            print("Not a valid choice, please try again!\n")

    return None
