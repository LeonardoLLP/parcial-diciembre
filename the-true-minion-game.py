import math
string_to_play = "BANANA"

string_to_count = string_to_play.casefold()

def possible_combinations(number_of_letters):
    return math.factorial(number_of_letters)

vocals = ["a", "e", "i", "o", "u"]

kevin_points = 0
stuart_points = 0

for letter_index in range(len(string_to_count)):
    if string_to_count[letter_index] in vocals:
        kevin_points += len(string_to_count[letter_index:])
    else:
        stuart_points += len(string_to_count[letter_index:])




if kevin_points > stuart_points:
    print("Kevin won with {} points".format(kevin_points))
elif stuart_points > kevin_points:
    print("Stuart won with {} points".format(stuart_points))
else:
    print("It was a draw")