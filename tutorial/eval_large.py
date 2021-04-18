import sys, random, time

filename = sys.argv[1]
exec(compile(open(filename, "rb").read(), filename, 'exec'))

num_sample = 100 # larger number of sample compare to eval.py
results = []
for i in range(num_sample):
    n = random.uniform(-10, 10) # wider range of input
    group = 0 if n < 0 else 1

    start = time.time()
    predicted_group = predict(n)
    latency = time.time() - start

    results.append((n, group, predicted_group, latency))
    print(f"{n}, group={group}, predicted_group={predicted_group}, latency={latency}sec")

with open("eval/result.csv", "w") as out:
    out.write("number,group,predicted_group,latency\n")
    for r in results:
        out.write(f"{r[0]},{r[1]},{r[2]},{r[3]}\n")
