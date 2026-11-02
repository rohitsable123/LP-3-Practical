
def fibonacci(n):
    a = 0
    b = 1
    steps = 0

    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b
        steps += 1

    print("\nsteps count is:", steps)

n = int(input("Enter number of terms: "))

fibonacci(n)