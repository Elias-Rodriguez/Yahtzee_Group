from Player import Player

class Dice:


    def first_roll(self):
        import random as rand
        self.current_player = Player()
        self.current_player.rolls += 1

        for i in range(0,5):
            self.current_player.dice_on_table[i] = rand.randint(1,6)
            print(self.current_player.dice_on_table[i])
        
