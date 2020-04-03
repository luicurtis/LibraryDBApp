import sqlite3
conn = sqlite3.connect('library.db')

# Search for a book in the library
def searchBook(ISBN, title, genre, publisher):
    with conn:
        queryDict = {}
        queryDict["type"] = "Book"

        myQuery = "SELECT * FROM Publications WHERE Type=:type"
        # Concatenate the query based on what info we are given
        if (ISBN != None):
            myQuery += " AND ISBN=:ISBN"
            queryDict["ISBN"] = ISBN
        if (title != None):
            myQuery += " AND Title=:title"
            queryDict["title"] = title
        if (genre != None):
            myQuery += " AND Genre=:genre"
            queryDict["genre"] = genre
        if (publisher != None):
            myQuery += " AND Publisher=:publisher"
            queryDict["publisher"] = publisher

        cur = conn.cursor()

        cur.execute(myQuery,queryDict)

        #rows=cur.fetchall()
        rows = cur.fetchone()
        if rows:
            print("Here are the following search results: ")
            for row in rows:
                print(row[1])
            print("\n")
        else:
            print("Unfortunately, we do not have any books that fill those search requirements. Please try again.\n")
        
        # Not sure if this is needed
        # it might close the connection in the main file?
        if conn:
            conn.close()
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


