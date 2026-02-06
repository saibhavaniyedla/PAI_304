def water_jug(jugA,jugB,target):
    open_list=[((0,0),[])]
    visited=[]
    while open_list:
        (a,b),path=open_list.pop(0)
        if(a,b) in visited:
            continue
        visited.append((a,b))
        path=path+[(a,b)]
        if a==target or b==target :
            return path
        moves=[(jugA,b),(a,jugB),(0,b),(a,0),(a-min(a,jugB-b),b+min(a,jugB-b)), (a+min(b,jugA-a),b-min(b,jugA-a))]
        for move in moves:
            if move not in visited:
                open_list.append((move,path))
    return none


jugA=int(input("JugA Capacity:"))
jugB=int(input("JugB Capacity: "))
target= int(input("Target: "))
solution=water_jug(jugA,jugB,target)
if solution:
    print("Solution Path:")
    print(solution)
else:
    print("Not possible with the given jugs")
