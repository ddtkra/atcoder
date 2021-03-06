#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int):
    def rec(n: int):
        if n >= K:
            return 0
        return rec(n*2)+1
    
    ans = 0
    for i in range(1, N+1):
        ans += 1/N * pow(1/2, rec(i))
    print(ans)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
