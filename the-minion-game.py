import math
string_to_play = "BANANA"

string_to_count = string_to_play.casefold()

def possible_combinations(number_of_letters):
    return math.factorial(number_of_letters)

vocals = ["a", "e", "i", "o", "u"]

n_vocals = 0
n_consonants = 0

kevin_points = 0
stuart_points = 0

for vocal in vocals:
    kevin_points += string_to_count.count(vocal) * possible_combinations(len(string_to_count) - 1)

print(kevin_points)

for letter in string_to_count:
    if letter not in vocals:
        stuart_points += 

