class HydraConferencier:
    def __init__(self, dico):
        self.id = None
        self.firstname = None
        self.name = None
        self.profession = None
        self.description = None
        self.hydrate(dico)

    def hydrate(self, dico):
        for key, value in dico.items():
            if hasattr(self,key):
                setattr(self, key, value)

    def __str__(self):
        return """----------------------------------------------------------------\n \
            id: {}\n \
            firstname: {} \n \
            name: {} \n \
            description: {}\n \
            profession: {} \n""".format(self.id, self.firstname, self.name, self.description, self.profession)
