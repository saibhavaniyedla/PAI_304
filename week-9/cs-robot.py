
import numpy as np

states = ['Idle', 'Loaded', 'LowBattery']
actions = ['Pick', 'Move', 'Charge']

gamma = 0.9

# Reward function
def reward(state, action):
    if action == 'Pick':
        return 10
    elif action == 'Move':
        return 2
    else:
        return -1

# Transition function
def transition(state, action):
    if state == 'Idle':
        if action == 'Pick': return 'Loaded'
        elif action == 'Move': return 'Idle'
        else: return 'Idle'

    elif state == 'Loaded':
        if action == 'Move': return 'Idle'
        elif action == 'Charge': return 'LowBattery'
        else: return 'Loaded'

    elif state == 'LowBattery':
        if action == 'Charge': return 'Idle'
        else: return 'LowBattery'

def policy_iteration():
    V = {s: 0 for s in states}
    policy = {s: np.random.choice(actions) for s in states}

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for s in states:
                a = policy[s]
                ns = transition(s, a)
                new_val = reward(s, a) + gamma * V[ns]

                delta = max(delta, abs(V[s] - new_val))
                V[s] = new_val

            if delta < 0.01:
                break

        # Policy Improvement
        stable = True
        for s in states:
            old = policy[s]

            best = max(actions, key=lambda a:
                reward(s, a) + gamma * V[transition(s, a)]
            )

            policy[s] = best

            if old != best:
                stable = False

        if stable:
            break

    return policy, V


# Run
policy, V = policy_iteration()

print("Policy Iteration Results:")
for s in states:
    print(f"State: {s}, Action: {policy[s]}, Value: {round(V[s],2)}")