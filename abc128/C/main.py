#!/usr/bin/env python3

MOD = 2  # type: int



def main():
    N, M = map(int, input().split())
    k = []
    s = []
    for i in range(M):
        l = input().split()
        k.append(l[0])
        s.append(list(map(int, l[1:])))
    p = list(map(int, input().split()))

    ans = 0
    
    for i in range(1<<N):
        t = [0] * M
        for j in range(N):
            if i>>j & 1:
                for r in range(M):
                    # print(j+1, s[r])
                    if j+1 in s[r]:
                        t[r] += 1
        f = True
        for j in range(M):
            if t[j]%2 != p[j]:
                f = False
        
        if f:
            ans += 1

    print(ans)
    
    

if __name__ == '__main__':
    main()
