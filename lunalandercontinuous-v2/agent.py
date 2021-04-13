# Agent Template.
#
# Copy this agent.py in your model dir (e.g. models/mymodel/agent.py)
# and implement predict(state) method to start

class Agent():
    def __init__(self):
        # initialize anything you need.
        # e.g. load pre-trained model
        pass


    def predict(self, state):
        # eval.py will call with method to evaluate in the given environment.

        # horizontal_coordinate = state[0]
        # vertical_coordinate = state[1]
        # horizontal_speed = state[2]
        # vertical_speed = state[3]
        # angle = state[4]
        # angular_speed = state[5]
        # first_leg_contact = state[6]
        # second_leg_contact = state[7]

        side_engine = 0
        main_engine = 0

        return [side_engine, main_engine]
