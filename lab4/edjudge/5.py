def zero(n):
    cnt=n
    while cnt>=0:
        yield cnt
        cnt-=1
n=int(input())
for x in zero(n):
    print(x)