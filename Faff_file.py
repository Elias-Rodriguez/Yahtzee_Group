class User_interactions:


    def __init__(self):
        self.data = []
        self.player_count = 0
        self.player_names = []
        self.testing = False
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.dice_to_keep = []
        self.roll_count = 0

    def ask_player_what_to_keep(self):
        user_selection = input('which dice do you want to keep?')
        if len(user_selection) > 0:
            user_choices = user_selection.split(" ")
            user_choices = [int(float(i)) for i in user_choices]
            print(user_choices)
            for num in user_choices:
                self.dice_to_keep.append(self.dice_on_table[num-1])
        self.get_current_score(self.dice_to_keep)

                


    def ask_player_count(self):
        if self.testing:
            player_count = 3
        else:
            player_count = input('hello, how many players would you like?')

        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('you don\'t want to play.')
        elif 1 == self.player_count:
            print('you want one player ')
        elif 2 <= self.player_count:
            print(f'you want {self.player_count} players.')

    def get_player_count(self):
        return self.player_count

    def ask_player_names(self):
        if self.testing:
            self.player_names.append('bob')
            self.player_names.append('susan')
            self.player_names.append('link')
        else:
            for item in range(0,self.player_count):
                name = input(f'Player {item+1}, please enter your name: ')
                self.player_names.append(name)

        print('for this game, we have the following player:')
        print(self.player_names)

    def get_player_name(self, player_number):
        return self.player_names[player_number]


    def roll_new_five(self):
        import random
        self.roll_count = 1
        print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1,6)
        print('here are the dice on the table.')
        print('\nDICE NUMBER\t1\t2\t3\t4\t5')
        print('DICE VALUE,', end = '')
        for die in self.dice_on_table:
            print(f'\t{die}', end = '')
        print()

    def roll_remaining(self, dice_left):
        import random
        self.roll_count +=1
        print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1,6)
        print('here are the dice on the table.')
        print('\nDICE NUMBER\t1\t2\t3\t4\t5')
        print('DICE VALUE,', end = '')
        for die in self.dice_on_table:
            print(f'\t{die}', end = '')
        print()

    def get_current_score(self, dice_to_keep):
        score = 0
        for dice in self.dice_to_keep:
            score += dice

        print("Your current dice add up to: {}".format(score))

    def check_for_upper(self, dice_to_keep):
        import Zybook_Poker_Dice
        check_dice = Zybook_Poker_Dice.find_high_score(self.dice_to_keep)
        print(check_dice)
    

    