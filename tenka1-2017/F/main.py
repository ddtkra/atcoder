#!/usr/bin/env python3
import sys

MOD = 4  # type: int

def solve(Q: int, A: "List[int]", M: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    A = [int()] * (Q)  # type: "List[int]" 
    M = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        A[i] = int(next(tokens))
        M[i] = int(next(tokens))
    solve(Q, A, M)

if __name__ == '__main__':
    main()
