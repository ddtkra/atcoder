#!/usr/bin/env python3
import sys
import math

def solve(N: int, K: int):

    ans = int(N/K) ** 3

    if(K%2 == 0):
        cnt = 0
        for i in range(int(K/2), N+1, K):
            cnt += 1
        ans += cnt ** 3
    
    print(ans)

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
    solve(N, K)

if __name__ == '__main__':
    main()
