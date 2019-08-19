from guess_game import number_range


class Ticket:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if type(self) == type(other) and self.number == other.number:
            return True
        else:
            return False

    def is_valid(self):
        assert type(self.number) == int

        if number_range >= self.number >= 0:
            return True
        else:
            return False
