import gym

env = gym.make('BreakoutNoFrameskip-v4')
o = env.reset()
while True:
    env.render()
    # take a random action
    a = env.action_space.sample()
    o, r, done, info = env.step(a)
    if done:
        break
env.close() # close and clean up