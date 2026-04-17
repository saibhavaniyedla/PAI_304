# Hidden states
states = ['Interested', 'Neutral', 'Disengaged']

# Observations
observations = ['high', 'medium', 'low']  # activity level

# Initial probabilities
start_prob = {
    'Interested': 0.5,
    'Neutral': 0.3,
    'Disengaged': 0.2
}

# Transition probabilities
transition_prob = {
    'Interested': {'Interested': 0.6, 'Neutral': 0.3, 'Disengaged': 0.1},
    'Neutral': {'Interested': 0.3, 'Neutral': 0.4, 'Disengaged': 0.3},
    'Disengaged': {'Interested': 0.1, 'Neutral': 0.3, 'Disengaged': 0.6}
}

# Emission probabilities
emission_prob = {
    'Interested': {'high': 0.7, 'medium': 0.2, 'low': 0.1},
    'Neutral': {'high': 0.3, 'medium': 0.4, 'low': 0.3},
    'Disengaged': {'high': 0.1, 'medium': 0.3, 'low': 0.6}
}

# Example user activity sequence
obs_seq = ['high', 'medium', 'high']


def forward_algorithm():
    forward = {}

    # Step 1: Initialization
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
        forward = new_forward

    # Step 3: Final probability
    return sum(forward.values())


result = forward_algorithm()
print("User behavior probability:", result)
