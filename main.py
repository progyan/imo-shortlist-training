import os
import webbrowser
import shutil
from random import choice

topics = {
    "A": "Algebra",
    "C": "Combinatorics",
    "G": "Geometry",
    "N": "Number Theory"
}

topic = input("Choose topic A/C/G/N or leave empty: ")
if topic not in "AGCN" or len(topic) > 1:
    raise Exception("Invalid topic")

show_prob = input("Show problem source? y/N: ") in ["y", "Y", "Yes", "yes"]

prob = choice(os.listdir("./problems"))
while topic and prob[5] != topic:
    prob = choice(os.listdir("./problems"))

if show_prob:
    print("The problem is " + prob)

with open("./problems/" + prob + "/rating.txt", "r") as f:
    rating = int(f.readline())
with open("./rating/" + prob[5] + ".txt", "r") as f:
    old_rating = int(f.readline())
shutil.copyfile("./problems/" + prob + "/statement.html", "tmp.html")
webbrowser.open("tmp.html")

expected = 1.0 / (1.0 + 10.0 ** ((rating - old_rating) / 800.0))

solved = float(input("Solved? Enter 0 or 1: "))

new_rating = int(old_rating + 120.0 * (solved - expected))

with open("./rating/" + prob[5] + ".txt", "w") as f:
    f.write(str(new_rating) + "\n")
if not show_prob:
    print("The problem was " + prob + " (rating " + str(rating) + ").")
print("Your rating in " + topics[prob[5]] + " became " + str(old_rating) + " -> \033[1m" + str(new_rating) + "\033[0m.")