class Optimized:
    @classmethod
    def run(cls, store, route_params):

        #store.get_action()
        poid, benef, elements = cls.sacADos_dynamique(
            store.data["invest"], store.data["actions"]
        )
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
            next = "quit"
        elif choice.lower() == "h":
            next = "homepage"

        return next, None

    # Solution optimale - programmation dynamique
    @classmethod
    def sacADos_dynamique(cls, capacite, elements):
        matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

        for i in range(1, len(elements) + 1):
            for w in range(1, capacite + 1):
                if elements[i - 1].cpa <= w:
                    matrice[i][w] = max(
                        elements[i - 1].benef + matrice[i - 1][w - elements[i - 1].cpa],
                        matrice[i - 1][w],
                    )
                else:
                    matrice[i][w] = matrice[i - 1][w]

        # Retrouver les éléments en fonction de la somme
        w = capacite
        n = len(elements)
        elements_selection = []
        poid = 0
        benef = 0
        while w >= 0 and n >= 0:
            e = elements[n - 1]
            if matrice[n][w] == matrice[n - 1][w - e.cpa] + e.benef:
                elements_selection.append(e.name)
                poid = poid + e.cpa
                benef = benef + (e.benef * e.cpa / 100)
                w -= e.cpa

            n -= 1
        # matrice[-1][-1]
        return poid, benef, elements_selection
