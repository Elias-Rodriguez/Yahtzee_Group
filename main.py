# we are going to make some of our own modules.
# here are two good sites to skim
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/tutorial/classes.html
# https://www.pythonpool.com/python-class-vs-module/
import Faff_file

our_object = Faff_file.User_interactions()

our_object.testing_or_playing()

our_object.ask_player_count()

our_object.ask_player_names()

while True:
    if our_object.finish:
        print('\nGood round everyone!')
        break
    if our_object.roll_count == 1:
        print(f'ready player {our_object.player_number}, aka {our_object.player_names[our_object.player_number - 1]}')
    our_object.roll_new_five()
    our_object.ask_player_what_to_keep()

