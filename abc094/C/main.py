#!/usr/bin/env python3
import sys
from bisect import bisect_left

def solve(N: int, X: "List[int]"):
    y = sorted(X)
    b = y[int(N/2)-1]
    a = y[int(N/2)]

    for i in X:
        if(i <= b):
            print(a)
        else:
            print(b)

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()
