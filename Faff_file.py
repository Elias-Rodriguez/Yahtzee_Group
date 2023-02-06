import random
import instructions
import Zybook_Poker_Dice

class User_interactions:

    def __init__(self):
        self.data = []
        self.player_count = 0
        self.dice_chance = 0
        self.player_number = 1
        self.player_names = []
        self.testing = True
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 1
        self.next_person = False
        self.finish = False
        self.keep_dice = False
        self.keep_dice_number_array = []
        self.score = 0
        self.score_list = []

    def testing_or_playing(self):
        print('Hello, Welcome to Yahtzee.')
        print(instructions.full_instructions)
        user_response = input('1 to play, anything else to test: ')
        if '1' != user_response:
            print('Entering testing mode.')
            self.testing = True
        else:
            # print('Welcome to the game.')
            self.testing = False

    def ask_player_what_to_keep(self):
        self.dice_chance += 1
        if self.dice_chance < 3:
            user_selection = input('\na. Reroll all b. Choose dice number to reroll c. Finish')
            if user_selection == 'b':
                keep_dice_number = input('Which dice tou want to reroll? (Use space to separate the numbers)')
                self.keep_dice_number_array = keep_dice_number.split()
                self.keep_dice = True
            elif user_selection == 'c':
                self.turn_next_person()
        elif self.dice_chance == 3:
            self.turn_next_person()

    def turn_next_person(self):
        self.display_score()
        if self.player_number == self.player_count:
            self.finish = True
        else:
            print('\n--------next person------------')
            self.next_person = True
            self.dice_chance = 0
            self.player_number += 1
            self.roll_count = 1
            self.score = 0

    def ask_player_count(self):
        player_count = input('hello, how many players would you like?')
        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('you don\'t want to play.')
        elif 1 == self.player_count:
            print('you want one player ')
        elif 2 <= self.player_count:
            print(f'you want {self.player_count} players.')

    def ask_player_names(self):
        for item in range(0, self.player_count):
            name = input(f'Player {item + 1}, please enter your name: ')
            self.player_names.append(name)
        print('for this game, we have the following player:')
        print(self.player_names)

    def roll_new_five(self):
        if not self.keep_dice:
            self.roll_count += 1
            print('New roll.')
            for die in range(0, len(self.dice_on_table)):
                self.dice_on_table[die] = random.randint(1, 6)

        else:
            for index, ch in enumerate(self.keep_dice_number_array):
                self.keep_dice_number_array[index] = int(ch) - 1
            for index in self.keep_dice_number_array:
                self.dice_on_table[index] = random.randint(1, 6)

        print('here are the dice on the table.')
        print('\nDICE NUMBER\t1\t2\t3\t4\t5')
        print('DICE VALUE ', end='')
        for die in self.dice_on_table:
            print(f'\t{die}', end='')
        print()

    def display_score(self):
        number_valid = False
        while not number_valid:
            number_to_score = int(input('\nWhat number do you want to score?'))
            if number_to_score not in self.score_list:
                number_valid = True
            else:
                print('You have already scored that number.')
                print('You have scored numbers ', end='')
                for num in self.score_list:
                    print(str(num) + '', end='')
                print()

        self.score_list.append(number_to_score)
        for d in self.dice_on_table:
            if d == number_to_score:
                self.score += d
        print('Your score is ' + str(self.score))

    def roll_remaining(self, dice_on_table):
        if self.roll_count < 3:
            import random
            self.roll_count += 1
            print('New roll.')
            for die in range(0, len(self.dice_on_table)):
                self.dice_on_table[die] = random.randint(1, 6)
            print('here are the dice on the table.')
            print('\nDICE NUMBER\t1\t2\t3\t4\t5')
            print('DICE VALUE,', end='')
            for die in self.dice_on_table:
                print(f'\t{die}', end='')
            print()
            if self.roll_count < 3:
                self.ask_player_what_to_keep()

    def get_current_score(self, dice, score):
        score = 0
        for die in self.dice_to_keep:
            score += die

        print("Your current dice add up to: {}".format(score))

    def check_for_upper(self, dice_to_keep):
        check_dice = Zybook_Poker_Dice.find_high_score(self.data)
        print(check_dice)

