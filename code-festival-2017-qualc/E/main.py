#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(A: int, B: int, C: int, D: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)

if __name__ == '__main__':
    main()
