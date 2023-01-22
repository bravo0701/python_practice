str = input()

arr = str.split()
arr2 = []
arr2 = arr2+arr
#print(arr)
arr1 = []
i = 0
while(i<len(arr)):
    #print(arr)
    m = arr.pop()
    #print(arr)
    arr1.append(m)
    #print(arr1)
    #print("/n")

if arr1 == arr2:
    print("palindrome")
else:
    print("not palindrome")