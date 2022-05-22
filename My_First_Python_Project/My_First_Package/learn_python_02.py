'''
Created on Apr 23, 2022 to learn Python
Smal game to play with folks

@author: ytiani
'''

def firstnumber(number):
    while True:
        try:
            return float(number)
        except ValueError:
            number = input("enter the 1st number \n enter the valid number here: ")
            
def secondnumber(number):
    while True:
        try:
            return float(number)
        except ValueError:
            number = input ("enter the 2nd number \n enter the valid number here: ")

def multiply():
    first_num = input("enter the 1st number \n enter the valid number here: ")
    enteredNumberOne = firstnumber(first_num)
    second_num = input ("enter the 2nd number \n enter the valid number here: ")
    enteredNumberTwo = secondnumber(second_num)
    total = enteredNumberOne * enteredNumberTwo
    print ("your multiplication total is {:0.2f}. GOOD BYE!!!". format(total))
    
def switch_demo(argument):
    switcher = {
        2: "\nYou only have 2 more attempts. Please read the assignment well",
        3: "\nAre you really reading... come on!",
        4: "\nDon't be that stupid. Your are such a disappointment",
    }
    print (switcher.get(argument, "\nYou are too dump, even read you are incapable."
    +"\nPlease stop waiting our times and close the program by entering 'N'"))    


print("This exercise will multiply two numbers then give you the result."
+"\n Are you ready to get this started.If so! Let's go :)")
 
start = input("\nPlease type Y or N to get started (keep in mind, entering 'N' will close the program) : ")
 
if start == 'Y':
   multiply()  
elif start == 'N': 
  print ("Thank you for playing. Enjoy your day. Bye Bye!")
    
else:
 mylist = ['N', 'Y']
 i = 0

 while start not in mylist:
  valid = input ("\nplease enter the letter Y or N only. No other letters or sentences are allowed! " + 
 "\n Let's try again for the {} time. Please enter a valid entry: ".format(i + 2, switch_demo(i + 2))) 
  if valid == 'Y': 
    multiply()
    break

  elif valid == 'N': 
    print ("Thank you for playing. Enjoy your day. Bye Bye!")
    break     
  i += 1