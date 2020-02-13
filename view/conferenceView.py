from model.conferenceModel import ConferenceModel

class ConferenceView:

    speech = ConferenceModel()

    def __init__(self):
        pass

    def add_conference(self):
        title = input("saisir le titre de la conférence à ajouter:")
        resume = input("ajouter le résumé de la conférence:")
        date = input("ajouter la date de la conférence:")
        hour = input("ajouter l'heure de la conférence:")
        date_creation = input("ajouter la date de création de la conférence:")
        id_conferencier = input("ajouter l'ID du conférencier:")
        self.speech.add_conference(title, resume, date, hour, date_creation, id_conferencier)


    def del_conference(self):
        id = input("Veuillez saisir l'identifiant de la conférence pour la supprimer:")
        self.speech.del_conference(id)

    def display_conference(self):
        liste_conferences = self.speech.display_conference()
        for conference in liste_conferences:
            print(f"*********************************************************************************\n  {conference}")
