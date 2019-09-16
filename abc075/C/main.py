#!/usr/bin/env python3
import sys

# refered to
# rank : http://at274.hatenablog.com/entry/2018/02/02/173000
# size : abc120 kaisetsu
class UnionFind:
    def __init__(self, n):
        # par = Parent Number or NoV
        self.par = [-1] * (n+1)
        # rank = Tree Height
        self.rank = [0] * (n+1)
    
    # 自分が所属する集合の数を返す
    def size(self, x):
        return -1*self.par[self.find(x)]
    
    def size_list(self):
        return [x*(-1) for x in self.par[1:] if x < 0]

    # 根なら番号を返す
    def find(self, x):
        
        if(self.par[x] < 1):
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    # 親が同じか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)

        # もう繋がれている
        if(x == y):
            return False

        # つなぎ替える
        if(self.size(x) < self.size(y)):
            x,y = y,x
        
        # xのサイズを更新
        self.par[x] += self.par[y]
        # yのサイズ(おやばんごう)をxに
        self.par[y] = x

        return True 


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if(j == i):
                continue
            else:
                uf.union(a[j], b[j])

        if(not uf.same_check(a[i], b[i])):
            ans += 1
        
    print(ans)

    return


# Generated by 1.1.3 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]" 
    b = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
