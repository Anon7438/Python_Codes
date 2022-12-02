x = input("Enter Any Alphabet : " )
n = ord(x)
if(65<=n<=90 or 97<=n<=122):
  print("yes" , n , "is an Alphabet")
else:
  print("NO" , n , "is Not an Alphabet")