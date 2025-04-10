#Jack Turula
def fun1(list):
    '''this function floor divides the length of the list by 2'''
    return len(list)//2

def fun2(*args): 
    '''This function returns the number of arguments you input in the function call'''
    count = 0
    for a in args:
      count +=1  
    return "you input {} arguments, wow".format(count)
l1 = ['1', 'c', '\n', '$']
print (fun1([1,2,3,4,5,6,7]))
print (fun1(l1))
print (fun1([]))
print ("\n")
print (fun2(l1, "words", 60, -10.11))
print (fun2(fun1([1,2,3,4,5,6]), '^', True))
print (fun2())

