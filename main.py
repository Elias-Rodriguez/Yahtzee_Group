# we are going to make some of our own modules.
# here are two good sites to skim
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/tutorial/classes.html
# https://www.pythonpool.com/python-class-vs-module/
import Faff_file
from Player import Player
from Dice import Dice

#our_object = Faff_file.User_interactions()

#our_object.ask_player_count()

#our_object.ask_player_names()

#keepPlaying = True

#while keepPlaying:
#    for player_number in range(0, our_object.get_player_count()):
#        print(f'ready player {player_number + 1}, aka {our_object.get_player_name(player_number)}')
#
#        our_object.roll_new_five()
#        our_object.ask_player_what_to_keep()
#    print('good round everyone!')
#

player_count = int(input("How many players would you like?"))


for i in range(0, player_count):

    dice = Dice()
    dice.first_roll()