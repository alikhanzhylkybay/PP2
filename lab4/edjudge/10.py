z=input().split()
n=int(input())
def times(z, n):
    for x in range(n):
        for i in z:
            yield i
print(*times(z, n))