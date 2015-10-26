import time
 
def solve():
    sum  = 200
    total = 0
 
    for a in range(sum, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                total += 1

    return total                                
        
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end-start)