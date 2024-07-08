import os
import webbrowser
import shutil
from random import choice

FILEPATH = os.path.abspath(os.path.dirname(__file__))

TOPICS = {
    "A": "Algebra",
    "C": "Combinatorics",
    "G": "Geometry",
    "N": "Number Theory"
}

topic = input("Choose topic A/C/G/N or leave empty: ").upper()
if topic not in "AGCN" or len(topic) > 1:
    raise Exception("Invalid topic")
if not topic:
    topic = choice("ACGN")

with open(FILEPATH + "/rating/" + topic + ".txt", "r") as f:
    old_rating = int(f.readline())

REQ_RATINGS_MIN = {
    "E": 0,
    "M": 1400,
    "H": 2000,
    "C": old_rating - 150,
    "F": old_rating - 300,
    "A": 0
}

REQ_RATINGS_MAX = {
    "E": 1399,
    "M": 1999,
    "H": 9999,
    "C": old_rating + 449,
    "F": old_rating + 899,
    "A": 9999
}

req_strign = "Choose rating range (type underlined letter) " \
    + "\033[4mE\033[0masy/\033[4mM\033[0medium/\033[4mH\033[0mard/\033[4mC\033[0mlose/\033[4mF\033[0mar/\033[4mA\033[0mny: "
req_rating = input(req_strign).upper()
req_min = REQ_RATINGS_MIN[req_rating]
req_max = REQ_RATINGS_MAX[req_rating]

show_prob = input("Show problem source? y/N: ") in ["y", "Y", "Yes", "yes"]

prob = choice(os.listdir(FILEPATH + "/problems"))
with open(FILEPATH + "/problems/" + prob + "/rating.txt", "r") as f:
    rating = int(f.readline())
while prob[5] != topic or rating > req_max or rating < req_min:
    prob = choice(os.listdir(FILEPATH + "/problems"))
    with open(FILEPATH + "/problems/" + prob + "/rating.txt", "r") as f:
        rating = int(f.readline())

shutil.copyfile(FILEPATH + "/problems/" + prob + "/statement.html", FILEPATH + "/tmp.html")
webbrowser.open(FILEPATH + "/tmp.html", new=1)

print()

if show_prob:
    print("The problem is \033[1m" + prob + "\033[0m (rating " + str(rating) + ").")

expected = 1.0 / (1.0 + 10.0 ** ((rating - old_rating) / 800.0))

solved = float(input("Solved? Enter 0 or 1: "))

if solved in [0, 1]:
    new_rating = int(old_rating + 120.0 * (solved - expected))

    with open(FILEPATH + "/rating/" + prob[5] + ".txt", "w") as f:
        f.write(str(new_rating) + "\n")
    print("Your rating in " + TOPICS[prob[5]] + " became " + str(old_rating) + " -> \033[1m" + str(new_rating) + "\033[0m.")
    
if not show_prob:
    print("The problem was " + prob + " (rating " + str(rating) + ").")