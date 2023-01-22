n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    for j in range(1,100):
        if a%j==0 or b%j==0 or c%j==0:
            continue
        else:
            break
    print(j)
