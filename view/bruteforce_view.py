class Bruteforce_view:
    @classmethod
    def result(cls, phrase_combi, max, cout_max):

        print(
            "\n( "
            + phrase_combi
            + " ) benefice = "
            + str(max)
            + " pour un investissement de "
            + str(cout_max)
        )
        print("H. Revenir au menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: \n")
