class Cat ():
    #attribute
    species = 'mammal'
    
    # constructor
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        return "(%s is %d years old" % (self.name, self.age)

guster = Cat(self.name, 11)
bandit = Cat(self.name, 10)

print(guster.description())

   

        
