import sqlite3
conn = sqlite3.connect('library.db')
from itemActions import searchItem 

searchItem()
