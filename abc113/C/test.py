
N=5
val = [[] for i in range(N)]

t = [[1,0], [1,1], [1,3]]

for t0, t1 in t:
    val[t0].append(t1)

for i in val:
    print(i)
