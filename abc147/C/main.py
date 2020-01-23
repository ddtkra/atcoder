#!/usr/bin/env python3

def main():
    # Failed to predict input format
    N = int(input())
    x = [ [] for i in range(N+1)]
    for i in range(N):
        a = int(input())
        for j in range(a):
            x[i].append(list(map(int, input().split())))

    ans = 0
    for i in range(1<<N):
        y = [[] for k in range(N+1)]
        for j in range(N):
            if (i>>j) &1:
                for k in range(len(x[j])):
                    a, b = x[j][k]
                    # print(a-1, b)
                    y[a].append(b)

        if all([j == [] or j.count(1) == len(j) or j.count(0) == len(j) for j in y[1:]]):
            f = True
            for idx, k in enumerate(y[1:], 1):
                if k == []:
                    continue

                elif k[0] == 0 and not i>>(idx-1)&1:
                    continue

                elif k[0] == 1 and i>>(idx-1)&1:
                    continue

                else:
                    f = False
            if f:
                ans = max(ans, '{:05b}'.format(i).count('1'))
                
    print(ans)


if __name__ == '__main__':
    main()
