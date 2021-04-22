import random
from CarRacingDQNAgent import CarRacingDQNAgent
from common_functions import process_state_image
from common_functions import generate_state_frame_stack_from_queue
from collections import deque

# the agent code is from https://github.com/andywu0913/OpenAI-GYM-CarRacing-DQN/blob/master/play_car_racing_by_the_model.py
class Agent():
    def __init__(self):
        self.agent = CarRacingDQNAgent(epsilon=0)
        self.agent.load("dqn/save/trial_500.h5")
        self._init_state = []
        self._total_reward = 0
        self._time_frame_counter = 1


    def predict(self, state):
        if 0 == len(self._init_state):
            self._init_state = process_state_image(state)
            self._state_frame_stack_queue = deque([self._init_state]*self.agent.frame_stack_num, maxlen=self.agent.frame_stack_num)
        else:
            next_state = process_state_image(state)
            self._state_frame_stack_queue.append(next_state)
        current_state_frame_stack = generate_state_frame_stack_from_queue(self._state_frame_stack_queue)
        action = self.agent.act(current_state_frame_stack)
        return action
