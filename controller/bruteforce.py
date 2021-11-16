from view.bruteforce_view import Bruteforce_view

class Bruteforce:

    @classmethod
    def run(cls, store, route_params):
        store.get_action()
        actions_data = store.data['actions']



        conbinations = {}
        max=0
        combi_max =""
        cout_max = 0

        #On récupère toutes les combinaisons possible avec un investissement de 500 ici
        for i in range(2,len(actions_data)+1):

            conbinations[i] = store.search_combination(i)

        #On recherche la meilleur combinaison
        for nb_combination,combination in conbinations.items():

            for actions in combination:
                combi =[]
                somme = 0
                cout = 0
                for action in actions:
                    combi.append(action)
                    somme = somme + (action.cpa * action.benef / 100)
                    cout = cout + action.cpa
                if max < somme:

                    max=somme
                    combi_max = combi
                    cout_max = cout

        phrase_combi ="( "
        for action in combi_max:
            phrase_combi = phrase_combi + action.name +", "

        #print( phrase_combi + " ) benefice = " + str(max) + " pour un investissement de " + str(cout_max))







        choice = Bruteforce_view.result(phrase_combi,max,cout_max)
        if choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next ="homepage"

        return next, None