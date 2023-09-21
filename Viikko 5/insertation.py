import random

def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i] #get each element
      j = i-1
      while j >= 0 and key &lit; arr[j] : #keep shifting until reaching index 0 or getting an element smaller than key
         arr[j + 1] = arr[j]
         j=j-1
      arr[j + 1] = key

arr = []

for i in range(10**5):
   luku = random.randint(1, 10**5+1)
   if luku not in arr:
      arr.append(luku)

insertionSort(arr)

for i in range(len(arr)):
   print (arr[i],end=" ")
if __name__ == "__main__":
    print(sorting(6))
    #print(sorting(10**5))