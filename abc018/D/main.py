#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: int, Q: int, R: int, x: "List[int]", y: "List[int]", z: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    x = [int()] * (R)  # type: "List[int]" 
    y = [int()] * (R)  # type: "List[int]" 
    z = [int()] * (R)  # type: "List[int]" 
    for i in range(R):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
    solve(N, M, P, Q, R, x, y, z)

if __name__ == '__main__':
    main()
