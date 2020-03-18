#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(s: str):
    n = len(s)
    # def f(K: int):
        
        
    def binary_search(left: int, right: int):
        while right-left > 1:
            mid = (left+right)//2
            b = mid+1
            a = mid
            if n%2 == 0:
                a += 1
            sb = ''.join([i for i in s[:b] if i != 'x'])
            sa = ''.join([i for i in s[a:] if i != 'x'])
            # print(sb, sa)
            if sb == sa[::-1]:
                return mid
            else:
                if len(sb) < len(sa):
                    left = mid
                else:
                    right = mid
        return left

    from collections import Counter
    c = Counter([i for i in list(s) if i != 'x'])
    x = [v%2 == 0 for k,v in c.items()].count(False)
    y = [v%2 == 0 for k,v in c.items()].count(True)
    # print([v%2 != 0 for k,v in c.items()])
    if not(x == 0 or (x == 1 and y == len(c.keys())-1)):
        print(-1)
        exit()

    from math import ceil, floor

    # print(ceil(n/2))
    p = binary_search(0, n-1)
    print(p)
    print(s[:p+1], s[p:])
    # recovery
    ans = 0
    ts = [i for i in s[p:] if i != 'x']
    idx = 0
    for i in range(max(p, n-p)):
        if  
    # print(max(p, n-1-p))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
