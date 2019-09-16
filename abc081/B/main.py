#!/usr/bin/env python3
import sys

MOD = 2  # type: int

def solve(N: int, A: "List[int]"):
    ans = 0
    f = 0
    while(not f):
        t = [i%2==0 for i in A]
        if(t.count(True) == N):
            A = [i//2 for i in A]
            ans += 1
        else:
            f = 1
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
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
