import random

class Agent():
    def __init__(self):
        random.seed()

    def predict(self, state):
        # return 0 or 1 to control cart to left and right
        angle = state[2]
        if angle > 0:
            return 1
        else:
            return 0
