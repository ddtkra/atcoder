#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, S: int):
    ans = [S]*K
    ans.extend([10**9-1]*(N-K))

    print(' '.join(map(str, ans)))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(N, K, S)

if __name__ == '__main__':
    main()
