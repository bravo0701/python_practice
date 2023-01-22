t = int(input())
LisT = []
count = 0
for i in range(t):
    c = int(input())
    x = list(map(int,input().split()))
    for i in range(c):
        if x[i]%2!=0:
            count = count+1
    if count == 0 or 2 != 0:
        print("NO")
    else:
        print("YES")