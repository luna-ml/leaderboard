import random

class Agent():
    def __init__(self, **kwargs):
        random.seed()

    def predict(self, state):
        # return 0 or 1 to control cart to left and right
        randomAction = random.randint(0, 1)
        return randomAction
