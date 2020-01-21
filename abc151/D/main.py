#!/usr/bin/env python3


INF = 10**9

def main():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        t = input()
        s.append(t)

    from collections import deque
    d = deque()
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                d.append([i, j])

    ans = 0
    while len(d) != 0:
        x, y = d.popleft()
        
        sc = [[-1] * (w) for i in range(h)]
        sc[x][y] = 0
        
        dd = deque()
        dd.append([x,y])

        while len(dd) != 0:
            # for i in sc:
            #     print(i)
            ix, iy = dd.popleft()
            for k in range(4):
                i = dx[k]
                j = dy[k]
                # print(ix+i, iy+j)
                if 0 <= ix+i < h and 0 <= iy+j < w:
                    if s[ix+i][iy+j] == '.':
                        if sc[ix+i][iy+j] == -1:
                            sc[ix+i][iy+j] = sc[ix][iy]+1   
                            dd.append([ix+i, iy+j])
                    
                            
        # for i in sc:
        #     print(i)
        # print('')
        ans = max(ans, max([max(i) for i in sc]))
    
    print(ans)



if __name__ == '__main__':
    main()
