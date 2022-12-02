#Copy content of sample text to sample 1 text 

with open('sample.txt') as f:
    f1= f.read()

with open('sample2.txt') as f:
    f2=f.read()
    
if f1==f2 :
    print("Both Files Are Identical ")
else :    
    print("Both Files Are Not Identical ")