#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(AtCoder: str, s: str, Contest: str):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    AtCoder = next(tokens)  # type: str
    s = next(tokens)  # type: str
    Contest = next(tokens)  # type: str
    solve(AtCoder, s, Contest)

if __name__ == '__main__':
    main()
