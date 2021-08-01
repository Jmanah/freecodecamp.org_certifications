import copy
import random
from collections import Counter

# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **colors):
        # converts the dictionary of contents to list of counter elements
        self.contents = list(Counter(colors).elements())
    
    def draw(self, qt):
        # returns all balls if number of balls requested exceeds total number of balls
        if qt > len(self.contents):
            return self.contents
        # returns a randome list of balls removes them from the contents of the hat
        else:
            return [
                self.contents.pop(
                    random.randrange(len(self.contents))
                ) for i in range(qt)
            ]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    # runs expirement for num_expiremnt rounds.
    for i in range(num_experiments):
        # increases count by 1 if the a counter object containing the expected draw is empty after subrtacting a counter object representing one draw.
        if not Counter(
               expected_balls
        ) - Counter(
            copy.deepcopy(hat).draw(num_balls_drawn)
        ):
            count += 1
    #returns probability
    return count/num_experiments