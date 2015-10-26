from number import isAbundant
import time
 
def solve() :
    numbers = []
    for x in range(0, 28124):
        numbers.append(x)
    abundants = []
    for x in range(12, 28124):
        if isAbundant(x):
            abundants.append(x)
    num = 0
    for x in range(0, len(abundants)):
        for y in range(x, len(abundants)):
            num = abundants[x] + abundants[y]
            if num<28124:
                numbers[num] = -1
    result = 0
    for x in range(0, len(numbers)):
        if numbers[x] != -1:
            result+=x
    return result
 
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end - start)