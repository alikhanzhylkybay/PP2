n=int(input())
num=list(map(int, input().split()))
res=filter(lambda x: x%2==0,num)
print(len(list(res)))