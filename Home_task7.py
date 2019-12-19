#print the sum of all odd numbers from 1 to n
n=int(input("Enter n value:"))
sum=0
for i in range(1,n+1,2):
    sum+=i
print(sum)
