#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(K: int, X: int):
    ans = [i for i in range(max(-1000000, X-K+1),min(1000000, X+K))]

    print(' '.join(map(str, ans)))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)

if __name__ == '__main__':
    main()
