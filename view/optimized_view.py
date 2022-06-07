class Optimized_view:
    @classmethod
    def result(cls, poid, benef, elements):
        print(
            str(elements)
            + " benefice = "
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
