import sqlite3
conn = sqlite3.connect('library.db')
from src.itemActions import searchByTitle, 
from src.eventActions import 
from src.libraryActions import 

print("Hello welcome to the library!!!!!!")
choice = input("Choose from the following: \n 1. Search \n 2. Borrow \n 3. Return \n 4. Donate \n 5.Find Event \n 6. ... ")

searchByTitle()