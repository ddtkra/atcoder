#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int):
    if B < 0:
        print(abs(B-A))
    
    elif A < 0:
        print(abs(A)+B-1)
    else:
        print(B-A)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
