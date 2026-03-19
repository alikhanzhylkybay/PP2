n=int(input())
num=list(map(int, input().split()))
result=sum(map(lambda x: x**2,num))
print(result)