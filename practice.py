t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    max1 = max(x)
    freq1 = x.count(max1)

    if freq1>1:
        max2 = max(y)
        i = y.index(max2)
        j = i+1
        print(j)

    else:
        k = x.index(max1)
        print(k+1)