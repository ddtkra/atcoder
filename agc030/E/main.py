#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, s: int, t: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = int(next(tokens))  # type: int
    t = int(next(tokens))  # type: int
    solve(N, s, t)

if __name__ == '__main__':
    main()
