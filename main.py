n = int(input())

l = [500,100,50,10,5,1]

n = 1000-n
ans = 0
for i in l:
    if(n == 0):
        break
    else:
        ans += int(n/i)
        n = n%i

print(ans)

