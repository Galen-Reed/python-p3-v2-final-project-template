
class Patient:

    def __init__(self, id, name, breed, age, ):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str) and len(breed):
            self._breed = breed
        else:
            raise ValueError(
                "Breed must be a non-empty string"
            )
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and len(age):
            self._age = age
        else:
            raise ValueError(
                "Age must be an integer"
            )
    
