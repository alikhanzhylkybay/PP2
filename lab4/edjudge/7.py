class Reverse:
    def __init__ (self, s):
        self.s=s
        self.index=len(s)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration
        char=self.s[self.index]
        self.index-=1
        return char
s=input()
for x in Reverse(s):
    print(x, end="")