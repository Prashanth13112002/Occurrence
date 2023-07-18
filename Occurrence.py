class solution:
    def occurrence (self,arr):
        output=0
        for i in arr:
            output^=i
        return output
a1=solution()
a=list(map(int,input().split()))
print(a1.occurrence(a))