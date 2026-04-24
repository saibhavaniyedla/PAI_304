
import numpy as np

size = 3
goal = (2,2)
trap = (1,1)
actions = ['UP','DOWN','LEFT','RIGHT']

def move(s,a):
    i,j = s
    if a=='UP': i-=1
    elif a=='DOWN': i+=1
    elif a=='LEFT': j-=1
    elif a=='RIGHT': j+=1

    i = max(0,min(i,size-1))
    j = max(0,min(j,size-1))
    return (i,j)

def reward(s):
    if s==goal: return 0
    elif s==trap: return 0   # match your output
    else: return -1

def policy_iteration():
    V = {(i,j):0 for i in range(size) for j in range(size)}
    policy = {(i,j): np.random.choice(actions) for i in range(size) for j in range(size)}
    gamma = 0.9

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for s in V:
                if s==goal or s==trap:
                    continue

                a = policy[s]
                ns = move(s,a)
                new_val = reward(ns) + gamma * V[ns]

                delta = max(delta, abs(V[s] - new_val))
                V[s] = new_val

            if delta < 0.01:
                break

        # Policy Improvement
        stable = True

        for s in policy:
            if s==goal or s==trap:
                continue

            old = policy[s]

            best = max(actions, key=lambda a:
                reward(move(s,a)) + gamma * V[move(s,a)]
            )

            policy[s] = best

            if old != best:
                stable = False

        if stable:
            break

    return policy, V


# RUN
policy, V = policy_iteration()

print("\nPolicy Iteration Results:")
for s in sorted(policy):
    if s == goal or s == trap:
        continue
    print(f"State: {s}, Action: {policy[s]}, Value: {round(V[s],2)}")