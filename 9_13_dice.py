from random import randint

class Die:
    def __init__(self, sides):
        """Initialize the class attributes."""
        self.sides = sides
    
    def roll_die(self):
        """Roll the die."""
        print(randint(1, self.sides))

dice_1 = Die(6)
dice_1.roll_die()

dice_2 = Die(10)
dice_2.roll_die()

dice_3 = Die(20)
dice_3.roll_die()        