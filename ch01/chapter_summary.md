# Key takeaways from Chapter 1

## 1.1. Reinforcement Learning definition

**Definition** Learning by itself how to map situations to actions so as to maximize a numerical signal reward.

**Difference with supervised learning** 

* Supervised learning involves learning from a training set of labeled examples provided by a knowledgeable external supervisor.

* In RL, the agents are able to learn form its own experience.

**Difference with unsupervised learning**
* Unsupervised learning finds structure hidden in colletions of unlabeled data, while RL does not rely on examples of correct behaviour, instead it maximizes rewards signals instread of trying to find a hidden structure.

**The trade off between exploration and exploitation**

**- Exploration:** the agent explores new actions that can potentially lead to maximize the reward

**- Exploitation:** the agent prefers actions that it has tried in the past and found to be efficient in producing reward.


## 1.2. Examples
blah blah

## 1.3 The 4 elements of RL: policy, reward signal, value function, model of environment.

### Policy

* Mapping from states to action.
* The optimal policy is what the agent seraches for. It is defined as the policy that maximizes the reward
* In general, policies are *stochastic*, they just specify the probabilities for each action.

### Reward signal

* Is the feedback given by the environment after each action from the agent.
* The agent's objective is to maximize the total reward.
* Rewards signals may be stochastic functions of the state of the environment and the actions taken.

### Value function

* Specifies what is a good policy in the *long run*
* The value of a state is the total amount of reward an agent can expect to accumulate over the future, starting from that state.
* Whereas rewards determine the immediate value of the state, the value function indicates the long-term desirability of the states.
* It looks at the long run as it takes into account the states that are likely to be followed and the rewards availablein those states.

### Model of environment

* A model that mimics the behaviour of the true environment, allowing inferences on how the environment will behave.


## 1.4 Limitations and scope
blah blah

## 1.5 Example: Tic-tac-toe

### Difference between evolutionary methods and methods that learn value functions

* **Evolutionary methods** - to evaluate a policy, it holds the policy fixed and plays many games against the opponent (or simulates many games using a model of the opponent)

    The *frequency of wins* gives an unbiased estimate of the prob of winning with that policy. Which is used to compare policies.

    Each policy change is done after many games.

    What happens *during* the game is irrelevant

* **Value function methods** allow individual states to be evaluated and updated as we play.

### Temporal difference learning method
These are methods used to estimate value functions (the expected return of a policy given a current state).



