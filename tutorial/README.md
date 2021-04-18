# Tutorial

See [Quickstart](https://luna-ml.github.io/luna/quickstart/index.html) for step by step instruction of the this tutorial project.

## Objective

This is a tutorial project that evaluates models and classify numbers into positive and negative groups.

## Scoring
The model not only needs to classify them correctly but also should aim lower latency when performing `predict()`.

So we are using the following scoring formula

```
score = accuracy / max(avg_latency, 0.01)
```

## How to submit a model?

Create a model directory under 'models'.
And create model.py. The models.py should implement the `predict(n: float)` function that returns 0 when it classifies numbers as a negative, 1 otherwise.
