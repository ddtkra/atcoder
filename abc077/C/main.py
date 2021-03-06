#!/usr/bin/env python3
import sys
from bisect import bisect_right, bisect_left


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    ans  = 0
    A.sort()
    B.sort()
    C.sort()
    for i in range(N):
        ai = bisect_left(A, B[i])
        ci = bisect_right(C, B[i])
        ans += (ai) * (N-ci)

    print(ans)

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)

if __name__ == '__main__':
    main()
