with open('sample.txt')as f:
    content = f.read()
    print(content)

    content = content.replace("Aakash", "Anon")
with open('sample.txt', 'w')as f:
    f.write(content)

with open('sample.txt')as f:
    content = f.read()
    print(content)