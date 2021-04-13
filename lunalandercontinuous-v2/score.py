import sys
import numpy as np

if __name__ == "__main__":
    eval_result = sys.argv[1]  # path to result.txt from eval.py. (e.g. /workspace/eval/result.txt)
    score_file = sys.argv[2]  # path to score file to write. (e.g. /workspace/score/score.txt)

    # read evaluation result
    all_rewards = []
    with open(eval_result, "r") as ins:
        lines = ins.readlines()

        for line in lines:
            reward = float(line.split(" ")[1])
            all_rewards.append(reward)

    # score
    avg = np.round(np.mean(all_rewards), 2)
    stdev = np.round(np.std(all_rewards), 2)

    # write score file
    with open(score_file, "w") as out:
        out.write(f"score {avg}\n")
        out.write(f"stdev {stdev}\n")

    print(f"Score (Average reward): {avg}")
    print(f"Std dev: {stdev}")
