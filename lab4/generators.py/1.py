def squares(n):
    cnt=1
    while cnt<=n:
        yield cnt**2
        cnt+=1
n=int(input())
for i in squares(n):
    print(i)