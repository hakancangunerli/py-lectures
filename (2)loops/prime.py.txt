for i in range (1, 100):      # main loop with index ("i") going from 2 to 100 (skip 1)
   prime_flag = True          # 1=TRUE, 0=FALSE; assume it's prime unless proven otherwise
   for divisor in range(2, i-1):   # scroll through all possible divisors from 2 to i-1
      if i % divisor == 0:         # if "i" is exactly divisible by some smaller divisor 
         prime_flag = False        # then it is NOT prime, so set the prime_flag to 0 and
         break                     # break out of the loop if that the number is not prime
   if prime_flag:                  # if the prime_flag is still true...
      print(i)      