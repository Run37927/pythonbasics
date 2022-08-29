class Animal:
    fur_color = 'orange'

    def speak(self):
        raise NotImplementedError
    def eat(self):
        raise NotImplementedError

    def chase(self):
        raise NotImplementedError

class HouseCat(Animal):
    def speak(self):
        print('meow')

    def eat(self):
        print('eating')

    def chase(self):
        print('chasing balls')

cat = HouseCat()
cat.eat()
cat.chase()