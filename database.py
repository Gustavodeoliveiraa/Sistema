
import sqlite3 as sq
import os


class Database():

    def __init__(self):
        USERNAME = os.getlogin()
        self.conn = sq.connect(F"C:/Users/{USERNAME}/auto_ar")
        self.cursor = self.conn.cursor()

    def Query(self, msg) -> list:
        self.cursor.execute(msg)
        result = self.cursor.fetchall()
        return result

    def manipulation(self, sql): 
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == "__main__":
    c = Database()
    c.manipulation("CREATE TABLE IF NOT EXISTS teste (id integer, nome text);")
    c.manipulation('INSERT INTO teste VALUES ("0", "ola");')
