class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30) 
print(getattr(person, 'name','asres')) # John Doe 
print(getattr(person, 'age',20)) # 30 
print(getattr(person, 'city', 'merto le mariyam')) # Milano