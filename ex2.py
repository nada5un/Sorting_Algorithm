n = int(input())
arr = []
for i in range(n):
  arr.append(input().split())

def setting(data):
  return data[1]

result = sorted(arr,key=setting)
for i in result:
  print(i[0], end=' ')