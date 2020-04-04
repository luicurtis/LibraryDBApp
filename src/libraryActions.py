# 4. Donate, 7. Volunteer 8. ask for help???
import sqlite3
conn = sqlite3.connect('library.db')

def DonateItem():
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
                        cur.execute("""
                            INSERT INTO FutureItems(ItemName, Type)
                            VALUES (?,?)
                            """, (UItemName, Utype))
                        conn.commit()
                        print('\n')
                        print ( '##############Item Donated Successfully##############' )
                        print('\n')

            elif (UserDecision == '2'):
                donating = 1
                break

            else:
                print("Please enter a valid choice, Please try again! \n")

    return None

def Volunteer():

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

                cur.execute(myQuery,{"Blank" : UserCardNumber, "Blank1" : UFirstname, "Blank2" : ULastname})

                conn.commit()

                print(cur.rowcount, "record(s) affected")

                print("Volunteer Status is set to True, you will be contacted with further information regarding your hours and task.\n")
                print("Thank you for Volunteering!\n")

        elif (UserDecision == '2'):
            Volunteering = 1
            break

        else:
            print("Please enter a valid choice, Please try again! \n")

    return None
