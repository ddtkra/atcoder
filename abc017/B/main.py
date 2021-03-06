#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(X: str):
    ans = X.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")
    print(YES) if not ans else print(NO)


    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    solve(X)

if __name__ == '__main__':
    main()
