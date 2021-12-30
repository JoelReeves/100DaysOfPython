# Dictionaries

state_capitals = {
    "NJ": "Trenton",
    "PA": "Harrisburg",
    "OR": "Salem",
    "HI": "Honolulu"
}

# getting an item from the dictionary
print(state_capitals["NJ"])

# adding an item to the dictionary
state_capitals["CA"] = "Sacramento"

# iterating through dictionary
for key in state_capitals:
    print(key, '->', state_capitals[key])

for item in state_capitals.items():
    print(item)

for key, value in state_capitals.items():
    print(key, '->', value)

# Grading Program - convert scores to grades
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

def get_student_grade(score):
    if score >= 91 and score <= 100:
        return "Outstanding"
    elif score >= 81 and score <= 90:
        return "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        return "Acceptable"
    else:
        return "Fail"

student_grades = {}

for key, value in student_scores.items():
    student_grades[key] = get_student_grade(value)

print(student_grades)

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris, Dijon", "Lille"],
    "Italy": ["Rome", "Venice", "Florence"]
}

# Dictionary in List
# Writing a program that adds to a travel_log - a List that contains 2 Dictionaries
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_country = {
      "country": country,
      "visits": visits,
      "cities": cities
    }

    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Secret Auction
import os
from art import logo
print(logo)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_highest_bidder(bidders):
    highest_bidder = ""
    highest_bid = 0

    for key, value in bidders.items():
        if (value > highest_bid):
            highest_bidder = key
            highest_bid = value

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

bidders = {}
end_bidding = False

while not end_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid price? $"))
    bidders[name] = price

    continue_game = input("Are there other bidders? y or n: ").lower()

    if continue_game == "y":
        clear_console()
    else:
        end_bidding = True
        get_highest_bidder(bidders)
