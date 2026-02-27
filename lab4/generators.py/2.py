def evens(n):
    cnt=0
    while cnt<=n:
        yield cnt
        cnt+=2
n=int(input())
print(*evens(n), sep=",")
