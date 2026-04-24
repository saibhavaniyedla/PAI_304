import numpy as np

# Grid setup
size = 3
goal = (2, 2)
trap = (1, 1)

actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gamma = 0.9

# Move function
def move(state, action):
    i, j = state

    if action == 'UP':
        i -= 1
    elif action == 'DOWN':
        i += 1
    elif action == 'LEFT':
        j -= 1
    elif action == 'RIGHT':
        j += 1

    # Stay inside grid
    i = max(0, min(i, size - 1))
    j = max(0, min(j, size - 1))

    return (i, j)

# ✅ FIXED REWARD FUNCTION
def reward(state):
    if state == goal:
        return 10        # 🔥 Positive reward
    elif state == trap:
        return -10       # 🔥 Negative reward
    else:
        return -1        # Step cost

# VALUE ITERATION
def value_iteration():
    V = {(i, j): 0 for i in range(size) for j in range(size)}

    iteration = 0

    while True:
        iteration += 1
        delta = 0
        new_V = V.copy()

        for state in V:

            # Skip terminal states
            if state == goal or state == trap:
                continue

            values = []

            for action in actions:
                next_state = move(state, action)

                val = reward(next_state) + gamma * V[next_state]
                values.append(val)

            new_V[state] = max(values)

            delta = max(delta, abs(V[state] - new_V[state]))

        V = new_V

        # 🔥 Smaller epsilon for proper convergence
        if delta < 0.0001:
            break

    return V

# RUN
V = value_iteration()

print("Value Iteration Results:")
for state in sorted(V):
    print(f"State: {state}, Value: {round(V[state], 2)}")