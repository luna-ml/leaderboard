import random
import numpy as np

class Agent():
    def __init__(self, **kwargs):
        random.seed()

    def predict(self, s):
        # this heuristic algorithm came from https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py

        angle_targ = s[0]*0.5 + s[2]*1.0         # angle should point towards center
        if angle_targ > 0.4: angle_targ = 0.4    # more than 0.4 radians (22 degrees) is bad
        if angle_targ < -0.4: angle_targ = -0.4
        hover_targ = 0.55*np.abs(s[0])           # target y should be proportional to horizontal offset

        angle_todo = (angle_targ - s[4]) * 0.5 - (s[5])*1.0
        hover_todo = (hover_targ - s[1])*0.5 - (s[3])*0.5

        if s[6] or s[7]:  # legs have contact
            angle_todo = 0
            hover_todo = -(s[3])*0.5  # override to reduce fall speed, that's all we need after contact

        if env.continuous:
            a = np.array([hover_todo*20 - 1, -angle_todo*20])
            a = np.clip(a, -1, +1)
        else:
            a = 0
            if hover_todo > np.abs(angle_todo) and hover_todo > 0.05: a = 2
            elif angle_todo < -0.05: a = 3
            elif angle_todo > +0.05: a = 1
        return a
