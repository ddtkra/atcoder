#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, a: "List[int]", b: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, b)

if __name__ == '__main__':
    main()
