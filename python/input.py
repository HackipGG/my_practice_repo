'''
name=input("Please input name")
print("Hello,", name)
try:
    num=int(input("enter a integer"))
    print(num)
    double=num*2
    print(double)
except:
    print("you didn't enter an integer")
'''
""" with open("movies.txt") as file:
    for line in file:
        print(line.strip()) """
with open("heights.txt") as file:
    for line in file:
        info=line.strip().split()
        info[2]=int(info[2])
        print(info)
f = input("enter a filename")
with open(f) as file:
    for line in enumerate(file):
        print(line)
