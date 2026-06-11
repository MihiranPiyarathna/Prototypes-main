"""
Prime Mover

Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
Examples
Input: 9
Output: 23
Input: 100
Output: 541
Tags
math fundamentalsprime numbers
"""

num = 9 # 23
num = 100 # 541
num = 1000 # 7919

def PrimeMover(num):
  from math import sqrt
  def isprime(e):   
    for i in range(2, int(sqrt(e)+1)): # important since if n has a factor > sqrt(n) it has one lower as well.
      if e%i ==0:
        return False
    # print(e)
    return True
  
  if num == 1: return 2

  count = 0
  sample = 2
  while count < num:
    if isprime(sample):
      count +=1
    sample +=1
  return sample-1

print(PrimeMover(num))