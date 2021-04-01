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
        # This function should return action 0 or 1 to move cart left or right
        action = 1
        return action


    def metrics(self) -> dict:
        # Metrics to export with evaluation result.
        # You can return additional informations such as hyper parameters of the model.
        #
        # key: str, name of metric
        # value: float
        return {}
