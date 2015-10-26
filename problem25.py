import time
 
def solve():
    term = 3
    a, b, c = 1, 1, 2
    while len(str(c)) < 1000:
        a = b
        b = c
        c = a + b
        term+=1
    return term
 
start = time.time()
result = solve()
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end-start)