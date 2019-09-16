#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[str]"):
    x = 0; a = 0; b = 0
    ans2 = 0
    for i in s:
        ans2 += i.count('AB')
        if(i[0] == 'B' and i[-1] == 'A'):
            x += 1
        elif(i[-1] == 'A'):
            a += 1
        elif(i[0] == 'B'):
            b += 1
    
    #####    AC2   ####
    ans1 = max(0,x-1) + min(a,b)
    if((a > 0 or b >0) and x > 0):
        ans1 += 1
    
    print(ans1+ans2)
    
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
