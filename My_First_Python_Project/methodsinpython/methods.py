'''
Created on Jun 4, 2022

@author: ytiani
'''
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
an arbitary choice and can be changed by any word of our choice. The function in args is type dictionary'''

def print_name(*args):
    return(f'hello {args[0]}, {args[1]} {args[2]}')

def print_names(*param):
    return(f'hello {param[0]}, {param[1]} {param[2]}')

print (print_name('Yves', 50, 'is old'))
print (print_names('John', 100, 'is very old'))

