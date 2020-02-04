#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]", e: "List[int]"):
    print(max(
        [ a[i]+b[i]+c[i]+d[i]+e[i]*110/900 for i in range(N) ]
    ))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    e = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
        e[i] = int(next(tokens))
    solve(N, a, b, c, d, e)

if __name__ == '__main__':
    main()
