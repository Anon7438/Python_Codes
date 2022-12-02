# Creating File in Python ------------->

file = open("Anon.txt", "w")


#To Read A file ----------> 

file.write("Hey This is sample Test text file ")
file.close

#To Read A file ---------->

file = open("Anon.txt", "r")
print(file.read())
file.close

#To Append a File

file = open("Anon.txt", "a")
file.write("Hey This is sample Test text file With Append  ")
file.close
file = open("Anon.txt", "r")
print(file.read())
file.close

#
