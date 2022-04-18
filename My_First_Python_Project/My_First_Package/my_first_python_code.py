'''
I am the owner of this template

'''
from test.test_contains import myset
print (round (19.9499959 * 28.99, 2))

w=10

print (type(w))

phrase = "Ighave an \nautomobile"
# phrase ="P"
print (phrase)

print (phrase[3:-13])
print (phrase[::3])

a = 'banana'
b = 3
d = "is 100f" 

''' Using float '''

c  = 100/777

''' Different print Formats '''

print ('{0} {1} {2}'.format (b,a,d))
print ('{0:.3f}'.format (c))
print (f'{b:2.2f} {a} {d}')

list_01 = ["one", "two", "tree"]

# Indexing
list_01[1]

# Concatenation
list_02 = [4, "five", 6, "seven"];

list_concat = list_01 + list_02
list_concat

# Slicing
list_concat[3:]

# Altering value in List
list_concat [1] = list_concat[1].upper();

# add at the end of list
list_concat.append('eight')

# Remove value from list
# list_concat.pop(1)

print (list_concat)

new_list_01 = ["1", "3", "5", "2", "4"]

'''Sort value '''

new_list_01.sort()
print (new_list_01)

''' Reverse value from list '''

new_list_01.reverse()
new_list_02 = new_list_01
print (new_list_02)

''' Dictionaries '''

my_dict = {'Color': 'blue', 'Make':'Toyota', 'Year':2009, 'Features':['radio','ABS', 20, 'Power'],
           'features_new':{'door':4, "type":'sedan', 'key':{'remote':'dual key', 'type':'electronic V2'}}}

print (my_dict['Features'])
print (my_dict['Features'][1])

''' Change value of the key color to upper cases BLUE and change it in the my_dict as well '''

color = my_dict['Color'].upper()
print (color)
my_dict['Color'] = color;
my_dict.get('Color', 'No Key for that')
print (my_dict);

''' Add new key/pair '''

add_new_key = {'Tires':{'types':['121/22/333', '17P']}}
tire_type = 'Michellin'
my_dict [tire_type] = add_new_key
print (my_dict)
print (my_dict ['Michellin'] ['Tires']['types'][1]);

''' Return Values only '''
print (my_dict.values());

''' Return keys only '''
print (my_dict.keys());

''' Return all items '''
print (my_dict.items());

''' Learn Tuple: Tuple is like a dictionnary, the only difference is that Tuple uses parenthesis where as
List uses square brackets '''

mytuple = (1, "two", 3.0, "four", 'four')
# count tuple
print (mytuple.count("four"))

# use index for tuple
print ("The lenght of my Tuple is {0} and the index 2 of my tuple {1} is {2}"
    .format(len(mytuple),  mytuple,   mytuple[2]))

''' Use of sets '''

myset = set()
myset.add ('2')
myset.add ('6')

''' Really useful to remove duplicate  from list '''
mylist4 = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
myset2 = set(mylist4)

print (myset2)
print (myset)

''' Complex number in python '''

print(complex(10, 20))  # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)

''' Boolean in Python values are True or False in first letter in Capital '''

isGreen = 'green';
tuple_color = ('Blue', 'Green')

print(tuple_color[1].__eq__(isGreen))

print ("//////////////////////////////set ///////////////////////////////////////////")

''' Set is different from dictionary because it does not have the key/value pair '''

mysets = set(my_dict);
print (mysets.__len__());

# print(mysets + '=>' + mysets[1]);
      
print ("//////////////////////////////////////////////////////// Play with List ////////////////////////////////////")

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

thislist.append("Berries")

thislist[1] = thislist[1].upper()

print ([thislist[0]] + [thislist [-1]])

for i in range (len(thislist)) :  
    
    print (thislist[i])

# for i in thislist :
''' Print the first and last value from the list to another list '''
last = [thislist[n] for n in (0,-1)]
print(last)

thislist = ["Data", "Salmon", "Nakerel"]

first_last = [thislist[n] for n in (0,1)]
print(first_last)
[print([thislist[n]]) for n in (0,1)]

''' List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
newlist = [expression for item in iterable if condition == True]
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != 'apple']

print(newlist)

mylist = [x for x in range (10) if x <=5]

print (mylist)

mylist1 = []
mylist2 = []
i = 0
while i < 10:
 if i <= 5:
  mylist1.append(i)
 i += 1
print ("mylist1 is {}" .format(mylist1))
    
for a in range (10):
 if a <= 5:
  mylist2.append(a)
print ("mylist2 is {}" .format(mylist2)) 

# mylist3 = mylist2 + mylist1
# mylist1 = mylist1.extend(mylist2)
print ("mylist3 is {}" .format(mylist2.append(mylist1))) 

