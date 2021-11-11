class Bruteforce_view:

    @classmethod
    def result(cls,store):
        print("Le meilleur investissement est : \n")
        for action in store.data['actions']:
            print( action.name +' avec un bénéfice apres 2 ans de ' + str(action.benef * action.benef / 100))

        print("H. Revenir au menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: \n")