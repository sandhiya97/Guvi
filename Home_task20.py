# Program to check Armstrong numbers from 1 to n
lower = 1
n = int(input())
for num in range(lower, n + 1):
   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)