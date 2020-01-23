#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: "List[int]"):
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(A)

if __name__ == '__main__':
    main()
