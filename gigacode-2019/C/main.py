#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<64


def solve(D: int, a: "List[int]", b: "List[int]"):
    x = [0] * (D+1)
    for i in range(D):
        x[i+1] = x[i] + a[i]

    ans = INF
    for i in range(D):
        if x[i+1] >= b[i]:
            ans = min(ans, b[i])
            
    if ans == INF:
        print(-1)
    else:
        print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    solve(D, a, b)

if __name__ == '__main__':
    main()
