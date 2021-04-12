# CartPole-v1 (Open AI gym)

This environment is to solve [CartPole-v1](https://gym.openai.com/envs/CartPole-v1/) from open AI gym.

## Leaderboard Scoring
  Average reward of 30 consecutive trials.

### Evaluate locally for development

```
eval.py <path to agent.py>

# example
eval.py models/random/agent.py
```

Will produce evaluation result under `/eval` directory.

## Environment
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of 0 or 1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center.

[![](https://user-images.githubusercontent.com/1540981/112910447-39967800-90a8-11eb-909e-cb9264a29b62.png)](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/CartPole-v1/original.mp4)

### Observation:

| Num | Observation | Min | Max |
| --- | ----------- | --- | --- |
| 0   | Cart Position | -2.4 | 2.4 |
| 1   | Cart Velocity | -Inf | Inf |
| 2   | Pole Angle | -0.418 rad (-24 deg) | 0.418 rad (24 deg) |
| 3   | Pole Angular Velocity | -Inf | Inf |

See environment source code [here](https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py).

### Actions:

| Num | Action |
| --- | ------ |
| 0   | Push cart to the left |
| 1   | Push cart to the right |

Note: The amount the velocity that is reduced or increased is not fixed; it depends on the angle the pole is pointing. This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it

### Reward:
Reward is 1 for every step taken, including the termination step

### Starting State:
All observations are assigned a uniform random value in [-0.05..0.05]

### Episode Termination:

 - Pole Angle is more than 12 degrees.
 - Cart Position is more than 2.4 (center of the cart reaches the edge of the display).
 - Episode length is greater than 500.

---
This environment corresponds to the version of the cart-pole problem described by Barto, Sutton, and Anderson [[Barto83]](https://gym.openai.com/envs/CartPole-v1/#barto83).

    [Barto83] AG Barto, RS Sutton and CW Anderson, "Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problem", IEEE Transactions on Systems, Man, and Cybernetics, 1983.


This README file is created from https://gym.openai.com/envs/CartPole-v1/.

