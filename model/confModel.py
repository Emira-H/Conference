from model.connection import Connection

class ConferencierModel:
    def __init__(self):
        self.db = Connection()


    def add_conferencier(self,firstname, name, description, profession):
        arguments = (firstname, name, description, profession)
        sql = """INSERT INTO conferencier (firstname, name, description, profession) VALUES (%s, %s, %s, %s);"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_conferencier(self, arguments):
        arguments = (id, )
        sql = """DELETE FROM conferencier WHERE id=%s"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql,arguments)
        self.db.close_connection()

    def display_conferencier(self):
        sql = """SELECT * FROM conferencier WHERE statut_actif = True"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.close_connection()
