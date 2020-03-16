import difflib
import json
from difflib import SequenceMatcher

SequenceMatcher(None, "rainn", "rain").ratio()

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

print(translate(word))