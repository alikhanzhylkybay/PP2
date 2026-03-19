n=int(input())
num=list(map(int,input().split()))
positive=all(x>=0 for x in num)
if positive:
    print("Yes")
else:
    print("No")