#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(1,N+1):
        s = str(i)
        d[int(s[0]+s[-1])] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += d[int(str(i)+str(j))]*d[int(str(j)+str(i))]

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
