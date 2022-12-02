num = (input("Enter a  Number : "))
reverse = num[::-1]
if (num == reverse):
    print("The given {} is a palindrome  ".format(num))
else:    
    print("This Given {} is Not a palindrome  ".format(num))
