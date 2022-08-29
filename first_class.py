class Animal:
    fur_color = 'orange'

    def speak(self):
        raise NotImplementedError
    def eat(self):
        print('im eating chips')
    def chase(self):
        raise NotImplementedError

class HouseCat(Animal):
    def speak(self):
        print('meow')

    def eat(self):
        super().eat()
        print('im eating tuna')

cat = HouseCat()
cat.eat()
