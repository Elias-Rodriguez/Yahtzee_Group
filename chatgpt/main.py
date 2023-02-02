import random

def roll_dice():
    return random.randint(1, 6)

def yahtzee():
    rolls = [roll_dice(), roll_dice(), roll_dice(), roll_dice(), roll_dice()]
    print("Rolls:", rolls)
    keep = input("Enter dice to keep (e.g. '1 2 4'): ")
    keep = [int(x) - 1 for x in keep.split()] if keep else []
    rolls = [rolls[i] if i in keep else roll_dice() for i in range(5)]
    print("Rolls:", rolls)
    
    counts = [rolls.count(x) for x in range(1, 7)]
    
    if 5 in counts:
        print("Yahtzee!")
        return 50
    elif 4 in counts:
        print("Four of a kind!")
        return sum(rolls)
    elif 3 in counts and 2 in counts:
        print("Full house!")
        return 25
    elif 3 in counts:
        print("Three of a kind.")
        return sum(rolls)
    elif any(count >= 2 for count in counts):
        print("Pair.")
        return sum(x * 2 for x in rolls if rolls.count(x) >= 2)
    else:
        is_straight = any(count == 1 for count in counts) and (counts[0] == 1 or counts[-1] == 1)
        if is_straight:
            print("Straight.")
            return 40
        else:
            print("Sorry, try again.")
            return 0

def play_yahtzee():
    scorecard = [0] * 13
    filled_spaces = 0
    total_score = 0
    while filled_spaces < 13:
        print("Scorecard:")
        print("---------------------------------------------------")
        print("| Ones:", scorecard[0], "| Twos:", scorecard[1], "| Threes:", scorecard[2], "| Fours:", scorecard[3], "| Fives:", scorecard[4], "| Sixes:", scorecard[5], "|")
        print("| Three of a kind:", scorecard[6], "| Four of a kind:", scorecard[7], "| Full House:", scorecard[8], "| Small Straight:", scorecard[9], "| Large Straight:", scorecard[10], "| Yahtzee:", scorecard[11], "| Chance:", scorecard[12], "|")
        print("---------------------------------------------------")
        yahtzee_score = yahtzee()
        scorecard[filled_spaces] = yahtzee_score
        total_score += yahtzee_score
        filled_spaces += 1
        print("Score:", yahtzee_score)
        print("Total score:", total_score)
        print("---------------------------------------------------")

play_yahtzee()
