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
* These are methods used to estimate value functions.

* A *value function* is a function that gives the total expected return of playing an entire policy, given the current state we are in.

* The value function has to be *estimated*  or *predicted* since future rewards of following the policy are not yet known.

* TD methods sample from the environment, and update the value function based on current estimates. They adjust predictions as additional information is collected.

    "Suppose you are on Monday and wish to predict the weather for Saturday, and you have some model that predicts Saturday's weather (i.e. the "Staurday model"), given the weather of each day in the week. We update our model for Saturday's weather based on the weather of each day prior to Saturday."
    
    * It's important to know that when starting out you really don’t have a good starting estimate for the value function, since one does not know which states will leads us to the best solution. You initialize using either random values or all zeros and then make updates to that estimate. Example:
    
        Initial value of each state =  [0,0,0,0,0,0,1] 
   
  * Note that we’ll leave the terminal states alone since those are known (hence the "1" at the end). Remember we’re only trying to predict the values for the non-terminal states since we know the value of the terminal states.
  
  
  **Updating the value function estimate at each step:**  


  [comment]: <> (use URL coding to escape catacters such as '+' =  %2B)
  
   <img src="https://render.githubusercontent.com/render/math?math=\text{Value of state (now)} = \text{Value of State (previous)}%2B\text{correction from new info}">
   
  
  * The *correction* term is called *the TD error* and represents by how much we want to update the last value.
  
     <img src="https://render.githubusercontent.com/render/math?math=\text{TD Error} = \alpha . (\text{Disc Rewards (now)} - \text{Value of State (previous)})">
     
   * alpha (α) term to adjust how much of that error we want to update by.
  
  





