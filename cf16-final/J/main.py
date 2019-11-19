#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

NO = "NO"  # type: str

def solve(N: int, U: "List[int]", D: "List[int]", L: "List[int]", R: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    U = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    R = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, U, D, L, R)

if __name__ == '__main__':
    main()
