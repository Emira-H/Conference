from view.conferenceView import ConferenceView
from view.confView import ConfView

choice_menu = ""
choice_user = ""
menu_CF = ConferenceView()
menu_CFR = ConfView()

if __name__ == '__main__':

    while choice_menu not in ["CF", "CFR","Q"]:
        choice_menu = input("Veuillez saisir CF pour la gestion des conférences ou CFR pour la gestion des conférenciers:").upper()

        if choice_menu == "CF":
            while choice_user not in ["C", "S","V","Q"]:
                choice_user = input("Taper: \n C pour créer une conférencier\n S pour supprimer un conférencier\n V pour voir les conférenciers:").upper()

                if choice_user == "C":
                    menu_CF.add_conference()
                elif choice_user == "S":
                    menu_CF.del_conference()
                elif choice_user == "V":
                    menu_CF.display_conference()
                elif choice_user == "Q":
                    choice_menu = input("Veuillez saisir CF pour la gestion des conférences ou CFR pour la gestion des conférenciers:").upper()

        elif choice_menu == "CFR":
            choice_user = input("Taper C pour créer une conférencier\nTaper S pour supprimer un conférencier\n ou V pour voir les conférenciers:").upper()
            while choice_user not in ["C", "S","V","Q"]:
                choice_user = input("Taper C pour créer une conférencier\nTaper S pour supprimer un conférencier\n ou V pour voir les conférenciers:").upper()

                if choice_user == "C":
                    menu_CFR.add_conferencier()
                elif choice_user == "S":
                    menu_CFR.del_conferencier()
                elif choice_user == "V":
                    menu_CFR.display_conferencier()
                elif choice_user == "Q":
                    choice_menu = input("Veuillez saisir CF pour la gestion des conférences ou CFR pour la gestion des conférenciers:").upper()

        elif choice_menu == "Q":
            exit()
