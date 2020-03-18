#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(a: str, b: str, c: str):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    c = next(tokens)  # type: str
    solve(a, b, c)

if __name__ == '__main__':
    main()
