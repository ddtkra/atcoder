#!/usr/bin/env python3
import sys
import numpy as np

def solve(n: int, a: "List[int]", b: "List[int]"):
    l = [0] * (10**6+2)

    for i in range(n):
        l[a[i]] += 1
        l[b[i]+1] -= 1
    
    x = [0] * (10**6+3)
    for i in range(10**6+2):
        x[i+1] += x[i] + l[i]

    print(max(x))

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int()] * (n)  # type: "List[int]" 
    b = [int()] * (n)  # type: "List[int]" 
    for i in range(n):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, a, b)

if __name__ == '__main__':
    main()
