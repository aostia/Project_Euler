from math import sqrt
def isprime(n):
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False
   first = 5
   second = 2
   while first * first <= n:
      if n % first == 0:
         return False
      first += second
      second = 6 - second
   return True
 
def gcd(number, denominator):
    while denominator != 0:
        temporary = denominator
        denominator = number % denominator
        number = temporary
    return number
 
def lcm(a,b):
    return a * b / gcd(a,b)
 
def factor(number_in):
    factors = set()
    for factorIterator in range(1, int(sqrt(number_in)) + 1):
        if number_in % factorIterator == 0:
            factors.add(factorIterator)
            factors.add(number_in // factorIterator)
    return sorted(factors)
 
def isPerfect(n):
    divisors = factor(n)
    sum = 0
    for x in range(0, len(divisors)-1):
        sum+=divisors[x]
    if sum==n:
        return True
    return False
 
def isAbundant(n):
   divisors = factor(n)
   sum = 0
   for x in range(0, len(divisors)-1):
      sum+=divisors[x]
   if sum>n:
      return True
   return False
 
def sumFrom(n1, n2):
   result = 0
   for x in range(n1, n2+1):
      result += x
   return result
 
def productFrom(n1, n2):
   result = 1
   for x in range(n1, n2+1):
      result *= x
   return result