#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, t: "List[int]"):
    for i in range(2, N):
        if t[i]+t[i-1]+t[i-2] < K:
            print(i+1)
            exit()

    print(-1)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, t)

if __name__ == '__main__':
    main()
