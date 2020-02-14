from model.connection import Connection
from model.entities.hydrate_conferencier import HydraConferencier

class ConferencierModel:
    def __init__(self):
        self.db = Connection()

    def add_conferencier(self,firstname, name, description, profession):
        sql = """INSERT INTO conferencier (firstname, name, description, profession) VALUES (%s, %s, %s, %s);"""
        arguments = (firstname, name, description, profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_conferencier(self, id):
        sql = """DELETE FROM conferencier WHERE id=%s;"""
        arguments = (id, )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def display_conferencier(self):
        sql = """SELECT * FROM conferencier WHERE statut_actif = True;"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        actif_conferenciers = self.db.cursor.fetchall()
        for key, value in enumerate(actif_conferenciers):
            actif_conferenciers[key]= HydraConferencier(value)
        self.db.close_connection()
        return actif_conferenciers
