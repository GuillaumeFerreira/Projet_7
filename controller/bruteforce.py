from view.bruteforce_view import Bruteforce_view
import itertools
from tqdm import tqdm


class Bruteforce:
    @classmethod
    def run(cls, store, route_params):
        # complexité temporelle --> 2^n + n --> O(2^n)
        # complexité spatiale --> 7 + n -->  O(n) ?

        maximun = 0
        cout_max = 0
        selection_actions = []
        phrase_combi = ""

        # Début logique bruteforce
        # Utilisation tqdm pour chargement console
        for i in tqdm(range(len(store.data["actions"]), 0, -1)):
            # Retourne toutes les combinaisons possible à i elements
            combination_actions = itertools.combinations(
                store.data["actions"], i
            )

            for combination in combination_actions:

                sum_cpa = 0
                sum_benef = 0
                valeur_dep = False
                for a in combination:
                    sum_cpa = a.cpa + sum_cpa
                    sum_benef = a.benefice + sum_benef
                    if sum_cpa > store.data["invest"]:
                        valeur_dep = True
                        break

                if valeur_dep is False and sum_benef > maximun:
                    maximun = sum_benef
                    selection_actions = combination
                    break
        # Fin logique bruteforce

        # Logique pour affichage résultat
        for action in selection_actions:
            phrase_combi = phrase_combi + action.name + ", "
            cout_max = action.cpa + cout_max

        # Affichage résultat
        choice = Bruteforce_view.result(phrase_combi, maximun, cout_max)
        if choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next = "homepage"

        return next, None
