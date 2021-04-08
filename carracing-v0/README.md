# CarRacing-v0 (Open AI gym)

This environment is to solve [CarRacing-v0](https://gym.openai.com/envs/CarRacing-v0/) from open AI gym.

## Leaderboard Scoring
  Average reward of 10 consecutive trials.

### Evaluate locally for development

```
eval.py <path to agent.py>

# example
eval.py models/random/agent.py
```

Will produce evaluation result under `/eval` directory.

## Environment
Easiest continuous control task to learn from pixels, a top-down racing environment. Discreet control is reasonable in this environment as well, on/off discretisation is fine. State consists of 96x96 pixels. Reward is -0.1 every frame and +1000/N for every track tile visited, where N is the total number of tiles in track. For example, if you have finished in 732 frames, your reward is 1000 - 0.1*732 = 926.8 points. Episode finishes when all tiles are visited. Some indicators shown at the bottom of the window and the state RGB buffer. From left to right: true speed, four ABS sensors, steering wheel position, gyroscope.

[![](https://user-images.githubusercontent.com/1540981/113469556-43e7a780-9403-11eb-955d-5ac32c126f2c.png)](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/CarRacing-v0/original.mp4)

### Observation:

See environment source code [here](https://github.com/openai/gym/blob/master/gym/envs/box2d/car_racing.py).

### Actions:

|index | Action | Value |
| --- | --- | ------ |
| 0 | Steer | Between -1 and +1 |
| 1 | Gas | Between 0 and 1 |
| 2 | Brake | Between 0 and 1 |


This README file is created from https://gym.openai.com/envs/CarRacing-v0/.
