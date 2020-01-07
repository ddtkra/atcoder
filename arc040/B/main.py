#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, R: int, S: str):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, R, S)

if __name__ == '__main__':
    main()
