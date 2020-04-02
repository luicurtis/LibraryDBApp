#1. Search \n 2. Borrow \n 3. Return 

import sqlite3
conn = sqlite3.connect('library.db')

def searchByTitle (title):
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