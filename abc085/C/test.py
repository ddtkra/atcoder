import sys


a = [1,2,4,7]
k = 13
n = 4

def dfs(i:int, s:int):
    if(i == n):
        return s==k

    if(dfs(i+1,s)):
        return True

    if(dfs(i+1,s+a[i])):
        return True
    return False

if(dfs(0,0)):
    print('Yes')
else:
    print('No')