#Copy content of sample text to sample 1 text 

with open('sample.txt') as f:
    content= f.read()
    print("Sample Text\n",content)
    
#Read in content and paste in content 1 file 
with open('sample2.txt','w') as f:
    f.write(content)
    f.close()
#display The content     
with open('sample2.txt') as f:
    content = f.read()
    print("Sample2 Text\n",content)