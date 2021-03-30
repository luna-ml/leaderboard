import sys, os
import importlib
import gym
import numpy as np

# create gym env
env = gym.make('CartPole-v1')

# number of evaluations to average rewards
num_evaluation = 10

# create eval output dir
os.makedirs("eval", exist_ok=True)

def evaluate():
    agent = Agent()

    observation = env.reset()
    done = False
    total_reward = 0
    while not done:
        # take action from agent
        action = agent.predict(observation)
        observation, reward, done, info = env.step(action)

        # update reward
        total_reward += reward

        if done:
            break

    return total_reward

if __name__ == "__main__":
    # loading agent file
    filename = sys.argv[1]
    exec(compile(open(filename, "rb").read(), filename, 'exec'))

    # evaluate
    all_rewards = []
    for episode in range(num_evaluation):
        reward = evaluate()
        print(f"Episode {episode}. rewards {reward}")
        all_rewards.append(reward)

    # get summary
    avg = np.mean(all_rewards)
    stdev = np.std(all_rewards)

    print("------------")
    print(f"Average reward: {avg}")
    print(f"Std dev: {stdev}")

    # Any files written into 'eval' directory will be
    # stored as a evaluation result and browse on evaluation tab.
    # Also scorer access these files to create score.
    with open("eval/result", "w") as out:
        out.write(f"avg {avg}\n")
        out.write(f"stdev {stdev}\n")
