from collections import defaultdict
import heapq
 
n, m = map(int, input().split())
dct = defaultdict(list)
 
for i in range(n):
    a, b = map(int, input().split())
    dct[a].append(-b)
 
for k,v in dct.items():
    print(k, v)

h = []
res = 0
 
for i in range(1, m + 1):
    
    if dct[i]:
        for item in dct[i]:
            heapq.heappush(h, item)
    if h:
        res += heapq.heappop(h)
    print(i, h, res)

print(-res)