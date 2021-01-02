=print('the prime numbers between 1 and 20 are')
for num in range(1,20 + 1):  #numnbers between 1-20
   if num > 1: 
       for i in range(2,num):
           if (num % i) == 0: 
               break
       else:
           print(num)

#student is asked to create a prime number system 
