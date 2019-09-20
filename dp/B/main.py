#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    INF = 10000000000
    dp = [INF]* (N+1)
    dp[0] = 0
    dp[1] = abs(h[1]-h[0])
    for i in range(2,N):
        for t in range(1,K+1):
            if(i-t >= 0):
                dp[i] = min(dp[i], dp[i-t]+abs(h[i]-h[i-t]))
        # print(dp)
    print(dp[N-1])
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()