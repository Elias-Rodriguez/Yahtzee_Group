import instructions

inst = instructions


class User_interactions:

    def __init__(self):
        self.data = []
        self.player_count = 1
        self.player_names = []
        self.testing = True
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 0
        self.numb = 0
        self.dice_to_keep = []
        self.score = 0

    def testing_or_playing(self):
        user_response = input('''
        Hello, Welcome to Yahtzee.
        Type Start to play or Help for instruction.
        ''')
        if 'Start' != user_response:
            print(inst.full_instructions)
            self.testing_or_playing()
        else:
            print('''
        Welcome to the game!''', end="")
            self.testing = False

    def ask_player_what_to_keep(self):
        # Commented out The following lines to irrelevancy
        """
        print('which dice do you want to keep?')
        print('enter the dice number or numbers to keep')
        print('just press enter to re-roll all dice.')

        if self.testing:
            print('This code needs to be completed still.')
        else:
            user_selection = input('which dice do you want to keep?')
        """
        user_selection = input('''
        Would you like to keep any dice? 
        ''')

        if "" == user_selection:
            '''
        Invalid Selection'''
            self.ask_player_what_to_keep()
        elif "yes" == user_selection:
            if len(user_selection) > 0:
                user_selection = input('''
        Which dice would you like to keep?
        Separate each selection with a comma and hit enter once done.
        ''')
            user_choices = user_selection.split(",")
            user_choices = [int(float(i)) for i in user_choices]
            print('You selected to keep the following dice {}'.format(user_choices))
            for num in user_choices:
                self.dice_to_keep.append(self.dice_on_table[num-1])
                self.data.append(self.dice_on_table[num-1])
                self.dice_on_table.remove(self.dice_on_table[num-1])

        self.get_current_score(self.data, self.score)
        self.roll_remaining(self.dice_on_table)




    def ask_player_count(self):

        if self.testing:
            player_count = 3
        else:
            player_count = input('''
        How many players would you like?''')

        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('''
        You don\'t want to play.''')
        elif 1 == self.player_count:
            print('''
        You want one player ''')
        elif 2 <= self.player_count:
            print(f'''
        You want {self.player_count} players.''')

    def get_player_count(self):
        return self.player_count

    def ask_player_names(self):

        if self.testing:
            self.player_names.append('bob')
            self.player_names.append('susan')
            self.player_names.append('link')
        else:
            for item in range(self.numb, self.player_count):
                name = input(f'''
        Player {self.numb + 1}, please enter your name: ''')
                if "" == name:
                    print('''
        Invalid Entry. Please try again.''')
                    self.ask_player_names()

                else:
                    self.player_names.append(name)
                    self.numb += 1

        print(f'''
        for this game, we have the following players:
        {self.player_names}
        ''')

    def get_player_name(self, player_number):
        return self.player_names[player_number]

    def roll_new_five(self):
        import random
        self.roll_count = 1
        print('''
        New roll.''')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1, 6)
        print('''
        Here are the dice on the table.''')
        print('''
        DICE NUMBER: \t1\t2\t3\t4\t5''')
        print('''
        DICE VALUE:''', end=' ')
        for die in self.dice_on_table:
            print(f'\t{die}', end='')
        print()

    def roll_remaining(self, dice_on_table):
        if self.roll_count < 3:
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
            if self.roll_count < 3:
                self.ask_player_what_to_keep()
        


    def get_current_score(self, dice, score):
        for die in self.data:
            self.score += die

        print("Your current dice add up to: {}".format(self.score))
