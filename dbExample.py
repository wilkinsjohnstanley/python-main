import sqlite3

def main():
    #connect to the database

    conn = sqlite3.connect('inventory.db')
    