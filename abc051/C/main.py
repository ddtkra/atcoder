#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(sx: int, sy: int, tx: int, ty: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    sx = int(next(tokens))  # type: int
    sy = int(next(tokens))  # type: int
    tx = int(next(tokens))  # type: int
    ty = int(next(tokens))  # type: int
    solve(sx, sy, tx, ty)

if __name__ == '__main__':
    main()
