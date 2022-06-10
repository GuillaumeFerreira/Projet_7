from view.optimized_view import Optimized_view
from tqdm import tqdm


class Optimized:

    # Solution optimale - programmation dynamique
    @classmethod
    def sacADos_dynamique1(cls, store, route_params):
        # objectif complexité linéaire O(n)
        # ou pseudo linéaire O(n log n ) ou logarithmique O(log n )

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

    @classmethod
    def sacADos_dynamique(cls, store, route_params):
        """Initialize the matrix (ks) for 0-1 knapsack problem
        Get best shares combination
        @param shares_list: shares data (list)
        @return: best possible combination (list)
        """

        max_inv = store.data["invest"] * 100  # capacity
        shares_total = len(store.data["actions"])
        cost = []  # weights
        profit = []  # values

        for share in store.data["actions"]:
            cost.append(int(share.cpa * 100))
            profit.append(share.benefice)

        # Find optimal profit
        ks = [[0 for x in range(max_inv + 1)] for x in range(shares_total + 1)]

        for i in tqdm(range(1, shares_total + 1)):

            for w in range(1, max_inv + 1):
                if cost[i - 1] <= w:
                    ks[i][w] = max(
                        profit[i - 1] + ks[i - 1][w - cost[i - 1]],
                        ks[i - 1][w],
                    )
                else:
                    ks[i][w] = ks[i - 1][w]

        # Retrieve combination of shares from optimal profit
        best_combo = []
        best_cost = 0
        best_inv = 0
        while max_inv >= 0 and shares_total >= 0:

            if (
                ks[shares_total][max_inv]
                == ks[shares_total - 1][max_inv - cost[shares_total - 1]]
                + profit[shares_total - 1]
            ):

                best_combo.append(store.data["actions"][shares_total - 1])
                max_inv -= cost[shares_total - 1]

            shares_total -= 1

        for action in best_combo:
            best_cost = action.cpa + best_cost
            best_inv = action.benefice + best_inv
        return (
            Optimized_view.result(best_cost, best_inv, best_combo),
            None,
        )
