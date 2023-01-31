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
    for player_number in range(0, our_object.get_player_count()):
        print(f'ready player {player_number + 1}, aka {our_object.get_player_name(player_number)}')

        our_object.roll_new_five()
        our_object.ask_player_what_to_keep()
    print('good round everyone!')
    break
