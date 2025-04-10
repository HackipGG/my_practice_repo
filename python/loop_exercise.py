#exercise 1
for i in range (1,20):
    if i%3 == 0:
        print (i)
print ('\n')
#exercise 2
i=1
sum=0
while i <= 50:
    if i%2 == 0:
        sum += i
    i+=1
print (sum)
print ('\n')
#exercise 3
numbers = [5, 8, 2, 15, 10, 3, 7]
for i in numbers:
    if i>5:
        print (i)
#swap list
def swap(lst):
    lst[-1] += lst[0]
    lst[0] = lst[-1] - lst[0]
    lst[-1] -= lst[0]
    return lst
print(swap([4,6,9,1,10,2,6,0,7]))