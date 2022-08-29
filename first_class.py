class Animal:
    fur_color = 'orange'

    def speak(self):
        raise NotImplementedError
    def eat(self):
        pass

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print('meow')

cat = HouseCat()
cat.speak()