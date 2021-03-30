# Random Agent

The baseline is random agent.
This agent performs random action 0 and 1.

Each evaluation, gym environment and random agent uses different random seed. So you can re-evaluate and see score changes.

## Evaluate locally for development

Prepare python 3.x environment with following dependencies installed

```
pip install gym numpy
```

And then in the project directory (`/cartpole-v1/`), you can run

```
eval.py
```