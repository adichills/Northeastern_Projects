# Given a list of strings find the common prefix 

def findCommonPrefixUtil(str1,str2):
  i = 0
  cprefix = ''
  while i < len(str1) and i < len(str2):
    if str1[i] == str2[i]:
      cprefix += str1[i]
      i = i+1
    else:
      break
  return cprefix


def findCommonPrefix(a,low,high):
  if low == high:
    return a[low]
  mid = low + (high-low)/2
  str1 = findCommonPrefix(a,low,mid)
  str2 = findCommonPrefix(a,mid+1,high)
  print str1,str2
  return findCommonPrefixUtil(str1,str2)

arr = ["geeksforgeeks", "geeks","geek", "geezer"]
print findCommonPrefix(arr,0,len(arr)-1)
