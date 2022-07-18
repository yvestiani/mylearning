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

class Animal:
   
    # Class Object Attribute
    species = 'mammal'
   
    def __init__(self,breed,name,noise):
        self.breed = breed
        self.name = name
        self.noise = noise

    def State(self):
        print(f'my animal type is {self.name}, his name is {self.breed} and the noise he makes is {self.noise}.' +
              f'The animal species type is {Animal.species}')

#instantiate the class Dog       
my_dog = Animal(breed='Kuttie', name="Dog", noise='WOOF')
my_cat = Animal(breed='Finnie', name="Cat", noise='Miaou')

#print breed
print(my_dog.breed)

# Create object using a method from a class
my_dog.State()
my_cat.State()

print('\n////////////////////////////////Inheritance ///////////////////////////\n')

class Animal():
    
    def __init__(self):
        print("Aninal Created")
        
    def animal_type(self, type=None):
        print('Animal type is ', type)
    
    def type_of_food(self, food=None):
        print("Animal food is ", food)
        
class NewAnimal(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('My new Animal Created')
        
    #Override the method from parent class Animal
    def animal_type(self, type=None):
        # Animal.animal_type(self, type='Wild Cat')
        print('this animal type is ', type)

mynewanimal = NewAnimal()
mynewanimal.animal_type()
mynewanimal.type_of_food('Cat Cereal')

print('\n////////////////////////////////Polymorphism ///////////////////////////\n')

class Animals():
    
    def __init__(self, sound = None, type = None):
        self.sound = sound
        self.type = type
    
    def AnimalSound(self):
        # print('my new animal sound')
        raise ThisIsAnError('This is an abstack class')
 
class Dog(Animals):
     
    def AnimalSound(self):
       return f'{self.sound} is the sound of this new {self.type} animal'
   
class Cat(Animals):

    def AnimalSound(self):
       return f'{self.sound}  is the sound of this {self.type} animal'

animal = Animals()
animal.AnimalSound()

cat = Cat(sound = 'Meaw! Meaw!', type = 'Cat')
dog = Dog('Woof! Woof!', 'Dog')
# dog.AnimalSound()
print(dog.AnimalSound())
print(cat.AnimalSound())



