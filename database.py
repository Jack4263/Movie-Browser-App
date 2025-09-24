import sqlite3

class MovieDatabase:
    def __init__(self, db_file="MovieApp.db"): 
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS Movies (movieID INTEGER PRIMARY KEY,title TEXT,genres TEXT,release_year TEXT,rating TEXT,overview TEXT)")
        self.conn.commit()
        self.c.execute("CREATE TABLE IF NOT EXISTS Users (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)")
        self.conn.commit()

    def add_movie(self, id, title, genres, release_year, rating=None, overview=None):
        self.c.execute("INSERT INTO Movies (ID, title, genres, release_year, rating, overview) VALUES (?,?,?,?,?,?)",(id, title, genres, release_year, rating, overview))
        self.conn.commit()

    def add_movie(self, userid, username, passowrd, email):
        self.c.execute("INSERT INTO Movies (userID, username, password, email) VALUES (?,?,?,?)", (userid, username, passowrd, email))
        self.conn.commit()

