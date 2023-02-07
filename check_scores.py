class check_scores:

    def __init__(self, dice):
        self.dice = dice

    def check_yahtzee(self, dice):
        
        if len(set(dice)) == 1:
            print("Yahtzee!")


    def check_full_house(self, dice):
        dice.sort()

        if (len(set(dice))) == 2:
            if (dice[0] == dice[2] and dice[3] == dice[4]):
                print("Full House!")
            elif (dice[2] == dice[4] and dice[0] == dice[1]):
                print("Full House!")

    def check_large_straight(self, dice):
        dice.sort()

        if len(set(dice)) == 5 and dice[4] == 5 and dice[0] == 1:
            print("Large Straight!")
        elif len(set(dice)) == 5 and dice[4] == 6 and dice[0] == 2:
            print("Large Straight!")
        
        
        

    def check_small_straight(self, dice):
        dice.sort()
        
        if len(set(dice)) >= 4:
            if (dice[0] == 1 and dice[3] == 4 or dice[4] == 6 and dice [1] == 2):
                print("Small Straight!")

    def check_four_of_a_kind(self, dice):
        dice.sort()

        if dice[0] == dice[3] or dice[1] == dice[4]:
            print("Four of a kind!")

    def check_three_of_a_kind(self, dice):
        dice.sort()

        if dice[0] == dice[2] or dice[1] == dice[3] or dice[2] == dice[4]:
            print("Three of a kind!")


    def check_all(self, dice):
        self.check_yahtzee(dice)
        self.check_full_house(dice)
        self.check_large_straight(dice)
        self.check_small_straight(dice)
        self.check_four_of_a_kind(dice)
        self.check_three_of_a_kind(dice)