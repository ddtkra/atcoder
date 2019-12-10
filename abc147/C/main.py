#!/usr/bin/env python3




def main():
    N = int(input())
    A = []
    X = []
    for i in range(N):
        a = int(input())
        A.append(a)
        x = []
        for i in range(a):
            x.append(list(map(int, input().split())))

        X.append(x)

    # print(A)
    # print(X)
    # print(X[0][0])

    ans = 0
    for i in range(1<<N):
        m = [[] for k in range(N+1)]
        n = [0] * (N+1)
        c = [0] * (N+1)
        for j in range(N):

            if (i>>j) & 1:
                n[j+1] = 1
                for l in range(A[j]):
                    s,t = X[j][l]
                    m[s].append(t)

        for k in range(1, N+1):
            if m[k] == []:
                c[k] = 2
            
            elif all(m[k]):
                c[k] = m[k][0]

            else:
                continue
            
        tans = 0
        for j in range(1, N+1):
            if (n[j] == 1 and c[j] == 0) or (n[j] == 0 and c[j] == 1):
                tans = -10000
            if c[j] != 0 and n[j] != 0:
                tans += 1
        
        # print(n)
        # print(c)
        # print(tans)
        # print('---')

        ans = max(ans, tans, 0)

    print(ans)



                

    
        

if __name__ == '__main__':
    main()
