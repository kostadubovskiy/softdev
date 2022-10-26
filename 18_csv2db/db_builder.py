#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import os

os.system('rm -rf discobandit.db')
DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()   

filename = 'students.csv'
with open(filename,newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    csv_list = list(reader)
    keys = list((csv_list[0]).keys())


          #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
c.execute(f'''create table students('{str(keys[0])}' text, '{str(keys[1])}' int, {keys[2]} text)''')
for row in csv_list:
    # c.execute(f'''insert into students({row[keys[0]]},{row[keys[1]]},{row[keys[2]]})''')
    c.execute(f'''insert into students values('andrew',199,'9000')''')
    
    
# c.execute('''.import --csv --skip 1 --schema temp /home/students/2023/kdubovskiy30/sd/softdev/18_csv2db/students.csv students''')

command = "select * from students"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


