from view.optimized_view import Optimized_view
from tqdm import tqdm


class Optimized:

    # Solution optimale - programmation dynamique
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
        # Construction de la matrice vide à n éléments et m max_inv
        """
        |0 0 0 ... m|
        |. . . ... m|
        |. . . ... m|
        |n n n ... m|
        """
        ks = [[0 for x in range(max_inv + 1)] for x in range(shares_total + 1)]

        #On rempli la matrice , on va regarder pour chaque cout la valeur la plus rentable
        #Exemple avec 4 valeurs [ [poid = 1 ,val = 1], [poid = 3 ,val = 4] , [poid = 4 ,val = 5] , [poid = 5 ,val = 7] ] --> 'shares_total' et un investissement de 7--> 'max_inv'
        #Si le le cout est suffisant on fait max( valeur de l element regardé + valeur de la case de la ligne d avant et pour la colonne on se place en fonction du cout utilisé , ou on prend la meme colonne de la ligne precedente)
        #cost[1, 3, 4, 5] , profit[1, 4, 5, 7]
        #Exemple pour ks[i=4][w=5]= max( profit[4-1] + ks[4-1][5-cost[4-1]],ks[4-1][5]=max( 7 + ks[3][0],ks[3][5])=max(7+0,7)=7
        #Exemple pour ks[i=2][w=7]= max( profit[2-1] + ks[2-1][7-cost[2-1]],ks[2-1][7]=max( 4 + ks[1][4],ks[1][7])=max(4+5,5)=9
        """ 
           0 1 2 3 4 5 6 7      0 1 2 3 4 5 6 7       
        1 |0 0 0 0 0 0 0 0|  1 |0 1 1 1 1 1 1 1 | 
        3 |0 0 0 0 0 0 0 0|  3 |0 1 1 4 5 5 5 5 |
        4 |0 0 0 0 0 0 0 0|  4 |0 1 1 4 5 6 6 9 |
        5 |0 0 0 0 0 0 0 0|  5 |0 1 1 4 5 7 8 9 |
        """

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
