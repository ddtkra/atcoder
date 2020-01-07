#!/usr/bin/env python3




def main():
    # Failed to predict input format
    N, Q = map(int, input().split())
    s = []
    for i in range(Q):
        x = list(map(int, input().split()))
        s.append(x)

    # print(s)

    ans = [['N'] * (N+1) for i in range(N+1)]

    for i in range(Q):
        l = s[i]
        
        if l[0] == 1:
            ans[l[1]][l[2]] = 'Y'
        elif l[0] == 2:
            for j in range(1, N+1):
                if ans[j][l[1]] == 'Y':
                    ans[l[1]][j] = 'Y'


        elif l[0] == 3:
            al = [j for j,v in enumerate(ans[l[1]]) if v == 'Y']
            for j in al:
                for k in range(1, N+1):
                    if ans[j][k] == 'Y' and k != l[1]:
                        ans[l[1]][k] = 'Y'


    for i in range(1, N+1):
        print(''.join(ans[i][1:]))
        # print(ans[i][1:])
    

if __name__ == '__main__':
    main()
