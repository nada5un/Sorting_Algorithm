n, k = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
arr2.sort()

count = 0

for i in range(n):
  arr1[i],arr2[n-1-i] = arr2[n-1-i],arr1[i]
  count +=1
  if count == k:
    break

print(sum(arr1))