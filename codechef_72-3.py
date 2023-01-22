'''n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    list1 = []
    list2 = []
    if x==1 or y==1:
        print("1")
    elif x==2 or y==2:
        print("2")
    else:
        for j in range(1,x):
            if x%j==0:
                list1.append(j)
            n1 = max(list1)
        for j in range(1,y):
            if y%j==0:
                list2.append(j)
            n2 = max(list2)
        print(min(n1,n2))'''

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    print(a)