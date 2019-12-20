#program to print the number in reverse
n=int(input())
y=0
while(n>0):
  x=n%10
  y=x+y*10
  n=n//10
print(y)