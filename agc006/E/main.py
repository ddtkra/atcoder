#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, a: "List[List[int]]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [[int(next(tokens)) for _ in range(N)] for _ in range(3)]  # type: "List[List[int]]"
    solve(N, a)

if __name__ == '__main__':
    main()
