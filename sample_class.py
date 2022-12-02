class sample :
    a = "Anon"

obj = sample() #if you want to change in class code->> sample.a ="vicky"
obj.a = "vicky"    # you can not change class attribute
print(sample.a)
print(obj.a)