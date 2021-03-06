#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(A: int, P: int):
    print((3*A+P)//2)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(A, P)

if __name__ == '__main__':
    main()
