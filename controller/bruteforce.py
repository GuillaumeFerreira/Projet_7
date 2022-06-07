from view.bruteforce_view import Bruteforce_view


class Bruteforce:
    @classmethod
    def run(cls, store, route_params):
        # store.get_action()

        max = 0
        combi_max = ""
        cout_max = 0

        # On récupère toutes les combinaisons possible avec
        # un investissement de 500 ici
        for i in range(2, len(store.data["actions"]) + 1):

            for combination_dict in store.search_combination(i):
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
