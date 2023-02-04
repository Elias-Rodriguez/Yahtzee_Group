# Use pip install tabulate to install module
# These will be the instructions for the Yahtzee game.

from tabulate import tabulate

# assign data for score tables
upper_section = [
    ["Aces(ones)", "Total of Aces only"],
    ["Twos", "Total of Twos only"],
    ["Threes", "Total of Threes only"],
      ["Fours", "Total of Fours only"],
    ["Fives" , "Total of Fives only"],
    ["Sixes" , "Total of Sixes only"]
]

lower_section = [
    ["3 of a kind", "Total of all 5 dice"],
    ["4 of a kind", "Total of all 5 dice"],
    ["Full House", "25 Points"],
      ["Small Straight", "30 Points"],
    ["Large Straight" , "40 Points"],
    ["YAHTZEE" , "50 Points"],
    ["Chance", "Total of all 5 dice"]
]

# create header
head_one = ["Upper Section", "What to Score"]
head_two  =["Lower Section", "What to Score"]
 
# Instructions that will be printed for the player

how_to_play = '''
On each turn, roll the dice up to 3 times to get the highest scoring combination for one of the thirteen categories.
After you finish rolling you must place a score or a zero in one of the 13 category boxes on your score card.
The game ends when all the players have filled their 13 boxes. Scored are totaled, including any bonus points.
The player with the highest total wins.
'''

score_combinations = '''
There will be two sections for scoring.
The upper section which is composed of Aces(ones),
Twos, Threes, Fours, Fives, and Sixes will allow for the
user to take down the sum of the dice that match one of the categories.
The lower section will be composed of the categories 3 of a kind,
4 of a kind, full house, small straight, large straight, YAHTZEE, and chance.
The chart below shows how each is scored.
'''

# Display the tables

upper_section_scores = (tabulate(upper_section, headers=head_one, tablefmt="grid"))

lower_section_scores = (tabulate(lower_section, headers=head_two, tablefmt="grid"))

# Variable for all the instructions put together.
full_instructions = how_to_play + score_combinations + "\n" + upper_section_scores + "\n\n" + lower_section_scores


