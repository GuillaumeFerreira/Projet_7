class Optimized_view:
    @classmethod
    def result(cls, poid, benef, elements):
        for el in elements:
            print(el.name + " " + str(el.cpa))
        print(
            " benefice = "
            + str(benef)
            + " pour un investissement de "
            + str(poid)
        )

        print("H. Revenir au menu principal\n")
        print("Q. Quitter le programme\n")

        choice = input("Votre choix: \n")
        if choice.lower() == "q":
            return "quit"
        elif choice.lower() == "h":
            return "homepage"
