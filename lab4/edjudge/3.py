def divisors(n):
    cnt=0
    while cnt<=n:
        yield cnt
        cnt+=12
n=int(input())
continuous=False
for i in divisors(n):
    if continuous:
        print(" ", end="")
    print(i, end="")
    continuous=True