# LunarLanderContinuous-v2 (Open AI gym)

This environment is to evaluate agents for [LunarLanderContinuous-v2](https://gym.openai.com/envs/LunarLanderContinuous-v2/).

## Evaluation

| Evaluator | Description |
| --------- | ----------  |
| avg10     | Average Average reward of 10 consecutive trials. |

## Evaluate locally for development

```
eval.py <path to agent.py>

# example
eval.py models/random/agent.py
```

Will produce evaluation result under `/eval` directory.
