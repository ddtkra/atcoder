#!/usr/bin/env python3
import sys


def solve(n: int, p: "List[int]"):
    ans = 0
    for i in range(1,n-1):
        if((p[i-1] < p[i] < p[i+1]) or (p[i-1] > p[i] > p[i+1])):
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
    n = int(next(tokens))  # type: int
    p = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, p)

if __name__ == '__main__':
    main()
