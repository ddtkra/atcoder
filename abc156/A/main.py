#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, R: int):
    if N >= 10:
        print(R)
    else:
        print(R+100*(10-N))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(N, R)

if __name__ == '__main__':
    main()
