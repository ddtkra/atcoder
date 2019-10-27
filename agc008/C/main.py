#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(a_I: int, a_O: int, a_T: int, a_J: int, a_L: int, a_S: int, a_Z: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a_I = int(next(tokens))  # type: int
    a_O = int(next(tokens))  # type: int
    a_T = int(next(tokens))  # type: int
    a_J = int(next(tokens))  # type: int
    a_L = int(next(tokens))  # type: int
    a_S = int(next(tokens))  # type: int
    a_Z = int(next(tokens))  # type: int
    solve(a_I, a_O, a_T, a_J, a_L, a_S, a_Z)

if __name__ == '__main__':
    main()
