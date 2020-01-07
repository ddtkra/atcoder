#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]"):
    from collections import defaultdict
    a0 = -1
    a2 = -1
    d = defaultdict(lambda: 0)
    for i in range(1,N+1):
        d[i] = 0

    for i in A:
        d[i] += 1
    
    for k, v in d.items():
        if v == 2:
            a2 = k
        elif v == 0:
            a0 = k
        

    if a0 == -1 and a2 == -1:
        print('Correct')
    else:
        print(a2, a0)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
