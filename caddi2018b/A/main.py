#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int):
    print(str(N).count('2'))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
