n = int(input())
arr = map(int, input().split())
list = []
i = 0
list.extend(arr)
m = list.count(max(list))
if m == 1:
    pass
else:
    while(i<m-1):
        list.remove(max(list))
        i = i+1
if n != 1:
    k1 = list.remove(max(list))
    k = list.pop(list.index(max(list)))
    print(k)

else:
    print(list[0])
