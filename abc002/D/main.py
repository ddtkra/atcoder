#!/usr/bin/env python3
import sys
import numpy

def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    
    ans = 1
    
    xy = [[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        xy[x[i]][y[i]] = 1
        xy[y[i]][x[i]] = 1

    for i in range(1<<N):
        l = []
        for j in range(N):
            if (i>>j)&1 :
                l.append(j+1)
        
        nl = len(l)
        f = True
        for s in range(nl):
            for t in range(nl):
                if(s == t): continue
                if(xy[l[s]][l[t]] == 0):
                    f = False
        
        if(f):
            ans = max(ans,len(l))

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
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]" 
    y = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)

if __name__ == '__main__':
    main()
