import random

def roll_dice():
    return random.randint(1, 6)

def yahtzee():
    rolls = [roll_dice(), roll_dice(), roll_dice(), roll_dice(), roll_dice()]
    print("Rolls:", rolls)
    keep = input("Enter dice to keep (e.g. '1 2 4') or press enter to take your score: ")
    keep = [int(x) - 1 for x in keep.split()] if keep else []
    rolls = [rolls[i] if i in keep else roll_dice() for i in range(5)]
    print("Rolls:", rolls)
    
    counts = [rolls.count(x) for x in range(1, 7)]
    
    if 5 in counts:
        print("Yahtzee!")
        return 11
    elif 4 in counts:
        print("Four of a kind!")
        return 7
    elif 3 in counts and 2 in counts:
        print("Full house!")
        return 8
    elif 3 in counts:
        print("Three of a kind.")
        return 6
    elif any(count >= 2 for count in counts):
        print("Pair.")
        return 5
    else:
        is_straight = any(count == 1 for count in counts) and (counts[0] == 1 or counts[-1] == 1)
        if is_straight:
            print("Straight.")
            return 10
        else:
            print("Sorry, try again.")
            return 0

def play_yahtzee():
    scorecard = [0] * 13
    filled_spaces = [False] * 13
    total_score = 0
    while False in filled_spaces:
        print("Scorecard:")
        print("---------------------------------------------------")
        print("| Ones:", scorecard[0], "| Twos:", scorecard[1], "| Threes:", scorecard[2], "| Fours:", scorecard[3], "| Fives:", scorecard[4], "| Sixes:", scorecard[5], "|")
        print("| Three of a kind:", scorecard[6], "| Four of a kind:", scorecard[7], "| Full House:", scorecard[8], "| Small Straight:", scorecard[9], "| Large Straight:", scorecard[10], "| Yahtzee:", scorecard[11], "| Chance:", scorecard[12], "|")
        print("---------------------------------------------------")
        yahtzee_score = yahtzee()
        if yahtzee_score == 0:
            continue
        category = None
        while category not in range(1, 14):
            category = int(input("Enter category to place score (1-13): "))
        if not filled_spaces[category - 1]:
            scorecard[category - 1] = yahtzee_score
            filled_spaces[category - 1] = True
            total_score += yahtzee_score
        else:
            print("Category already filled, please choose another.")
    print("Game over! Final score:", total_score)

play_yahtzee()
