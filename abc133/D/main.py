#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    X = [0] * N
    S = sum(A)
    # 初期
    X[0] = S - sum([2*A[i] for i in range(1,N) if i%2 == 1])
    # 漸化式
    for i in range(1, N):
        X[i] = 2*A[i-1] - X[i-1]

    print(' '.join(map(str, X)))
    
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
