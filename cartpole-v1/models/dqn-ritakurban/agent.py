import pathlib
import keras
import numpy as np

class Agent():
    def __init__(self, **kwargs):
        self.model = self.load_model(f"""{kwargs.get("path")}/pretrained""")

    def load_model(self, path):
        """Load pretrained model"""
        model = keras.models.load_model(path)
        return model

    def predict(self, state):
        # return 0 or 1 to control cart to left and right
        q_values = self.model.predict(np.array([state]))
        return np.argmax(q_values[0])
