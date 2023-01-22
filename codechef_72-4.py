n = int(input())
for i in range(n):
    a = int(input())
    for j in range(1,a):
        for k in range(1,a):
            for l in range(1,a):
                if a%(j*k)==0 and a%(k*l)==0 and a%(l*j)==0 and (j*k*l)%a==0:
                    break
    print(j,k,l)
