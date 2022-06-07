import xlsxwriter


class Optimized:
    @classmethod
    def run(cls, store, route_params):

        # store.get_action()
        # import pdb;pdb.set_trace()
        poid, benef, elements = cls.sacADos_dynamique(
            store.data["invest"], store.data["actions"]
        )
        print(
            str(elements)
            + " benefice = "
            + str(benef / 100)
            + " pour un investissement de "
            + str(poid / 100)
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
        # creation matrice vide
        matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

        # rempli la matrice
        for i in range(1, len(elements) + 1):
            for w in range(1, capacite + 1):
                if elements[i - 1].cpa <= w:
                    matrice[i][w] = max(elements[i - 1].benefice, matrice[i - 1][w])
                else:
                    matrice[i][w] = matrice[i - 1][w]

        w = capacite
        n = len(elements)
        elements_selection = []
        # poid = 0
        benef = 0
        e = elements[n - 1]
        # while w >= 0 and n >= 0:
        while w - e.cpa > 0 and n >= 0:
            e = elements[n - 1]

            # if e.cpa <= w:
            if matrice[n][w] == matrice[n - 1][w - e.cpa] + e.benefice:
                elements_selection.append(e.name)

                # poid = e.cpa
                benef = benef + e.benefice
                w -= e.cpa

            n -= 1
        poid = capacite - w

        # + matrice[i - 1][w - elements[i - 1].cpa]
        # cls.write_matrice( matrice, capacite, elements)
        return poid, benef, elements_selection

    @classmethod
    def write_matrice(cls, matrice, capacite, elements):
        workbook = xlsxwriter.Workbook("hello.xlsx")
        worksheet = workbook.add_worksheet()
        for i in range(1, len(elements) + 1):
            for w in range(1, capacite + 1):
                worksheet.write(i, w, str(matrice[i][w]))

        workbook.close()
