import os
from controller.home_controller import HomePage
from controller.bruteforce import Bruteforce
from controller.optimized import Optimized
from controller.dataset import Dataset
from model.store import Store


class Application:
    routes = {
        "homepage": HomePage.dispatch,
        "bruteforce": Bruteforce.run,
        "optimized": Optimized.sacADos_dynamique,
        "dataset1": Dataset.charger_dataset1,
        "dataset2": Dataset.charger_dataset2,
        "dataset": Dataset.charger_dataset,
    }

    def __init__(self) -> None:

        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()
        # self.store.get_action()

    def run(self):
        while not self.exit:
            # On efface la console pour avoir une interface propre
            os.system("cls")

            controller_method = self.routes[self.route]
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            self.route = next_route
            self.route_params = next_params

            if next_route == "quit":
                self.exit = True
