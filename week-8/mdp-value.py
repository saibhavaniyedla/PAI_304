
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

def value_iteration():
    V = {(i,j):0 for i in range(size) for j in range(size)}
    gamma = 0.9

    while True:
        delta = 0
        new_V = V.copy()

        for s in V:
            if s==goal or s==trap:
                continue

            values = []
            for a in actions:
                ns = move(s,a)
                values.append(reward(ns) + gamma * V[ns])

            new_V[s] = max(values)
            delta = max(delta, abs(V[s] - new_V[s]))

        V = new_V

        if delta < 0.01:
            break

    return V


# RUN
V = value_iteration()

print("Value Iteration Results:")
for s in sorted(V):
    print(f"State: {s}, Value: {round(V[s],2)}")