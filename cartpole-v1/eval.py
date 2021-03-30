import sys, os
import importlib
import gym
from gym.wrappers import Monitor
import numpy as np
import matplotlib.pyplot as plt

# create gym env
# env = Monitor(gym.make('CartPole-v1'), "./eval/", video_callable=lambda episode_id: True, force=True)
env = gym.make('CartPole-v1')

# number of evaluations to average rewards
num_evaluation = 100

# max score in cartpole-v1 env
max_score = 500


# create eval output dir
os.makedirs("eval", exist_ok=True)

def plot_reward(values, title=''):
    # Define the figure
    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
    f.suptitle(title)
    ax[0].plot(values, label='score per run')
    ax[0].axhline(max_score, c='red', ls='--', label='goal')
    ax[0].set_xlabel('Episodes')
    ax[0].set_ylabel('Reward')
    x = range(len(values))
    ax[0].legend()

    # Plot the histogram of results
    ax[1].hist(values[-50:])
    ax[1].axvline(max_score, c='red', ls='--', label='goal')
    ax[1].set_xlabel(f"Score")
    ax[1].set_ylabel('Frequency')
    ax[1].legend()

    # plt.show()
    plt.draw()
    f.savefig('eval/plot.png', dpi=100)

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
    with open("eval/result.txt", "w") as out:
        out.write(f"score {avg}\n")
        out.write(f"stdev {stdev}\n")

    # create plot
    plot_reward(all_rewards)
