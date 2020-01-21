#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(X: str, s: str):
    print(''.join(s.split(X)))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    s = next(tokens)  # type: str
    solve(X, s)

if __name__ == '__main__':
    main()
