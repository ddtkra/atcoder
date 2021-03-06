#!/usr/bin/env python3
import sys


def solve(H: int, W: int, A: "List[List[str]]"):

    INF = -1
    d = [[INF] * W for i in range(H)]

    from collections import deque
    q = deque()

    # q.appendleft([sy,sx])

    s = []
    for i,x in enumerate(A):
        idx =[j for j,y in enumerate(x) if y == '#']
        for j in idx:
            q.appendleft([i,j])


    dx = [[-1,0], [1,0], [0,1], [0,-1]]

    ans = 0
    while(len(q)):
        # for i in A:
        #     print(i)
        # print()
        if(A == [['#']*W for i in range(H)]):
            break
        i,j = q.pop()
        if(A[i][j] == '#'):
            for di,dj in dx:
                nx = i+di
                ny = j+dj
                f = False
                if(0 <= nx < W and 0 <= ny < H and d[nx][ny] == INF and A[nx][ny] == '.'):
                    q.appendleft([ny,nx])
                    A[nx][ny] = '#'
                    f = True
            if(f):
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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [ list(next(tokens)) for _ in range(W) ]  # type: "List[str]"
    solve(H, W, A)

if __name__ == '__main__':
    main()
