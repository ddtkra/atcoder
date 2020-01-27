#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 9  # type: int

def solve(K: int, M: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(K, M)

if __name__ == '__main__':
    main()
