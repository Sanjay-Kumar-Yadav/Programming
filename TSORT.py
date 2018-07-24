n=int(input())
b=n
a=[]
while n>=1:
  a.append(int(input()))
  n=n-1

i=0
a.sort()
while b>=1:
  print(a[i])
  i=i+1
  b=b-1
