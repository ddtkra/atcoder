#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, D: "List[int]", M: int, T: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, D, M, T)

if __name__ == '__main__':
    main()