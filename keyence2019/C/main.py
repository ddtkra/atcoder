#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):

    s = [0] * N
    for i in range(N):
        s[i] = A[i]-B[i]

    s.sort()
    minus = sum([i for i in s if i < 0])
    minus_len = len([i for i in s if i < 0])
    plus =  sum([i for i in s if i >= 0])

    if(minus+plus < 0):
        print(-1)
        exit()

    s.sort(reverse=True)

    ans = 0
    while minus < 0:
        minus += s[ans]
        ans += 1

    print(ans + minus_len)

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
    solve(N, A, B)

if __name__ == '__main__':
    main()
