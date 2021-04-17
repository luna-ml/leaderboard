# This evaluator will generate 10 random number and
import sys, random, time

# write evaluation results into /workspace/eval/result.csv
#
# import predict() function by executing given .py file
# The function takes a number from argument and
#    return 0 when the number is negative
#           1 when otherwise
filename = sys.argv[1]
exec(compile(open(filename, "rb").read(), filename, 'exec'))

num_sample = 10
results = []
for i in range(num_sample):
    # in this example, we generate random data to evaluate.
    # In a real use case, you will load your evaluation data set
    # or set up simmulation environment here.
    n = random.uniform(-1, 1)
    group = 0 if n < 0 else 1

    # run predict() function.
    start = time.time()
    predicted_group = predict(n)
    latency = time.time() - start

    results.append((n, group, predicted_group, latency))


# Write an evaluation result data.
# Evaluation results can be anything from text, image, to video.
# Only requirement is that they need to be placed under the 'eval' directory.
# in this example, we'll write a csv file with
# number,group,predicted_group,latency in each line
with open("eval/result.csv", "w") as out:
    out.write("number,group,predicted_group,latency\n")
    for r in results:
        out.write(f"{r[0]},{r[1]},{r[2]},{r[3]}\n")
