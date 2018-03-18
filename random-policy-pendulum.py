import gym
env = gym.make('BipedalWalker-v2')

print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space)
print(env.action_space.high)
print(env.action_space.low)

score = 0.0

for i_episode in range(1):
    observation = env.reset()
    score = 0.0
    for t in range(1000):
        # env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # score += reward
        print( reward )
        if done:
            print("Episode finished after {} timesteps, Reward=".format(t + 1),score)
            break
