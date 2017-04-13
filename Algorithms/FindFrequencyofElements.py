# Given a sorted array , output the frequency of occurence of each element

def findFrequencyUtil(a,low,high,elements):
  if a[low] == a[high]:
    if a[low] not in elements:
      elements[a[low]] = high - low +1
    else:
      elements[a[low]]+= high - low+1
  else:
    mid = (high + low)/2
    findFrequencyUtil(a,low,mid,elements)
    findFrequencyUtil(a,mid+1,high,elements)

def findFrequency(a):
  low = 0
  high = len(a) -1
  elements = {}
  findFrequencyUtil(a,low,high,elements)
  
  for key in elements:
    print "Frequency of element = "+ str(key) + " is "+ str(elements[key])

arr = [1,1,1,3,3,3,3,3]
findFrequency(arr)


#T(n) = 3(T(n/2)) + O(n)

