#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

# refered to
# rank : http://at274.hatenablog.com/entry/2018/02/02/173000
# size : abc120 kaisetsu
class UnionFind:
    def __init__(self, n):
        # par = Parent Number or NoV
        self.par = [-1] * (n+1)
        # rank = Tree Height
        self.rank = [0] * (n+1)
    
    # Returns the number of sets to which x belongs
    def size(self, x):
        return -1*self.par[self.find(x)]
    
    def size_list(self):
        return [x*(-1) for x in self.par[1:] if x < 0]

    # Returns number if root
    def find(self, x):
        if(self.par[x] < 1):
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    # Are the parents of x and y the same?
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        # find root 
        x = self.find(x)
        y = self.find(y)

        # Already x connect to y
        if(x == y):
            return False

        # Reconnect
        if(self.size(x) < self.size(y)):
            x,y = y,x
        
        # update x size
        self.par[x] += self.par[y]
        # set parent number of y to x
        self.par[y] = x

        return True 
    
    def root_nodes(self):
        return len([i for i in self.par[1:] if i <= -1])


def solve(N: int, M: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    uf = UnionFind(N)
    for i in range(M):
        uf.union(X[i], Y[i])
    print(uf.root_nodes())
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    Z = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, M, X, Y, Z)

if __name__ == '__main__':
    main()
