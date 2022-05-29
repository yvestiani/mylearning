from ctypes.test.test_pickling import name
from random import shuffle

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange", "apple", "cherry"]

thisset.add('appled')

thisset.update(mylist)
x = thisset.difference(mylist)

#thisset.remove('apples')
#thisset.discard('appled')
print(thisset)
print(x)

def trirecursion(k):
  if(k > 0):
    result = k + trirecursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
trirecursion(6)

def funct(number_01):
   data = lambda number_02: number_01 * number_02
   return data

multiply = funct(4)

print (multiply(20))

class myclass:
    x=5

p1= myclass()
print (p1.x)

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

p2 = Person("John", 25)
print(p2.name)

print ('///////////////////////////////////////////// Play with List //////////////////')
thisset = ["apple", "banana", "cherry"]
mylist = ["kiwi", "orange", "apple", "cherry"]

