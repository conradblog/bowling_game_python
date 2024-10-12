# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️

import platform
from bowling import Pin, BowlingGame

def main():
    bowling_game = BowlingGame()
    bowling_game.add(Pin(5))
    bowling_game.add(Pin(3))
    print(f"Total score: {bowling_game.score}")
    print(f"Python version: {platform.python_version()}")

if __name__ == '__main__':
    main()