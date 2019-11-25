#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(a: "List[int]", b: "List[int]"):
    ab = a+b
    t1 = [ab.count(1), ab.count(2), ab.count(3), ab.count(4)]
    
    if t1.count(1) == t1.count(2):
        print(YES)
    else:
        print(NO)

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = [int()] * (3)  # type: "List[int]"
    b = [int()] * (3)  # type: "List[int]"
    for i in range(3):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(a, b)

if __name__ == '__main__':
    main()
