#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(L: int, B: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(L)]  # type: "List[int]"
    solve(L, B)

if __name__ == '__main__':
    main()
