import random

class Agent():
    def __init__(self):
        random.seed()

    def predict(self, state):
        # eval.py will call with method to evaluate in the given environment.
        
        steer = random.uniform(-1, 1) # [-1, +1]
        gas = random.uniform(0.5, 1)   # [0, +1]
        brake = random.uniform(0, 0.5) # [0, +1]

        return [steer, gas, brake]
