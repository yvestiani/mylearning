from random import shuffle
import random

print ('/////////////////////////////////////Play with list ////////////////////////')

guesses = list()
# test = ['','','','']

num = random.randint(1, 100)
print(num)

while True:
    userinput = abs(int(input("enter a number: ")))
    
    
    if num == userinput:
        print (f"Bravo! you've guessed correctly and it took you {len(guesses)} guess(es) to pass!")
        break;
       
    if userinput <1 or userinput > 100:
        print('OUT OF BOUNDS')
        continue
    
    guesses.append(userinput)

    
    if len(guesses) >1:
        if abs((num-userinput)) < abs((num-guesses[-2])):
           print("Warmer")
        else:
           print("Colder")
            
    else:
       if abs((num-userinput)) <= 10:
            print('Warm')
       else:
            print('Cold') 
        

mylist03 = [True, False, True]

'''Play with Zip function. Zip will only iterate up to the shortest list. The shortest list in my scenario is mylist03
'''
