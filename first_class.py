class Animal:
    fur_color = 'orange'

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print('im eating chips')

    def chase(self, animal='piranha'):
        print('im chasing', animal)


class HouseCat(Animal):
    def speak(self):
        print('meow')

    def eat(self):
        super().eat()
        print('im eating tuna')

    def chase(self, animal):
        super().chase(animal)
        print(animal, 'was caught')

cat = HouseCat()
cat.chase('tail')
