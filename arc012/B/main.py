#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, v_a: int, v_b: int, L: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    v_a = int(next(tokens))  # type: int
    v_b = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, v_a, v_b, L)

if __name__ == '__main__':
    main()
