#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(R: int, B: int, x: int, y: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(R, B, x, y)

if __name__ == '__main__':
    main()
