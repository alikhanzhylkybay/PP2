n=int(input())
words=input().split()
res=enumerate(words)
print(*[f"{i}:{w}" for i, w in res])
