'''
Created on July 01st, 2022

@author: ytiani
'''
def square(n):
    x = lambda a : a**n
    return x

squareroot = square(2)

print (squareroot(2)) 

tables = [lambda x=x: x*10 for x in range(1, 11)] 
for table in tables:
    print(table())
    
print ('\n//////////////////map() function //////////////////')

#modulo of number in tuple
mylist = (12, 30,9,7,34,5)
def even(num):
    return num%2==0
result = map(even, mylist)
print(list(result))

#case 2
def even(num):
    return num%2==0
for x in map(even, mylist):
    print(x)

# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

print ('\n//////////////////filter() function //////////////////')

#modulo of number in tuple
mylist = (12, 30,9,7,34,5)
def even(num):
    return num%2==0
result = filter(even, mylist)
print(list(result))

#case 2
def even(num):
    return num%2==0
for x in filter(even, mylist):
    print(x)

print ('\n//////////////////lambda() function //////////////////')

''''Lambda is used as an alternative to def function to make the code more simple. Instead of using def we can use lambda if 
ww intend to use the function only one time'''

mylist = (12, 30,9,7,34,5)
# def even(num):
#     return num%2==0
result1 = filter(lambda num: num%2==0, mylist)
result2 = map(lambda num: num%2==0, mylist)

print(f'the filter is {list(result1)} and map is {list(result2)}')