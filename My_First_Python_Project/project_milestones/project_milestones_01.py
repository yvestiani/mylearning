'''Finally let's combine all of these ideas to create a small game where a user can choose a "position" 
in an existing list and replace it with a value of their choice.'''
from IPython.core.display_functions import clear_output

def mylist():
    return [1,2,3]

def get_position_to_replace():
    mylist2 = mylist()
    inlist = 'notinlist'
    
    print(f'Please retain this current list {mylist2}. It will be replace by yours\n')
    
    while inlist not in mylist2:
        
        inlist = input(r'please enter the position you want to replace: ')
        # clear_output()
        
        if inlist.isdigit()== False:
            print('You did not enter a number (1,2,3)\n')

        elif inlist.isdigit()== True:
            if(int(inlist) in mylist2):
                return int(inlist)
            
def replace_position():
   mynewlist = mylist()
   position = get_position_to_replace()
   text = input(r'please enter the text you want to replace with: ')
   mynewlist[position-1] = text 
   print(f'Your current list is {mynewlist}')
   
def replay():
    mylist2 = ['Y', 'N']
    play = True
    
    replace_position()
        
    while play:
        inlist = input(r'Do you want to play again choose Y or N: ')
        # clear_output(wait=True)
        
        if inlist not in mylist2:
            print('please enter Y or N')

        elif inlist == 'Y':
            replace_position()
        elif inlist == 'N':
           print ('thank you for playing. Good Bye')
           break
replay()


   
   
   
