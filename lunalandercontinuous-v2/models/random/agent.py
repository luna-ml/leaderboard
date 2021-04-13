import random

class Agent():
    def __init__(self, **kwargs):
        random.seed()

    def predict(self, state):
        # eval.py will call with method to evaluate in the given environment.

        horizontal_coordinate = state[0]
        vertical_coordinate = state[1]
        horizontal_speed = state[2]
        vertical_speed = state[3]
        angle = state[4]
        angular_speed = state[5]
        first_leg_contact = state[6]
        second_leg_contact = state[7]

        side_engine = random.uniform(-1, 1)
        main_engine = random.uniform(0.5, 1)

        return [side_engine, main_engine]
