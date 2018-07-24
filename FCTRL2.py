n=int(input())

def fact(a):
  f=1
  while a>=1:
     f=f*a
     a=a-1
  return f

while n>=1:
  a=int(input())
  print(fact(a))
  n=n-1


