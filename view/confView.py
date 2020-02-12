
from model.confModel import ConferencierModel

class ConfView:

    author = ConferencierModel()

    def __init__(self):
        pass


    def add_conferencier(self):
        firstname = input("Veuillez ajouter le prénom du conférencier: ")
        name = input("Veuillez ajouter le nom du conférencier: ")
        description = input("Veuillez ajouter la description: ")
        profession = input("Veuillez saisir la profession du conférencier: ")
        self.author.add_conferencier(firstname, name, description, profession)

    def del_conferencier(self):
        id = input("Veuillez saisir l'identifiant du conférencier à supprimer")
        self.author.del_conferencier(id)

    def display_conferencier(self):
        conferenciers_actifs = self.author.display_conferencier()
        if conferenciers_actifs:
            for conferencier in conferenciers_actifs:
                print(conferencier)
        else:
            print("Aucun conférencier actif")
