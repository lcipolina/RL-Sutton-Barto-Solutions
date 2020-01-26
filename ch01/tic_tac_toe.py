# LCK's python code for Sutton and Barto's RL book ch01
# Implementation of tic-tac-toe using Q leaning

#####################################################
# PRELIMS:
# Q-learning works for Tic-tac-toe since the total number of states is finite and discrete. 
# It works by developing a table of values for each state representing the highest future reward. 
# We want to maximize the reward by giving the agent reward for each step closer to the win condition or tie condition 
# whereas the reward function is defined as Rt = rt + γrt+1 + γ 2 rt+2
# the state is the positions of the naughts and crosses on the board. It represents the visible characteristics of the environment: your board.
# The agent will use a combination of stochastic (random) actions and greedy-epsilon (best) actions to explore and exploit the board environment.

######################################################
# STRATEGY:
# Explore the space - MC simulation
# Attach value based on distance from goal state
# Q(s) is were we store what we know about each state. This is what we are trying to learn, we want to assing Q(.) the correct value.
# Tabular Q-learning: We create a table consisting of all possible states on one axis and all possible actions on another axis.
  # Each cell in this table has a Q-value. 
  # The Q-value tells us whether it is a good idea or not to take the corresponding action from the current state.
  # A high Q-value is good and a low Q-value is bad. Rewards increase the associated Q-values. 
  # We can also assign a negative reward as a punishment for an action, which reduces the Q-value, and therefore discourages taking that action from that particular state in the future.


