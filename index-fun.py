import time

def tablescan(searchterm):
  with open('unordered.txt', 'r') as file:
    words = file.read().splitlines()
    starttime = time.time()
    for i in range(len(words)):
      if words[i] == searchterm:
        print(f"tablescan found {searchterm} @ {i}")
        break
  endtime = time.time()
  print('tablescan runtime', endtime - starttime)

def makeIndex():
  with open('unordered.txt', 'r') as file:
    with open('unordered.idx', 'w') as indexFile:
      words = file.read().splitlines()
      for i in range(len(words)):
        # make baby's first 'index' file 🤡
        words[i] = words[i] + "," + str(i) + "\n"
      words.sort()
      indexFile.writelines(words)

def binarySearch(A, i):
  left = 0
  right = len(A) - 1
  while left <= right:
    middle = left + (right - left) // 2
    # we want only the value, so exclude the comma + rest
    value = A[middle].split(',')[0]
    if value == i:
      return middle
    elif value < i:
      left = middle + 1
    else:
      right = middle - 1
  return -1

def search(searchterm):
  with open('unordered.idx', 'r') as indexFile:
    indexLines = indexFile.read().splitlines()
    starttime = time.time()
    resultIndex = binarySearch(indexLines, searchterm)
    endtime = time.time()
    if resultIndex != -1:
      index = indexLines[resultIndex].split(',')[1]
      with open('unordered.txt', 'r') as file:
        words = file.read().splitlines()
        print(f"binarySearch found {searchterm} @ {index}")
        print(f"this should read {searchterm}:", words[int(index)])
        print('index runtime', '{:.10f}'.format(endtime - starttime))

# makeIndex()
tablescan("wiz")
search("wiz")