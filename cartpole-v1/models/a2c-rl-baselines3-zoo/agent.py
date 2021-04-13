import pathlib
from stable_baselines3 import A2C

class Agent():
    def __init__(self, **kwargs):
        self.model = A2C.load(f"""{kwargs.get("path")}/CartPole-v1.zip""")

    def predict(self, state):
        action, _ = self.model.predict(state, deterministic=False)
        return action
