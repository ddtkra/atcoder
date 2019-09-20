#!/usr/bin/env python3
import sys

ans = []

def dfs(pros: "List[str]", cons: str):
    if(len(cons) == 1):
        pros.append(cons[0])
        ans.append(pros)
        return 0

    dfs(pros, cons)
    pros.append(cons[0])
    cons = cons[1:-1:1]
    dfs(pros, cons)

def solve(S: str):
    dfs([],S)

    ans = list(set(ans))

    print(ans[0])

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()