import math
string_to_play = "BANANA"

string_to_count = string_to_play.casefold()

def possible_combinations(string_: str):
    return math.factorial(len(string_))

vocals = ["a", "e", "i", "o", "u"]

n_vocals = 0
n_consonants = 0

kevin_points = 0
stuart_points = 0

for vocal in vocals:
    n_vocals += string_to_count.count(vocal)
n_consonants = len(string_to_count) - n_vocals

kevin_points = n_vocals