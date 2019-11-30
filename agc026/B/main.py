#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(T: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    A = [int()] * (T)  # type: "List[int]"
    B = [int()] * (T)  # type: "List[int]"
    C = [int()] * (T)  # type: "List[int]"
    D = [int()] * (T)  # type: "List[int]"
    for i in range(T):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(T, A, B, C, D)

if __name__ == '__main__':
    main()
