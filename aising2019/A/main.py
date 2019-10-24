#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, H: int, W: int):
    print((N-H+1)*(N-W+1))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(N, H, W)

if __name__ == '__main__':
    main()
