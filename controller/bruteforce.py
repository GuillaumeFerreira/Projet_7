from view.bruteforce_view import Bruteforce_view

class Bruteforce:

    @classmethod
    def run(cls, store, route_params):
        store.get_action()

        choice = Bruteforce_view.result(store)
        if choice.lower() == "q":
            next = "quit"
        elif choice.lower() == "h":
            next ="homepage"

        return next, None