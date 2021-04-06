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
        
        steer = 0 # [-1, +1]
        gas = 0   # [0, +1]
        brake = 0 # [0, +1]

        return [steer, gas, brake]
