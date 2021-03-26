cls = int(input())
lst = input().split()
lst = list(map(int,lst))
start,Max = cls,0
for i in range(cls):
    if lst[i]==1:
        start= i
        break
p = range(cls)
for i in p[cls-1::-1]:
    if lst[i]==1:
        Max = i
        break
count = 0
for i in range(start,Max-1):
    if lst[i]==1:
        if lst[i+1] != 1:
            count+=1
    else:
        count+=1
print(count+1)
