#!/usr/bin/env python3
import sys
from math import ceil, floor

def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    
    x = []
    y = []  

    for i in range(ceil(F/(100*A))+1):
        for j in range(ceil(F/(100*B))+1):
            dx = 100*A*i+100*B*j
            if(min(100*A,100*B) <= dx <= F):
                x.append(dx)

    for i in range(ceil(F/C)+1):
        for j in range(ceil(F/C)+1):
            dy = C*i+D*j
            if(0 <= dy <= F):
                y.append(dy)

    x = sorted(list(set(x)))
    y = sorted(list(set(y)))
    
    w = x[0]
    s = y[0]

    for i in x:
        for j in y:
            de = 100*s/(w+s)
            ne = 100*j/(i+j)
            if(i+j <= F and de < ne <= 100*E/(100+E)):
                # print(i, j, ne)
                w = i
                s = j

    print(w+s, s)

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)

if __name__ == '__main__':
    main()
