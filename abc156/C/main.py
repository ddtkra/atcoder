#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, X: "List[int]"):
    ans = INF
    for i in range(1, 101):
        t = 0
        for j in range(N):
            t += (X[j]-i)**2

        ans = min(ans, t)

    print(ans)

    returncode 