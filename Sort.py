#선택 정렬 
def select_sort():
  arr = [7,5,9,0,3,1,6,2,4,8]
  for i in range(len(arr)):
    #앞으로 보낼 자리 인덱스 
    min_index = i 
    for j in range(i+1,len(arr)):
      if arr[min_index]>arr[j]:
        #가장 작은 원소 
        min_index=j
    arr[i],arr[min_index] = arr[min_index],arr[i]
  print("선택 정렬: ",arr)

#삽입 정렬 
def insert_sort():
  arr = [7,5,9,0,3,1,6,2,4,8]
  for i in range(1,len(arr)):
    #인덱스 i 부터 1까지 감소하며 확인 
    for j in range(i,0,-1):
      #이전 것보다 값이 작다면 값 바꾸기 
      if arr[j]<arr[j-1]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
      else:
        break
  print("삽입 정렬: ",arr)

#퀵 정렬
def quick_sort1(arr,start,end):
  if start>=end:
    return
  #피봇은 첫번째 원소 
  pivot = start
  left = start+1
  right = end
  while left <= right:
    # 피봇보다 큰 데이터를 찾을 때 까지 left 증가 시킴 
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    # 피봇보다 작은 데이터 찾을 때 까지 right 감소 시킴 
    while right > start and arr[right] >= arr[pivot]:
      right -= 1
    # 엇갈렸다면 작은 데이터와 피봇을 교체 
    if left > right:
      arr[right],arr[pivot] = arr[pivot], arr[right]
    # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체 
    else:
      arr[left],arr[right] = arr[right],arr[left]
  # 분할 이후 왼쪽/ 오른쪽으로 나눠서 각각 정렬 
  quick_sort1(arr,start,right-1)
  quick_sort1(arr,right+1,end)

def quick_sort2(arr):
  if len(arr)<=1:
    return arr

  pivot = arr[0]
  tail = arr[1:]
  #list comprehension
  left = [x for x in tail if x<=pivot]
  right = [x for x in tail if x>pivot]
  return quick_sort2(left)+[pivot]+quick_sort2(right)

#계수 정렬 
def counting_sort():
  arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
  count = [0]*(max(arr)+1)

  # 각 데이터에 해당하는 인덱스 값 증가 
  for i in range(len(arr)):
    count[arr[i]] += 1
  for i in range(len(count)):
    # 인덱스 안 중복된 원소 출력  
    for j in range(count[i]):
      print(i,end=' ')



select_sort()
insert_sort()

arr1=[5,7,9,0,3,1,6,2,4,8]
arr2=[5,7,9,0,3,1,6,2,4,8]

quick_sort1(arr1,0,len(arr1)-1)
print("퀵 정렬 1: ",arr1)
print("퀵 정렬 2: ",quick_sort2(arr2))
print("계수 정렬")
counting_sort()