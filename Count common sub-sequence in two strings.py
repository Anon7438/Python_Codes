
# Python3 program to count common
# subsequence in two strings
 
# return the number of common subsequence
# in two strings
def CommomSubsequencesCount(s, t):
 
    n1 = len(s)
    n2 = len(t)
    dp = [[0 for i in range(n2 + 1)]
             for i in range(n1 + 1)]
 
    # for each character of S
    for i in range(1, n1 + 1):
 
        # for each character in T
        for j in range(1, n2 + 1):
 
            # if character are same in both
            # the string
            if (s[i - 1] == t[j - 1]):
                dp[i][j] = (1 + dp[i][j - 1] +
                                dp[i - 1][j])        
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] -
                            dp[i - 1][j - 1])        
         
    return dp[n1][n2]
 
# Driver Code
s = input('Enter 1st String : ')
t = input('Enter 2nd String : ')
 
print(CommomSubsequencesCount(s, t))