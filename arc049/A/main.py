#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str, A: int, B: int, C: int, D: int):
    print("".join([S[0:A], "\"", S[A:B], "\"", S[B:C], "\"", S[C:D], "\"", S[D:]]))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(S, A, B, C, D)

if __name__ == '__main__':
    main()
