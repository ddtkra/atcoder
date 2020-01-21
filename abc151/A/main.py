#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(C: str):
    print(chr(ord(C)+1)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    C = next(tokens)  # type: str
    solve(C)

if __name__ == '__main__':
    main()
