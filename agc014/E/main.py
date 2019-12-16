#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (N - 1)  # type: "List[int]"
    d = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, a, b, c, d)

if __name__ == '__main__':
    main()
