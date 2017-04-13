def multiply(a,b):
  ans=0
  count = 0
  while a:
    if a%2 ==1:
      ans+= b<<count
      print ans
    a/=2
    count+=1
  return ans
  
print multiply(13,5)
      