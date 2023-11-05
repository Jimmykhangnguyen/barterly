import sqlite3 as sq

# Connect and create cursor for the database
con = sq.connect("barterly.db")
cur = con.cursor()

# User data
udata = [
    ('Thomas1999', 'thomas@gmail.com', 'JHJ3jh3hK2NC', 'Thomas Yonge', 5, 3, 'Y4J T41', 'Toronto'),
    ('Charles1999', 'charles@gmail.com', 'NF3N4h3hK2NC', 'Charles Olde', 9, 12, 'J4J T9L', 'Kingston'),
    ('Tommy2003', 'tommy@gmail.com', 'J3JHWOOE24Wgjsd3', 'Tommy Middle-Age', 10, 3, 'K2R N1H', 'Boston'),
    ('test', 'test@gmail.com', 'test', 'Test Name', 10, 8, 'test', 'Test')
]

# Product data
pdata = [
    ('Thomas', 'CLO' ,  'shirt',  8, '2023-11-04', 'Toronto'),
    ('Thomas', 'CLO' ,  'sweatpants',  10, '2022-12-29', 'Vancouver'),
    ('Thomas', 'CLO' ,  'blue fitted cap',  9, '2023-07-03', 'Montreal'),
    ('Thomas', 'CLO' ,  'avocado socks',  7, '2023-01-17', 'Calgary'),
    ('Thomas', 'CLO' ,  'shirt',  6, '2022-10-02', 'Toronto'),
    ('Thomas', 'CLO' ,  'dress',  9, '2021-12-24', 'Calgary'),
    ('Thomas', 'CLO' ,  'sweatpants',  5, '2023-08-30', 'Calgary'),
    ('Thomas', 'CLO' ,  'sweatpants',  7, '2023-02-18', 'Montreal'),
    ('Thomas', 'CLO' ,  'jeans',  8, '2022-05-22', 'Toronto'),
    ('Thomas', 'CLO' ,  'jeans',  7, '2023-09-10', 'Ottawa'),
    ('Tommy', 'ELE' ,  'sony headphones',  4, '2022-02-08', 'Toronto'),
    ('Tommy', 'ELE' ,  'apple watch',  7, '2019-10-13', 'Toronto'),
    ('Tommy', 'ELE' ,  'canon dslr',  8, '2020-08-29', 'Vancouver'),
    ('Tommy', 'ELE' ,  'ipad pro',  5, '2022-06-27', 'Montreal'),
    ('Tommy', 'ELE' ,  'hp laptop',  5, '2023-10-18', 'Ottawa'),
    ('Tommy', 'ELE' ,  'sony headphones',  7, '2023-04-06', 'Vancouver'),
    ('Tommy', 'ELE' ,  'iphone 11',  6, '2023-11-01', 'Toronto'),
    ('Tommy', 'ELE' ,  'ipad pro',  9, '2021-01-24', 'Montreal'),
    ('Tommy', 'ELE' ,  'ipad air',  8, '2020-08-20', 'Vancouver'),
    ('Tommy', 'ELE' ,  'nintendo switch',  8, '2022-11-30', 'Montreal'),
    ('Charles', 'STN' ,  'Calc II textbook',  3, '2022-05-20', 'Toronto'),
    ('Charles', 'STN' ,  'Scientific calculator',  10, '2023-09-09', 'Ottawa'),
    ('Charles', 'STN' ,  'Calc II textbook',  7, '2023-06-01', 'Calgary'),
    ('Charles', 'STN' ,  'Scientific calculator',  9, '2022-12-15', 'Montreal'),
    ('Charles', 'STN' ,  'post-it notes',  10, '2021-05-26', 'Toronto'),
    ('Charles', 'STN' ,  'bullet journal',  10, '2023-03-28', 'Ottawa'),
    ('Charles', 'STN' ,  'notebook',  9, '2021-06-22', 'Calgary'),
    ('Charles', 'STN' ,  'Anthro textbook',  5, '2022-05-31', 'Toronto'),
    ('Charles', 'STN' ,  'notebook',  7, '2023-10-12', 'Calgary'),
    ('Charles', 'STN' ,  'notebook',  8, '2022-07-21', 'Ottawa')
]

