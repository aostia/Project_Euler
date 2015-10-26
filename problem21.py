from number import factor
import time
 
def solve():
    result = 0
    for x in range(1, 10000):
        divisors = factor(x)
        sum1 = 0
        for y in range(0, len(divisors)-1):
            sum1 += divisors[y]
        divisors = factor(sum1)
        sum2 = 0
        if sum1!=x:
            for y in range(0, len(divisors)-1):
                sum2 += divisors[y]
            if sum2==x:
                result = result+x
    return result
           
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end - start)