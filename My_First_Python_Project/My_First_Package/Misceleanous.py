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

      
print('\n/////////////////////////////////////Play with Enumerate Function ////////////////////////')

zip01 = [print (x) for x in enumerate(mylist01)]
'''tuple unpacking means we can actually called the key and value of the tuple since the enumerate function
returns the value as tuple and from that tuple you can unpack
'''
zip02 = [print (actualvalue) for item, actualvalue in enumerate(mylist01)]
