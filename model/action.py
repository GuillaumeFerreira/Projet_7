class Action:
    def __init__(self, name, cpa, benef):

        self.name = name
        self.cpa = cpa
        self.benef = benef

    @property
    def benefice(self):
        return self.cpa * self.benef / 100
