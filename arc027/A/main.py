#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(h: int, m: int):
    print((18-h)*60-m)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    h = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    solve(h, m)

if __name__ == '__main__':
    main()
