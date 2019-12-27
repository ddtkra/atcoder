#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(x: int, y: int, W: str, c: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    W = next(tokens)  # type: str
    c = [int(next(tokens)) for _ in range(9)]  # type: "List[int]"
    solve(x, y, W, c)

if __name__ == '__main__':
    main()
