import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY Key, ratio text, meal text, date text, "
                         "blood_sugar text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM place")
        rows = self.cur.fetchall()
        return rows

    def insert(self, ratio, meal, date, blood_sugar):
        self.cur.execute("INSERT INTO place VALUES (NULL, ?, ?, ?, ?)",
                         (ratio, meal, date, blood_sugar))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM place WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, ratio, meal, date, blood_sugar):
        self.cur.execute("UPDATE place SET ratio = ?, meal = ?, date = ?, blood_sugar = ? WHERE id = ?",
                         (ratio, meal, date, blood_sugar, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
