'''
Created on Jun 4, 2022

@author: ytiani
'''
import string
print ('/////////call a function using a default value, so your function does not fail when calling the method//////')

def print_name(name='John'):
    print('hello '+name)

#  Here i'm passing the argument as yves.   
print_name('Yves')

''' Notice here when calling the method , I am not passing any argument. In his scenario, the function will use the default
parameter passed in the function which is John'''

print_name()

print ('//////////////////call a function using a return method//////////////////')

def print_name(name='John'):
    return('hello '+name)

print (print_name('Yves'))
a = print_name()
print(a)

print ('//////////////////logic in function: Print if number is even or uneven//////////////////')


def check_numbers(numb1):
    
    mod = numb1 % 2
    if (mod == 0):
      return (f'this number {mod} is even')
    else:
      return (f'this number {mod} is uneven')
    
print(check_numbers(51))

print ('//////////////////logic in function: Loop through a list and fetch even numbers//////////////////')

def check_numbers_list(mylist):
    evenlist = []
    for x in mylist: 
        mod2 = x % 2
        if (mod2 == 0):
            evenlist.append(x)
    return (f'Here is the list of even numbers you provided {evenlist}')
    
print(check_numbers_list([3,20,41,908,45,59,70]))

print ('\n//////////////////logic in function: Unpacking Tuple using function//////////////////')

mytuple = [('state_01', 'Georgia'),('state_02', 'Illinois'),('state_03', 'Virginia')]

def unpack_tuples(mytuple):
    for state, statename in mytuple:
         print(f'my {state} is {statename}')
    return 

unpack_tuples(mytuple)

''' Get the employee with max hours '''

work_hours = [('Abby',1000),('Billy',9000),('Cassie',8000)]

def max_employee(tupleunpack):
    employeemax = None
    currenthour = 0
    for employee , hours in tupleunpack:
        if hours > currenthour: 
           currenthour =  hours 
           employeemax = employee
    employee_of_month = (employeemax, currenthour)
    return employee_of_month
    # return print((employeemax, currenthour))

''' Tuple unpacking of function'''

employe_tuple = max_employee(work_hours)

employee, hours = employe_tuple
print(f'{employee} and {hours} hours cummulated')
# if __name__ == '__main__':
#     pass

''' Exercises on function '''
print ('\n//////////////////*args function //////////////////')

''' *args is used to pass in many arguments without having to defne the number of parameters. args is 
an arbritary choice and can be changed by any word of our choice. The function in args is type tuple'''

def print_name(*args):
    return(f'hello {args[0]}, {args[1]} {args[2]}')

def print_names(*param):
    return(f'hello {param[0]}, {param[1]} {param[2]}')

print (print_name('Yves', 50, 'is old'))
print (print_names('John', 100, 'is very old'))

print ('\n//////////////////**kwargs function //////////////////')

''' **kwargs is used to pass in many arguments without having to define the number of parameters. args is 
an arbitary choice and can be changed by any word of our choice. The function in **kwargs is type dictionary'''

def print_name(**kwargs):
    return(f'dict is: {kwargs}, {kwargs["name"]}, {kwargs["age"]}, {kwargs["nature"]}')

print (print_name(name= 'Yves', age =50, nature = 'is old'))

print ('\n//////////////////combine *args and **kwargs function //////////////////')

def print_name(*args, **kwargs):
    return(f'{args[0]}, age {kwargs["age"]}, {args[1]}') 

print (print_name('Yves', 'is old', age =50))

def myfunc(*args):
    mylist = [x for x in args if x%2 ==0]
    return mylist

print(myfunc(10,3,2,5))

'''Define a function called.  that takes in a string, and returns a matching string where every even 
letter is uppercase, and every odd letter is lowercase. 
Assume that the incoming string only contains letters, and don't worry about numbers, 
spaces or punctuation. The output string can start with either an uppercase or lowercase 
letter, so long as letters alternate throughout the string.
'''
def myfunc(name):
    newname = ''
    for x in range(len(name)):
        if x%2==0:
            newname = newname+(name[x].upper())
        else:
            newname = newname+(name[x].lower())
    return newname

'''using the join function to join string in list'''
def myfunc2(name2):
    newname = []
    for x in range(len(name2)):
        if x%2==0:
            newname.append(name2[x].upper())
        else:
            newname.append(name2[x].lower())
    return ''.join(newname)

print(myfunc('Anthropomorphism, don"t do it'))
print(myfunc2('Anthropomorphism'))

def up_low(s):
    countupper = 0
    countlower = 0
    for x in range (len(s)):
        if s[x].isupper(): 
            countupper +=1
        elif s[x].islower():
            countlower +=1
        else:
            pass

    return (f'No. of Upper case characters: {countupper}\nNo. of Upper case characters: {countlower}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print (up_low(s))

def unique_list(lst):
    return list(set(lst))

def unique_list2(lst):
    newlist = []
    for x in lst:
        if x not in newlist:
            newlist.append(x)
    return newlist
        

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print(unique_list2([1,1,1,1,2,2,3,3,3,3,4,5,5,5,5,5,]))

def print_big(letter):
    dic = {"A":['  *', ' * *', '*****', '*   *', '*   *']}
    
    for n in dic[letter]:   
        print(n)
    
print_big('A')