import timeit
start = timeit.default_timer()
#timer start
TRIALS = 1000
CURFILE = "data3.txt"

def insertionSort(myarr):
  for i in range(1, len(myarr)):
    key = myarr[i]
    j = i - 1
    while j >= 0 and key < myarr[j]:
      myarr[j+1] = myarr[j]
      j -= 1
    myarr[j+1] = key
  return myarr

def bubbleSort(myarr):
  for i in range(1, len(myarr)):
    for j in range(len(myarr)-1):
      while j < len(myarr) and myarr[j] > myarr[j+1]:
        temp = myarr[j+1]
        myarr[j+1] = myarr[j]
        myarr[j] = temp
  return myarr

def selectionSort(myarr):
  for i in range(len(myarr)):
    mini = myarr[i]
    ind = i
    for j in range(i+1, len(myarr)):
        if myarr[j] < mini:
          mini = myarr[j]
          ind = j
    temp = myarr[i]
    myarr[i] = mini
    myarr[ind] = temp
    print(myarr)
  return myarr
  
for b in range(TRIALS):
  data = open(CURFILE, 'r')
  arr = []
  temp = data.readline()
  while temp:
    arr.append(int(temp))
    temp = data.readline()

  if b == 0:
    print(arr)

  #arr = insertionSort(arr)
  arr = bubbleSort(arr)
  #arr = bubbleSort(arr)
  #insertion sort - 0.003
  '''for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  '''

  #bubble sort - 0.02
  '''
  for i in range(1, len(arr)):
    for j in range(len(arr)-1):
      while j < len(arr) and arr[j] > arr[j+1]:
        temp = arr[j+1]
        arr[j+1] = arr[j]
        arr[j] = temp
  '''

  #selection sort - 0.0007
  '''
  for i in range(len(arr)):
    mini = arr[i]
    ind = i
    for j in range(i, len(arr) - 1):
        if arr[j] < mini:
          mini = arr[j]
          ind = j
    temp = arr[i]
    arr[i] = mini
    arr[ind] = temp
  '''

  if(b == TRIALS-1):
    print(arr)

#timer stop
stop = timeit.default_timer()
print('Time: ', (stop - start)/TRIALS)
