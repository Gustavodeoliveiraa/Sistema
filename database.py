import mysql.connector


class Database:

    def __init__(self, host='localhost', user='root',
                 password='300423', database='auto_ar') -> None:

        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self):
        self.connect = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor_ = self.connect.cursor()

    def disconnect(self):
        self.cursor_.close()

    def Query(self, sql):
        self.connection()
        self.cursor_.execute(sql)
        result = self.cursor_.fetchall()
        self.disconnect()
        return result

    def manipulation(self, sql) -> None:
        self.connection()
        self.cursor_.execute(sql)
        self.connect.commit()
        self.disconnect()
