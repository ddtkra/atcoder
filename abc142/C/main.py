#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    x = sorted([[i,A[i]] for i in range(N)], key=lambda x:x[1])
    ans = [i+1 for i,j in x]
    print(' '.join(map(str,ans)))

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
    solve(N, A)

if __name__ == '__main__':
    main()
