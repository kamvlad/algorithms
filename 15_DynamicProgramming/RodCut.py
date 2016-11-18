n = 10
costs = [1, 5, 8, 9]

#assert (n == len(costs))
dynamic = [-1] * n

def solve(n,  costs):
    r = 0
    for i in range(min(n, len(costs))):
        if dynamic[n - i - 1] == -1:
            dynamic[n - i - 1] = solve(n - i - 1, costs)
        c = dynamic[n - i - 1] + costs[i]
        if c > r:
            r = c
    return r

print(solve(n, costs))
print dynamic