#!/usr/bin/env python3
import sys
from statistics import mean

def solve(N: int, a: "List[int]"):
    ans = 0
    if(sum(a)%N != 0):
        print(-1)
        sys.exit()
    av = int(sum(a)/N)
    for i in range(1,N):
        if(mean(a[:i]) != mean(a[i:])):
            ans += 1
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
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
