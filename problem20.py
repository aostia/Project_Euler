import time
def solve(n):
    ans = 1
    for x in range(2, n+1):
        ans*=x
    ans = str(ans)
    result = 0
    for x in range(0, len(ans)):
        result += int(str(ans[x]))
    return result
 
start = time.time()
result = solve(100)
end = time.time()
 
print "Result: " + str(result) + "  Time: " + str(end-start)