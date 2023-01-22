str = input()
arr = []
arr1 = []
i = 0
j = 0
for i in str:
    arr.append(i)
# print(arr)
# print(" ")
arr2 = []
arr2 = arr2 + arr
# print(arr2)
# print(" ")
while j < len(arr2):
    m = arr2.pop()
    # print(arr2)
    # print(" ")
    arr1.append(m)
    # print(arr1)
    # print(" ")

if arr == arr1:
    print("palindrome")
else:
    print("not palindrome")
