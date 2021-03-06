#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    ans = [0] * 8
    a32 = 0
    for i in a:
        if(i >= 3200):
            a32 += 1
        else:
            if(i < 400):
                ans[0] +=1
            elif(400 <= i < 800):
                ans[1] +=1
            elif(800 <= i < 1200):
                ans[2] +=1
            elif(1200 <= i < 1600):
                ans[3] +=1
            elif(1600 <= i < 2000):
                ans[4] +=1
            elif(2000 <= i < 2400):
                ans[5] +=1
            elif(2400 <= i < 2800):
                ans[6] +=1
            elif(2800 <= i < 3200):
                ans[7] +=1

    if(ans.count(0) == 8):
        if(a32 > 0):
            print(1, a32)
        else:
            print(0, 0)
    else:
        print(8-ans.count(0), 8-ans.count(0)+a32)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
