import sqlite3

def main():

    #connect to the database
    conn = sqlite3.connect('inventory.db')

    #get a cursor
    cur = conn.cursor()

    #create inventory table
    #cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL, ItemName TEXT, Price REAL)''')
    
    #add elements to a row in the table called inventory
    # cur.execute('''INSERT INTO Inventory (ItemName, Price) VALUES ("Screwdriver", 4.99)''')
    # cur.execute('''INSERT INTO Inventory (ItemName, Price) VALUES ("Hammer",20.99)''')

    #select table
    cur.execute('SELECT * FROM Inventory')
    results = cur.fetchall()
    print(results)

    for row in results:
        print(f'{row[0]:30} {row[1]:5} {row[2]:5}')

    #commit changes
    conn.commit()

    #close the connectiono
    conn.close()
main()