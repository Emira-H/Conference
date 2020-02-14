from model.connection import Connection
from model.entities.hydrate_conference import HydraConference

class ConferenceModel:
    def __init__(self):
        self.db = Connection()


    def add_conference(self,title, resume, date, hour, date_creation, id_conferencier):
        sql = """INSERT INTO conference (title, resume, date, hour, date_creation, id_conferencier) VALUES (%s, %s, %s, %s, %s, %s);"""
        arguments = (title, resume, date, hour, date_creation, id_conferencier)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_conference(self, id):
        sql = """DELETE FROM conference WHERE id=%s;"""
        arguments = (id, )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def display_conference(self):
        sql = """SELECT a.*, b.firstname, b.name FROM conference as a
                INNER JOIN conferencier as b
                ON a.id_conferencier = b.id;"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        conferences = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(conferences):
            conferences[key]= HydraConference(value)
        return conferences
