# function Call itself
# factorial
def fact_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        fact = n * fact_recursive(n-1)
        return fact


n = int(input("Enter The Number for FActorial : "))
f = fact_recursive(n)
print(f)
