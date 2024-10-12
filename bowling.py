class Pin:
    def __init__(self, score):
        self._score = 0
        self.set_score(score)

    def set_score(self, score):
        assert 0 <= score <= 10, "Score must be between 0 and 10"
        self._score = score

    @property
    def score(self):
        return self._score

class BowlingGame:
    def __init__(self):
        self._pins = []

    def add(self, pin):
        self._pins.append(pin)

    @property
    def score(self):
        return sum(pin.score for pin in self._pins)