from view.optimized_view import Optimized_view


class Optimized:

    # Solution optimale - programmation dynamique
    @classmethod
    def sacADos_dynamique(cls, store, route_params):
        # objectif complexité linéaire O(n) ou pseudo linéaire O(n log n )

        capacite = store.data["invest"] * 100
        elements = store.data["actions"]
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

        benef = 0
        e = elements[n - 1]

        while w - e.cpa > 0 and n >= 0:
            e = elements[n - 1]

            if matrice[n][w] == matrice[n - 1][w - e.cpa] + e.benefice:
                elements_selection.append(e.name)

                benef = benef + e.benefice
                w -= e.cpa

            n -= 1
        poid = capacite - w

        return (
            Optimized_view.result(poid / 100, benef / 100, elements_selection),
            None,
        )
