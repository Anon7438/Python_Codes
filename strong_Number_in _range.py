# def fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact    
def Strong(n):
    temp = n 
    sum = 0
    while(temp):
        digit = temp % 10 
        temp = temp//10
        fact = 1
        for i in range(1, digit+1):
            fact = fact * i
        sum = sum + fact 
    return sum == n
    
      
min_value = int(input('Enter minimum value: '))
max_value = int(input('Enter maximum value: '))

for i in range(min_value, max_value+1):
    if Strong(i):
        print(i, end = ' ')