import sqlite3 as sq

# Initiate database with a connection
con = sq.connect("barterly.db")

# Initiate cursor for database
cur = con.cursor()

'''Creating Tables'''

# Product table
cur.execute("""
    CREATE TABLE product (
        user TEXT,
        prod TEXT CHECK (length(prod) = 3),
        item TEXT,
        condition INT CHECK (condition >= 0 AND condition <= 10),
        listdate DATE,
        listlocation TEXT
    )
""")

# User table
cur.execute("""
    CREATE TABLE users (
        username TEXT CHECK (length(username) <= 16),
        email TEXT,
        password TEXT,
        name TEXT,
        rating INT CHECK (rating >= 0 AND rating <= 10),
        numtransactions INT,
        mailaddress TEXT,
        location TEXT
    )
""")

# Transactions table
cur.execute("""
    CREATE TABLE transactions (
        prodr TEXT CHECK (length(prodr) = 3),
        prodg TEXT CHECK (length(prodg) = 3),
        itemr TEXT,
        itemg TEXT,
        userr TEXT,
        userg TEXT,
        ratingr INT CHECK (ratingr >= 0 AND ratingr <= 10), 
        ratingg INT CHECK (ratingg >= 0 AND ratingg <= 10),
        transactiondate DATE
    )
""")

con.close()