import xlsxwriter
from view.optimized_view import Optimized_view

class Optimized:
    @classmethod
    def run(cls, store, route_params):

        poid, benef, elements = cls.sacADos_dynamique(
            store.data["invest"], store.data["actions"]
        )
        next = Optimized_view.result(cls, poid, benef, elements)

        return next, None

    # Solution optimale - programmation dynamique
    @classmethod
    def sacADos_dynamique(cls, capacite, elements):
        # creation matrice vide
        matrice = [
            [0 for x in range(capacite + 1)] for x in range(len(elements) + 1)
        ]

        # rempli la matrice
        for i in range(1, len(elements) + 1):
            for w in range(1, capacite + 1):
                if elements[i - 1].cpa <= w:
                    matrice[i][w] = max(
                        elements[i - 1].benefice, matrice[i - 1][w]
                    )
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


        return poid, benef, elements_selection


