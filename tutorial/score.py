import sys
import numpy as np

# scorer can read evaluation data from 'eval' directory
# and produces scorefile in 'score' directory.
#
# scorefile includes '<key> <value>' set in each line
# where key is string (w/o space) and value is float number.
#
# In this example we'll write three metrics into the scorefile
#   score: higher score on higher accuracy and low latency
#   accuracy: prediction accuracy
#   avg_latency: average time taken in prediction in seconds

eval_result = "eval/result.csv" # evaluation results from evaluator
score_file = "score/score.txt"  # scorefiles need to be placed under 'score' directory

# read evaluation result
results = []
latency = []
linenum=-1
with open(eval_result, "r") as ins:
    lines = ins.readlines()

    for line in lines:
        linenum = linenum + 1
        if linenum == 0:
            # skip csv header
            continue

        vals = line.split(",")
        
        group = int(vals[1])
        predicted_group = int(vals[2])

        results.append(1.0 if group == predicted_group else 0)
        latency.append(float(vals[3]))

# prepare metrics to write
accuracy = np.round(np.mean(results), 2)
avg_latency = np.round(np.mean(latency), 2)

# calautlate score.
score = int(accuracy / max(avg_latency, 0.01))

# write score file
with open(score_file, "w") as out:
    out.write(f"score {score}\n")
    out.write(f"accuracy {accuracy}\n")
    out.write(f"avg_latency {avg_latency}\n")

# print on the screen as well
print(f"score: {score}")
print(f"accuracy: {accuracy}")
print(f"avg_latency: {avg_latency}")
