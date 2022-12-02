
words=["Anon","yoy" ]
with open('sample.txt')as f:
    content = f.read()
    print(content)

for word in words :
     content = content.replace(word, "Anon")
with open('sample.txt', 'w')as f:
    f.write(content)

with open('sample.txt')as f:
    content = f.read()
    print(content)