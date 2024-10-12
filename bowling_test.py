import unittest
from bowling import Pin, BowlingGame

class TestPin(unittest.TestCase):
    def test_pin_score(self):
        pin = Pin(5)
        self.assertEqual(pin.score, 5)

    def test_pin_score_invalid(self):
        with self.assertRaises(AssertionError):
            Pin(11)
        with self.assertRaises(AssertionError):
            Pin(-1)

class TestBowlingGame(unittest.TestCase):
    def test_bowling_game_score(self):
        game = BowlingGame()
        game.add(Pin(3))
        game.add(Pin(5))
        self.assertEqual(game.score, 8)

    def test_bowling_game_empty(self):
        game = BowlingGame()
        self.assertEqual(game.score, 0)
    
    def test_bowling_game_strike_should_score_10(self):
        game = BowlingGame()
        game.add(Pin(10))
        self.assertEqual(game.score, 10)
    
    def test_bowling_game_strike_in_a_row_should_add_bonus(self):
        game = BowlingGame()
        game.add(Pin(10))
        game.add(Pin(10))
        self.assertEqual(game.score, 30)

if __name__ == '__main__':
    unittest.main()