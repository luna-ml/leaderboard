import random

# This model returns random predictions.
# In the real world use case, this might be
# loading a pre-trained model in your favorite ML framework
# and returning prediction results from it.
def predict(n):
    return random.randint(0, 1)
