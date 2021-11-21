import itertools
from model.action import Action


class Store:
    def __init__(self):

        self.data = {"actions": [], "invest": 500}

    def get_action(self):
        data = [
            {"name": "action-1", "cpa": 20, "benef": 5},
            {"name": "action-2", "cpa": 30, "benef": 10},
            {"name": "action-3", "cpa": 50, "benef": 15},
            {"name": "action-4", "cpa": 70, "benef": 20},
            {"name": "action-5", "cpa": 60, "benef": 17},
            {"name": "action-6", "cpa": 80, "benef": 25},
            {"name": "action-7", "cpa": 22, "benef": 7},
            {"name": "action-8", "cpa": 26, "benef": 11},
            {"name": "action-9", "cpa": 48, "benef": 13},
            {"name": "action-10", "cpa": 34, "benef": 27},
            {"name": "action-11", "cpa": 42, "benef": 17},
            {"name": "action-12", "cpa": 110, "benef": 9},
            {"name": "action-13", "cpa": 38, "benef": 23},
            {"name": "action-14", "cpa": 14, "benef": 1},
            {"name": "action-15", "cpa": 18, "benef": 3},
            {"name": "action-16", "cpa": 8, "benef": 8},
            {"name": "action-17", "cpa": 4, "benef": 12},
            {"name": "action-18", "cpa": 10, "benef": 14},
            {"name": "action-19", "cpa": 24, "benef": 21},
            {"name": "action-20", "cpa": 114, "benef": 18},
        ]

        for action in data:
            self.data["actions"].append(
                Action(action["name"], action["cpa"], action["benef"])
            )

    def search_combination(self, r):

        #Retourne toutes les combinaisons possible à r elements
        combination_actions = itertools.combinations(self.data["actions"], r)
        for combination in combination_actions:

            cpa = sum(a.cpa for a in combination)
            benefice = sum(a.benefice for a in combination)

            if cpa <= self.data["invest"]:

                yield {"combination" : combination, "cpa": cpa, "benefice": benefice}



