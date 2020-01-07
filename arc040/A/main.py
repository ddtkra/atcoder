#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: "List[str]"):
    t = sum([i.count('R') for i in S])
    a = sum([i.count('B') for i in S])

    if t == a:
        print('DRAW')
    elif t > a:
        print('TAKAHASHI')
    else:
        print('AOKI')

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
