#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(H: int, W: int, N: int, r: "List[int]", c: "List[int]"):
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    r = [int()] * (N)  # type: "List[int]" 
    c = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(H, W, N, r, c)

if __name__ == '__main__':
    main()
