
def knapsack(capacity, values, weights, n):

    dp = []

    for i in range(n + 1):
        row = []
        for w in range(capacity + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

n = int(input("Enter number of items:"))

values = list(map(int, input("Enter values seperated by spaces: ").split()))
weights = list(map(int, input("Enter values seperated by spaces: ").split()))

if len(values) != n and len(weights) != n:
    print("Error: enter exactly", n, "values and weights!")
else:
    capacity = int(input("Enter capacity of knapsack: "))
    print("maximum value is:", knapsack(capacity, values, weights, n))