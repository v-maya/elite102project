# Testing of MySQL and experimenting, not yet adapted to needs

import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="h3110$iMn",
    database="testdatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("JOEY", datetime.now(), "F"))

#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

mycursor.execute("ALTER TABLE Test CHANGE first_name first_name VARCHAR(4)")

mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)