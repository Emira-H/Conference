from model.connection import Connection
from model.entities.hydrate_conferencier import HydraConferencier

#Class to manage the speakers
class ConferencierModel:
    def __init__(self):
        self.db = Connection()

#method to add a conferencier in the table conferenciers
    def add_conferencier(self,firstname, name, description, profession):
        sql = """INSERT INTO conferencier (firstname, name, description, profession) VALUES (%s, %s, %s, %s);"""
        arguments = (firstname, name, description, profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

#method to delete a conferencier in the table conferenciers by id

    def del_conferencier(self, id):
        sql = """DELETE FROM conferencier WHERE id=%s;"""
        arguments = (id, )
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

#method to display all conferencier actifs
    def display_conferencier(self):
        sql = """SELECT * FROM conferencier WHERE statut_actif = True;"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
# we stock the fetchall in a variable which is a list of tuples containing rows of the result of the request
        actif_conferenciers = self.db.cursor.fetchall()
# we use the hydratation method in order to display the fetchall in a particular way defined in this method
        for key, value in enumerate(actif_conferenciers):
            actif_conferenciers[key]= HydraConferencier(value)
        self.db.close_connection()
        return actif_conferenciers
