#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str):
    N = len(S)
    l = [0] * (N+1)

    for i in range(N):
        if S[i] == '<':
            l[i+1] = l[i]+1

    for i in range(N)[::-1]:
        if S[i] == '>':
            l[i] = max(l[i], l[i+1]+1)

    print(sum(l))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
