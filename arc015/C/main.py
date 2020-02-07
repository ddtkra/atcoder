#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, large: "List[str]", m: "List[int]", small: "List[str]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    large = [str()] * (N)  # type: "List[str]"
    m = [int()] * (N)  # type: "List[int]"
    small = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        large[i] = next(tokens)
        m[i] = int(next(tokens))
        small[i] = next(tokens)
    solve(N, large, m, small)

if __name__ == '__main__':
    main()
