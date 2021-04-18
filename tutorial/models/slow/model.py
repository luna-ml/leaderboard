import random, time

# This model returns accurate results but takes longer time.
def predict(n):
    time.sleep(random.uniform(0, 1)/50)
    return 0 if n < 0 else 1
