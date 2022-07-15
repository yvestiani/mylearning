'Tiani', 'Yves''Tiani', 'Yves''''
Created on July 14th, 2022

@author: ytiani
'''
class LearnClass():
    
    def __init__(self, name, username):
        self.name = name
        self.username = username

    def list_myname(self):
        print(f'my mane is {self.name} and username {self.username}')

#create an instance of the class using object completename
completename = LearnClass('Tiani','Yves')
completename2 = LearnClass(True,False)

#After class instantiated, I can call method from class
completename.list_myname()
completename2.list_myname()

# Call the attribute of the class
print(completename.name)

print('\n////////////////////////////////Exercise Contruct class for dog ///////////////////////////\n')

class Dog:
   
    # Class Object Attribute
    species = 'mammal'
   
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

#instantiate the class Dog        
my_dog = Dog(breed='Kuttie', name="Denver")
#print breed
print(my_dog.breed)