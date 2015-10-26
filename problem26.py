from number import isprime
import time
 
def solve():
    length = 0
    ans = 0
    for x in range(1000, 0, -1):
        if isprime(x):
            if length >= x:
                break;
            remainders = [0]*x
            value = 1
            pos = 0
            while remainders[value]==0 and value != 0:
                remainders[value] = pos
                value *= 10
                value = value%x
                pos += 1
            if pos -remainders[value] > length:
                ans = x
                length = pos - remainders[value]
    return ans
 
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end-start)