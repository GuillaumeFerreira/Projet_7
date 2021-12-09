class HomeView:
    @classmethod
    def home(cls):
        print("Bienvenue sur le menu principal\n")
        print("1. Executer le script 'bruteforce'\n")
        print("2. Executer le script 'optimized'\n")
        print("3. Charger dataset 1 \n")
        print("4. Charger dataset 2\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: \n")
