
#### main.py

```python
#!/usr/bin/env python3
import random

empires = [
    "The Starlight Dominion – A civilization of astronomers who vanished when the stars realigned.",
    "The Iron Sovereigns – A brutal empire of warriors, lost to a rebellion erased from history.",
    "The Obsidian Court – A kingdom built on magic, collapsed when their spells turned against them.",
    "The Sapphire Citadel – A floating city that disappeared into the clouds, never to descend again.",
    "The Crimson Pact – A society ruled by an eternal emperor, who vanished without a trace."
]

def get_random_empire():
    return random.choice(empires)

def main():
    print("Welcome to Forgotten Empires!")
    print("Here is a randomly generated lost empire and its fate:")
    print(get_random_empire())

if __name__ == "__main__":
    main()
