#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(c: "List[str]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [next(tokens) for _ in range(0 - 0 + 1)]  # type: "List[str]"
    solve(c)

if __name__ == '__main__':
    main()
