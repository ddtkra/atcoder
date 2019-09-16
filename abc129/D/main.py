#!/usr/bin/env python3
import sys


def solve(H: int, W: int, S: "List[str]"):
    from collections import deque

    q = deque()
    ans = 0
    for x in range(H):
        for y in range(W):
            if(S[x][y] == '.'):

                t = 1
                
                # 上
                s = 1
                while(0 <= x-s < H and 0 <= y < W and S[x-s][y] == '.'):
                    t += 1
                    s += 1

                # 下
                s = 1
                while(0 <= x+s < H and 0 <= y < W and S[x+s][y] == '.'):
                    t += 1
                    s += 1

                # 左
                s = 1
                while(0 <= x < H and 0 <= y-s < W and S[x][y-s] == '.'):
                    t += 1
                    s += 1

                # 右
                s = 1
                while(0 <= x < H and 0 <= y+s < W and S[x][y+s] == '.'):
                    t += 1
                    s += 1

                ans = max(ans, t)

    print(ans)

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
