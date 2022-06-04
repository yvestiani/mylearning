from random import shuffle
print ('/////////////////////////////////////Play with list ////////////////////////')

mylist01 = ['a', 'b', 'c', 'd']
mylist02 = [1, 2, 3, 4]
mylist03 = [True, False, True]

'''Play with Zip function. Zip will only iterate up to the shortest list. The shortest list in my scenario is mylist03
'''
zip01 = [print (x) for x in zip(mylist01, mylist02, mylist03)]
zip02 = list(zip(mylist01, mylist02, mylist03))
print(zip02)
print("min is {min} and max is {max}".format(min=min(mylist02), max=max(mylist02)))


print ('\n/////////////////////////////////////Play with Random Function ////////////////////////')
'''Start by importing the Random libraries and inport Shuffle which is random python object'''

shuffle(mylist02) #This will generate the number in a random position within the list
mylist02.sort(key=None, reverse=True)
print(mylist02) 

print ('\n/////////////////////////////////////Play with List Comprehension ////////////////////////')
'''The list comprehension is used to simplify the for loop and basically reducing the for loop in one line'''
mylist = [x for x in range(10) if x%2==0] # This simple for comprehension create a list of number modulo of w or prime number'''
mylist2 = [x if x%2==0 else x%2==1 for x in range(10)] # With the if/else statement
mylist3 = [x**y for x in range(2) for y in range(5)] # with nested loop

print(f'{mylist} and with if/else statement {mylist2} and with nexted loop \n {mylist3}')

      
print('\n/////////////////////////////////////Play with Enumerate Function ////////////////////////')

zip01 = [print (x) for x in enumerate(mylist01)]
'''tuple unpacking means we can actually called the key and value of the tuple since the enumerate function
returns the value as tuple and from that tuple you can unpack
'''
zip02 = [print (actualvalue) for item, actualvalue in enumerate(mylist01)]

print(list(range(0,11,3)))