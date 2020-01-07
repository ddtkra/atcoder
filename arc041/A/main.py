#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(x: int, y: int, k: int):
    if k <= y:
        print(x+k)
    else:
        print(y+x-(k-y))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(x, y, k)

if __name__ == '__main__':
    main()
