#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, S: str):
    s = list(S)
    s[K-1] = s[K-1].lower()
    print(''.join(s))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
