from number import isprime
import time
from math import sqrt
 
def solve():
    target = 600851475143 
    largest = 0
    for x in range(2, int(sqrt(target))):
        if target%x == 0:
            if isprime(target/x):
                if target/x > largest:
                    largest = target/x
            elif isprime(x):
                if x > largest:
                    largest = x
                
    return largest

 
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end-start)