def squares(n):
    cnt=0
    while cnt<=n:
        yield 2**cnt
        cnt+=1
n=int(input())
print(*squares(n))
