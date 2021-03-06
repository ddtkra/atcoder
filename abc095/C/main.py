#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    if(2*C >= A+B):
        print(A*X+B*Y)
        exit()

    ans = A*X+B*Y
    for i in range(100001):
        ans = min(ans, 2*C*i + max(0,X-i)*A + max(0,Y-i)*B)

    print(ans)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)

if __name__ == '__main__':
    main()
