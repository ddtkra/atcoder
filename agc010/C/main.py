#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, A: "List[int]", a: "List[int]", b: "List[int]"):
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
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, A, a, b)

if __name__ == '__main__':
    main()