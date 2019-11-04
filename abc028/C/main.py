#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32
from itertools import combinations

def solve(A: int, B: int, C: int, D: int, E: int):
    l = [A,B,C,D,E]
    ans = []
    for i,j,k in combinations(l, 3):
        ans.append(i+j+k)

    ans.sort()
    print(ans[-3])

    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)

if __name__ == '__main__':
    main()
