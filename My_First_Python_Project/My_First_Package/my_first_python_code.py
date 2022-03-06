'''
I am the owner of this template

'''
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