#!/usr/bin/env python3
import sys


def solve(s: str):
    
    s = s.replace('BC', 'X')

    ans = 0
    cur = 0
    for i in range(len(s)):
        if(s[i] == 'A'):
            cur += 1
        elif(s[i] == 'X'):
            ans += cur
        else:
            cur = 0    

    print(ans)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()