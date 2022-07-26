import sqlite3


class Repo:
    def __init__(self) :
        try:
            self.conn = sqlite3.connect('database.db', check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            # self.conn = psycopg2.connect(
            # user="postgres", password="password", host="127.0.0.1", port="5432", database="postgres")
            #  self.conn = psycopg2.connect(config["DATABASE_URL"])
            self.cur = self.conn.cursor()
            print("Opened database successfully")
        except Exception as e:
            print(e)

    def __del__(self):
        try:
            self.conn.close()
            print("Database Closed successfully")
        except Exception as e:
            print(e)


