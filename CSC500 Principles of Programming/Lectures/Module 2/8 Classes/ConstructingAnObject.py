class Animal:
    def __init__ (self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type
    
    def name(self):
        return self._name
    
    def sound(self, change = None):
        if change: self._sound = change # allows change
        return self._sound
    
    def __str__(self):
        return f"\nThe {self.type()} is {self.name()} and says {self.sound()}\n"
    
def main():
    dog = Animal("dog", "kahlua", "woof")
    print(dog)
    dog.sound("bark")
    print(dog.name())

if __name__ == '__main__': main()
