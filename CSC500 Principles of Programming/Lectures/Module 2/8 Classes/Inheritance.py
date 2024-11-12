class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']
    
    def type(self, change = None):
        if change: self._type = change
        try: return self._type
        except AttributeError: return None

    def name(self, change = None):
        if change: self._name = change
        try: return self._name
        except AttributeError: return None

    def sound(self, change = None):
        if change: self._sound = change
        try: return self._sound
        except AttributeError: return None

    def __str__(self):
        return f"\nThe {self.type()} is {self.name()} and says {self.sound()}\n"
    
class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
    
    def kill(self, str):
        print(f'{self.name()} will kill {str}')

def main():
    donald = Duck(name='donald', sound='quack')
    cat = Kitten(name="pip", sound="meow")
    print(donald)
    print(cat)
    cat.kill('someone')
    print(cat.name())

if __name__ == '__main__': main()