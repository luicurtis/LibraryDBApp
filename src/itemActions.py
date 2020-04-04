import sqlite3
conn = sqlite3.connect('library.db')

# Search for a book in the library
def searchBook():
    queryDict = {}
    queryDict["type"] = "Book"
    print("Choose from the following: \n 1. Search by title \n 2. Search by ISBN \n 3. Search by genre")
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
    # Search by genre
    elif (choice == '3'):
        genre = input("Input the genre: ")
        queryDict["Genre"] = str(genre)
        myQuery = "SELECT * FROM Publications WHERE Type=:type AND Genre=:genre"
    else:
        print("ERROR: input " + choice + " is not a possbile input. Please try again.")
        return

    with conn:
        cur = conn.cursor()
        cur.execute(myQuery, queryDict)

        rows=cur.fetchall()
        i = 1

        if rows:
            print("Here are the following search results: ")
            for row in rows:
                #AssetTag, Status, ShelfNumber, ISBN, Title, Genre, Author, Subject, Edition, Type, ContentRating, Publisher, DateOfPublication
                print("Result #" + str(i) + ":")
                print("    Asset Tag: " + str(row[0]))
                print("    Status: " + row[1])
                print("    Shelf Number: " + str(row[2]))
                print("    ISBN: " + row[3])
                print("    Title" + row[4])
                print("    Genre: " + row[5])
                print("    Author: " + row[6])
                print("\n")
                i += 1
            print("\n")
        else:
            print("Unfortunately, we do not have any books that fill those search requirements. Please try again.\n")

    return 

def searchMagazine(ISBN, title, genre, publisher, contentRating):

    return

def searchDVD(title, yearReleased, genre):

    return

def searchCD(title, genre, artist):

    return

def searchRecord(title, genre, artist):

    return

def searchVideogames(title, yearReleased, genre):

    return

def borrowItem(assetTag, cardNumber):

    return

def returnItem(assetTag, cardNumber):

    return


