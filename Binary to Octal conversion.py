print("Enter a binary number: ")
binary = int(input())
octal = 0
decimal = 0
i = 0
while (binary != 0):
    decimal = decimal + (binary % 10) * pow(2, i)
    i += 1
    binary = binary // 10
print("decimal value ", decimal)
i = 1
while (decimal != 0):
    octal = octal + (decimal % 8) * i
    decimal = decimal // 8
    i = i * 10
print("octal value: ", octal)
