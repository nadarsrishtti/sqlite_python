import sqlite3
import mvidatabase

#Query the DB and return all records
def show_all():
    #connect to databasee
    conn = sqlite3.connect('movie.db')
    #create a cursor
    c = conn.cursor()


    #Query The Database
    c.execute("SELECT rowid, * FROM movies")
    #c.execute("SELECT rowid, * FROM movies WHERE name = 'LaLaLand'")
    items = c.fetchall()

    for item in items:
       print(item)
    #comit our command
    conn.commit()

    #close our connection
    conn.close()


#fucntion to add rows in the table
#def add_one(name,act,acrt,dir,yor):
 #  conn = sqlite3.connect('movie.db')
 #  c = conn.cursor()
 #  c.execute("INSERT INTO movies VALUES (?,?,?,?,?)",(name,act,acrt,dir,yor))
 #  conn.commit()
 #  conn.close()


def filter():
   conn = sqlite3.connect('movie.db')
   c = conn.cursor()
   c.execute("SELECT * FROM movies WHERE name = 'LaLaLand'")
   conn.commit()
   conn.close()