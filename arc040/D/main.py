#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str

def solve(N: int, S: "List[str]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
