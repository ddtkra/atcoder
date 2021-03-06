#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[int]", y: "List[int]", h: "List[int]"):

    
    ansx = -1
    ansy = -1
    ansh = -1

    # ix = [i for i,x in enumerate(h) if(x > 0)][0]
    # print(ix)
    ix = h.index(max(h))

    for cx in range(101):
        for cy in range(101):
            H = h[ix] + abs(x[ix]-cx) + abs(y[ix]-cy)
            f = True
            for i in range(N):
                if(h[i] > 0 and H-h[i] != abs(x[i]-cx) + abs(y[i]-cy)):
                    f = False
                if(h[i] == 0 and H > abs(x[i]-cx) + abs(y[i]-cy)):
                    f = False
            if(f):
                ansx = cx
                ansy = cy
                ansh = H
        

    print(ansx, ansy, ansh)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]" 
    y = [int()] * (N)  # type: "List[int]" 
    h = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, x, y, h)

if __name__ == '__main__':
    main()
