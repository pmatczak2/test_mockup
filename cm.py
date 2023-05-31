# context manager

f = open("README.rst","r")
content = f.readlines()
print(content)
f.close()
# always close file! because of memory leak


with open("README.rst", "r") as f:
    content = f.readlines()
    print(content)
print("good bye")

#