import mysql.connector

from object import Phone


class Database:
    def __init__(self):
        self.con = mysql.connector.connect(host='gendalf.cf', port=3308, user='root', password='1234567890', database='Pasina')
        self.cur = self.con.cursor()

    def upload_phone(self, phone: Phone):
        self.cur.execute('INSERT INTO phone (name, price, url) VALUES (%s,%s,%s)', (phone.name, phone.price, phone.url))

    def commit(self):
        self.con.commit()

    def truncate(self):
        self.cur.execute('TRUNCATE phone')


