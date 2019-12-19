#print sum of all the even numbers from 1 to N
n=int(input("Enter n value:"))
sum=0
for i in range(2,n+1,2):
    sum+=i
print(sum)