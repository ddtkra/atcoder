#!/usr/bin/env python3




def main():
    s = input()
    Q = int(input())
    q = [list(input().split()) for i in range(Q)]

    # print(q)

    rq = [0] * (Q+1)
    for i in range(Q):
        if len(q[i]) == 1:
            rq[i+1] = rq[i] + int(q[i][0])
        else:
            rq[i+1] = rq[i]
        rq[i+1] %= 2

    b = []
    a = []

    for i in range(Q):
        if len(q[i]) != 1:
            if (q[i][1] == '1' and rq[i+1] == 0) or (q[i][1] == '2' and rq[i+1] == 1):
                b.append(q[i][2])
            else:
                a.append(q[i][2])

    b = b[::-1]

    if rq[Q]%2 == 1:
        b, a = reversed(a), reversed(b)
        s = s[::-1]


    ans = ''.join([''.join(b), s, ''.join(a)])

    print(ans)


if __name__ == '__main__':
    main()
