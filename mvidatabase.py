import sqlite3

#connect to databasee
conn = sqlite3.connect('movie.db')

#create a cursor
c = conn.cursor()


#create a table
#c.execute("""CREATE TABLE movies (
 #   name text,
 #   actor text,
 #   actress text,
 #   director text,
 #   y_o_r text
#)""")
#print("The Table has created.")


#insert rows in the table
#many_movies =[
 #   ('BeforeSunset','EthanHawke','JulieDelpy','RicharLinklater','2004-06-17'), 
 #   ('TheNotebook','RyanGosling','RachelMcAdams','NickCassavetes','2004-06-25'), 
 #   ('LaLaLand','RyanGosling','EmmaStone','DamienChazelle','2016-11-09'), 
 #   ('TheConjuring','VeraFarmiga','PatrickWilson','JamesWan','2003-08-02'), 
 #   ('SpiritedAway','DaveighChase','MiyuIrino','HayaoMiyazaki','2001-07-20')
 #   ]

#c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", many_movies)
#print("Rows Inserted Successfully!!")


#Query The Database
#c.execute("SELECT rowid, * FROM movies")
#c.execute("SELECT rowid, * FROM movies WHERE name = 'LaLaLand'")

items = c.fetchall()

for item in items:
    print(item)


#comit our command
conn.commit()

#close our connection
conn.close()