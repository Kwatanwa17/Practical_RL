
def get_action_value(mdp, state_values, state, action, gamma):
    """ Computes Q(s,a) as in formula above """

    # YOUR CODE HERE
    # state_values: dictionary of state:index
    Q = 0
    
    for state_prime in mdp.get_next_states(state, action):
        reward = mdp.get_reward(state, action, state_prime)
        Q += mdp.get_transition_prob(state, action, state_prime) * (reward+gamma*state_values[state_prime])
    return Q

