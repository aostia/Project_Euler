import time
from itertools import permutations
 
def solve():
    return "".join(sorted(permutations(['0','1','2','3','4','5','6','7','8','9']))[999999])    
   
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end - start)