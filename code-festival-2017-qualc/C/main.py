#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(s: str):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
