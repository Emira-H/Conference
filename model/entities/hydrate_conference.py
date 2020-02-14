from .hydrate_conferencier import HydraConferencier

class HydraConference:
    def __init__(self, dico):
        self.id = None
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.date_creation = None
        self.id_conferencier = None
        self.firstname = None
        self.name = None
        self.hydrate(dico)

    def hydrate(self, dico):
        for key, value in dico.items():
            if hasattr(self,key):
                setattr(self, key, value)

    def __str__(self):
        return "-------------------\nid: {}\ntitle: {} \nresume: {} \ndate: {}\nheure: {} \ndate_creation: {}\nconferencier: {}".format(
            self.id,
            self.title,
            self.resume,
            self.date,
            self.hour,
            self.date_creation,
            self.firstname + " " + self.name)