# Past Transactions data
tdata = [
    ('CLO', 'ELE', 'jeans', 'sony headphones', 'user_35', 'user_7', 8, 7, '2023-11-04'),
    ('ELE', 'ELE', 'iphone 11', 'nintendo switch', 'user_50', 'user_12', 6, 0, '2019-01-01'),
    ('STN', 'STN', 'Calc II textbook', 'Calc II textbook', 'user_39', 'user_84', 6, 7, '2022-06-15'),
    ('ELE', 'CLO', 'apple watch', 'shirt', 'user_60', 'user_92', 10, 5, '2020-08-30'),
    ('ELE', 'CLO', 'canon dslr', 'jeans', 'user_34', 'user_67', 0, 10, '2021-03-12'),
    ('ELE', 'CLO', 'iphone 11', 'jeans', 'user_58', 'user_91', 8, 9, '2023-09-01'),
    ('ELE', 'ELE', 'iphone 11', 'iphone 11', 'user_24', 'user_97', 9, 0, '2019-03-28'),
    ('CLO', 'ELE', 'shirt', 'sony headphones', 'user_13', 'user_83', 0, 8, '2021-09-15'),
    ('STN', 'STN', 'post-it notes', 'post-it notes', 'user_68', 'user_63', 8, 2, '2020-12-10'),
    ('CLO', 'CLO', 'avocado socks', 'avocado socks', 'user_88', 'user_71', 6, 6, '2023-05-19'),
    ('STN', 'STN', 'bullet journal', 'bullet journal', 'user_12', 'user_63', 10, 9, '2022-08-07'),
    ('CLO', 'CLO', 'sweatpants', 'avocado socks', 'user_88', 'user_18', 7, 4, '2022-02-14'),
    ('ELE', 'STN', 'iphone 11', 'Scientific calculator', 'user_66', 'user_63', 3, 5, '2020-10-29'),
    ('ELE', 'ELE', 'sony headphones', 'nintendo switch', 'user_22', 'user_98', 2, 9, '2020-09-16'),
    ('CLO', 'ELE', 'blue fitted cap', 'iphone 11', 'user_57', 'user_99', 4, 8, '2020-12-04'),
    ('CLO', 'ELE', 'avocado socks', 'nintendo switch', 'user_22', 'user_96', 2, 0, '2021-06-03'),
    ('ELE', 'ELE', 'sony headphones', 'apple watch', 'user_97', 'user_76', 9, 6, '2022-09-05'),
    ('STN', 'CLO', 'post-it notes', 'avocado socks', 'user_85', 'user_82', 3, 0, '2019-11-22'),
    ('CLO', 'STN', 'shirt', 'Scientific calculator', 'user_58', 'user_17', 9, 6, '2023-04-30'),
    ('STN', 'ELE', 'notebook', 'iphone 11', 'user_66', 'user_83', 7, 2, '2020-07-09'),
    ('CLO', 'ELE', 'jeans', 'apple watch', 'user_34', 'user_87', 9, 0, '2021-08-17'),
    ('STN', 'CLO', 'notebook', 'avocado socks', 'user_93', 'user_84', 7, 2, '2019-07-25'),
    ('CLO', 'STN', 'sweatpants', 'Scientific calculator', 'user_72', 'user_88', 9, 8, '2021-11-14'),
    ('ELE', 'ELE', 'hp laptop', 'hp laptop', 'user_33', 'user_51', 4, 6, '2019-06-03'),
    ('CLO', 'STN', 'avocado socks', 'Calc II textbook', 'user_1', 'user_18', 6, 9, '2021-12-22'),
    ('STN', 'ELE', 'Calc II textbook', 'iphone 11', 'user_17', 'user_19', 5, 5, '2022-05-20'),
    ('STN', 'STN', 'Calc II textbook', 'notebook', 'user_77', 'user_91', 0, 2, '2019-04-15'),
    ('ELE', 'STN', 'sony headphones', 'Scientific calculator', 'user_39', 'user_46', 2, 5, '2021-10-03'),
    ('STN', 'CLO', 'notebook', 'avocado socks', 'user_94', 'user_25', 9, 9, '2022-11-23'),
    ('ELE', 'CLO', 'sony headphones', 'jeans', 'user_2', 'user_7', 8, 8, '2022-01-12')
]


cur.executemany(
    "INSERT INTO product VALUES(?, ?, ?, ?, ?, ?)", pdata)
con.commit()

cur.executemany(
    "INSERT INTO transactions VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", tdata)
con.commit()

cur.executemany(
    "INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", udata)
con.commit()

con.close()