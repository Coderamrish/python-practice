# python can be used to perform operations on a file.(read & write data)
# we have to open a file reading or writing

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

data = f.read() # reads entire file
data = f.readline() # reads one line at a time