from view.home_view import HomeView

class HomePage:
    @classmethod
    def dispatch(cls, store, route_params):

        choice = HomeView.home()

        if choice.lower() == "q":
            next = "quit"

        elif choice == "1":
            next = "bruteforce"
        elif choice == "2":
            next = "optimized"


        return next, store