import sqlite3
from datetime import datetime
conn = sqlite3.connect('library.db')

# Search for a book in the library
def searchItem():
    queryDict = {}
    itemType = input("What item are you looking for? \n 1. Books \n 2. Magazines \n 3. Scientific Journals \
                    \n 4. DVDs \n 5. CDs \n 6. Records \n 7. Video Games \n")
    # Search for book
    if (itemType == '1'):
        queryDict["type"] = "Book"
        print("Choose from the following: \n 1. Search by title \n 2. Search by ISBN")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND Title=:title"
        # Search by ISBN
        elif (choice == '2'):
            isbn = input("Input the ISBN: ")
            queryDict["ISBN"] = isbn
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND ISBN=:ISBN"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for Magazine
    elif (itemType == '2'):
        queryDict["type"] = "Magazine"
        print("Choose from the following: \n 1. Search by title \n 2. Search by ISBN")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND Title=:title"
        # Search by ISBN
        elif (choice == '2'):
            isbn = input("Input the ISBN: ")
            queryDict["ISBN"] = isbn
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND ISBN=:ISBN"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for Scientific Journals
    elif (itemType == '3'):
        queryDict["type"] = "Scientific Journal"
        print("Choose from the following: \n 1. Search by title \n 2. Search by ISBN")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND Title=:title"
        # Search by ISBN
        elif (choice == '2'):
            isbn = input("Input the ISBN: ")
            queryDict["ISBN"] = isbn
            myQuery = "SELECT * FROM Publications WHERE Type=:type AND ISBN=:ISBN"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for DVD
    elif (itemType == '4'):
        queryDict["type"] = "DVD"
        print("Choose from the following: \n 1. Search by title \n 2. Search by Genre")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Title=:title"
        # Search by Genre
        elif (choice == '2'):
            genre = input("Input the Genre: ")
            queryDict["genre"] = genre
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Genre=:genre"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for CDs
    elif (itemType == '5'):
        queryDict["type"] = "CD"
        print("Choose from the following: \n 1. Search by title \n 2. Search by Artist")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Title=:title"
        # Search by Artist
        elif (choice == '2'):
            artist = input("Input the Artist: ")
            queryDict["artist"] = artist
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Artist=:artist"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for Records 
    elif (itemType == '6'):
        queryDict["type"] = "Record"
        print("Choose from the following: \n 1. Search by title \n 2. Search by Artist")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Title=:title"
        # Search by Artist
        elif (choice == '2'):
            artist = input("Input the Artist: ")
            queryDict["artist"] = artist
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Artist=:artist"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for Record
    elif (itemType == '6'):
        queryDict["type"] = "Record"
        print("Choose from the following: \n 1. Search by title \n 2. Search by Artist")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Title=:title"
        # Search by Artist
        elif (choice == '2'):
            artist = input("Input the Artist: ")
            queryDict["artist"] = artist
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Artist=:artist"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    # Search for video game
    elif (itemType == '7'):
        queryDict["type"] = "VideoGame"
        print("Choose from the following: \n 1. Search by title \n 2. Search by Production Studio")
        choice = input("Please enter your decision: ")
        # Search by title
        if (choice == '1'):
            title = input("Input the title: ")
            queryDict["title"] = title
            myQuery = "SELECT * FROM Media WHERE Type=:type AND Title=:title"
        # Search by Artist
        elif (choice == '2'):
            productionStudio = input("Input the Production Studio Name: ")
            queryDict["productionStudio"] = productionStudio
            myQuery = "SELECT * FROM Media WHERE Type=:type AND ProductionStudio=:productionStudio"
        else:
            print("ERROR: input " + choice + " is not a possbile input. Please try again.")
            return
    else:
        print("ERROR: input " + itemType + " is not a possbile input. Please try again.")
        return

    # Perform query
    with conn:
        cur = conn.cursor()
        cur.execute(myQuery, queryDict)
        rows=cur.fetchall()

        if rows:
            if (int(itemType) >= 1 and int(itemType) <= 3):
                printPublications(rows)
            elif (int(itemType) > 3 and int(itemType) <= 7):
                printMedia(rows)
        else:
            print("Unfortunately, we do not have any books that fill those search requirements. Please try again.\n") 
    return

def printPublications(rows):
    i = 1
    print("Here are the following search results: ")
    for row in rows:
        # Publications(AssetTag, Status, ShelfNumber, ISBN, Title, Genre, Author, Subject, Edition, Type, ContentRating, Publisher, DateOfPublication)
        print("Result #" + str(i) + ":")
        print("    Asset Tag: " + str(row[0]))
        print("    Status: " + row[1])
        print("    Shelf Number: " + str(row[2]))
        print("    ISBN: " + row[3])
        print("    Title: " + row[4])
        print("    Genre: " + row[5])
        print("    Author: " + row[6])
        print("\n")
        i += 1

    print("\n")
    return
    
def printMedia(rows):
    i = 1
    print("Here are the following search results: ")
    for row in rows:
        # Media(AssetTag, Status, ShelfNumber, Title, YearReleased, Genre, ProductionStudio, Artist, Length, NumTracks, Rating, Type)
        print("Result #" + str(i) + ":")
        print("    Asset Tag: " + str(row[0]))
        print("    Status: " + row[1])
        print("    Shelf Number: " + str(row[2]))
        print("    Title: " + row[3])
        print("    Year Released: " + row[4])
        print("    Genre: " + row[5])
        print("    Production Studio: " + row[6])
        print("\n")
        i += 1

    print("\n")
    return

def borrowItem():
    cardNumber = input("What is your library card number?\n")
    assetTag = input("What is the asset tag number of your item?\n")

    with conn:
        cur = conn.cursor()

        myQuery = "INSERT INTO BorrowedBy (AssetTag, CardNumber) VALUES (:assetTag, :cardNumber)"
        try:
            cur.execute(myQuery,{"assetTag":assetTag, "cardNumber":cardNumber})

        except sqlite3.IntegrityError:
            print("ERROR: There was a problem borrwing the book. Please check that you have entered the correct card member or asset tag!\n")
            return     

        if conn:
            conn.commit()
            print("Success! Book borrowed, please return the book within 14 day to avoid a fine.\n")
    return

def returnItem():
    cardNumber = input("What is your library card number?\n")
    assetTag = input("What is the asset tag number of your item?\n")
    todaysDate = datetime.today().strftime('%Y-%m-%d')

    with conn:
        cur = conn.cursor()
        myQuery = "UPDATE  BorrowedBy SET DateReturned=:todaysDate WHERE AssetTag=:assetTag AND CardNumber=:cardNumber"
        try:
            cur.execute(myQuery,{"todaysDate":todaysDate, "assetTag":assetTag, "cardNumber":cardNumber})

        except sqlite3.IntegrityError:
            print("ERROR: There was a problem returning the book. Please check that you have entered the correct card member or asset tag!!!\n")
            return     

    if conn:
            conn.commit()
            print("Success! Book returned.\n")    
    
    return


