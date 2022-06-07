from view.bruteforce_view import Bruteforce_view
import itertools


class Bruteforce:
    @classmethod
    def search_combination(cls, r, store):

        # Retourne toutes les combinaisons possible à r elements
        combination_actions = itertools.combinations(store.data["actions"], r)
        for combination in combination_actions:

            cpa = sum(a.cpa for a in combination)
            benefice = sum(a.benefice for a in combination)

            if cpa <= store.data["invest"]:

                yield {
                    "combination": combination,
                    "cpa": cpa,
                    "benefice": benefice,
                }

    @classmethod
    def run(cls, store, route_params):
        # complexité temporelle --> 2^n + n --> O(2^n) ?
        # complexité spatiale --> 7 + n -->  O(n) ?

        max = 0
        combi_max = ""
        cout_max = 0

        # On récupère toutes les combinaisons possible
        for i in range(2, len(store.data["actions"]) + 1):

            for combination_dict in cls.search_combination(i, store):
                if combination_dict["benefice"] > max:
                    max = combination_dict["benefice"]
                    combi_max = combination_dict["combination"]
                    cout_max = combination_dict["cpa"]

        phrase_combi = "( "
        for action in combi_max:
            phrase_combi = phrase_combi + action.name + ", "

        choice = Bruteforce_view.result(phrase_combi, max, cout_max)
        if choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next = "homepage"

        return next, None
