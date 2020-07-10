class MoneyBox:
    def __init__(self, capaciti):
        self.capaciti = capaciti
        self.money = 0

    def can_add(self, v):
        if self.capaciti >= (self.money + v):
            return True
        else:
            return False

    def add(self, v):
        self.money += v
