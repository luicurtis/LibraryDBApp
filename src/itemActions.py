import sqlite3
conn = sqlite3.connect('library.db')

# Search for a book in the library
def searchBook(ISBN, title, genre, publisher):
    with conn:

        cur = conn.cursor()

        myQuery = "SELECT * FROM albums NATURAL JOIN artists WHERE Name=:myArtist"

        cur.execute(myQuery,{"myArtist":myFavArtist})

        #rows=cur.fetchall()
        rows = cur.fetchone()
        if rows:
            print("We do have the following albums from your favorite artist, " + myFavArtist + ": ")
        else:
            print("Unfortunately, we do not have any albums by " + myFavArtist + "!\n")

        for row in rows:
            print(row[1])
        print("\n")

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


