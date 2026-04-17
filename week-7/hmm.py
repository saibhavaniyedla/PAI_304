# States
states = ['Rainy', 'Sunny']

# Observations
observations = ['walk', 'shop', 'clean']

# Initial probabilities
start_prob = {'Rainy': 0.6, 'Sunny': 0.4}

# Transition probabilities
transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

# Emission probabilities
emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

# Observation sequence
obs_seq = ['walk', 'shop', 'clean']


def forward_algorithm():
    # Step 1: Initialization
    forward = {}
    for state in states:
        forward[state] = start_prob[state] * emission_prob[state][obs_seq[0]]

    # Step 2: Recursion
    for t in range(1, len(obs_seq)):
        new_forward = {}
        for curr_state in states:
            total = 0
            for prev_state in states:
                total += forward[prev_state] * transition_prob[prev_state][curr_state]
            
            new_forward[curr_state] = total * emission_prob[curr_state][obs_seq[t]]
        
        forward = new_forward  # move to next step

    # Step 3: Final probability
    return sum(forward.values())


# Run
result = forward_algorithm()
print("Final Probability:", result)
