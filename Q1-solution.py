C = int(input())

def markDelayed(x):
    delayed[x] = True
    visited[x] = True
    try:
        for y in hashmap[x]:
            if not visited[y]:
                markDelayed(y)
    except:
        pass

for c in range(C):
    hashmap = {}
    delayed = {x:False for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    visited = {x:False for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    # Read data
    K, J = [int(x) for x in input().split()]
    for k in range(K)::
        X, Y = input().split()
        if Y not in hashmap:
            hashmap[Y] = [X]
        else:
            hashmap[Y].append(X)

    for jj in input().split():
        delayed[jj] = True

    # For every delayed projects in J:, markDelayed recursively:
    for x in [zz for zz in delayed.keys() if delayed[zz]]:
        markDelayed(x)

    # Output all delayed projects
    print('Case #%d:' % (c+1), ' '.join(sorted([zz for zz in delayed.keys() if delayed[zz]])))