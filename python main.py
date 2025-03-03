
#### main.py

```python
#!/usr/bin/env python3
import random

civilizations = [
    "The Astral Keepers – Masters of the cosmos, their observatories mapped the heavens before they mysteriously vanished.",
    "The Sunborn Empire – Harnessed the power of the sun, but were destroyed by an eternal eclipse.",
    "The Umbral Dynasty – An advanced civilization that mastered shadow magic, only to be lost in its own darkness.",
    "The Gilded Dominion – Builders of golden towers, toppled when greed consumed their hearts.",
    "The Echo Tribes – Their voices still haunt the ruins, whispering secrets of the past."
]

def get_random_civilization():
    return random.choice(civilizations)

def main():
    print("Welcome to Chronicles of the Elders!")
    print("Here is a randomly generated lost civilization and its wisdom:")
    print(get_random_civilization())

if __name__ == "__main__":
    main()
