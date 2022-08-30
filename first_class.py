class Animal:
    animal_type = "unknown"

    def __init__(self, fur_color):
        self.fur_color = fur_color

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print('im eating chips')

    def chase(self, animal='piranha'):
        print('im chasing', animal)

    def get_fur_color(self):
        print("getting fur color:", self.fur_color)


class HouseCat(Animal):
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("fur color was saved to the class object")
        self.animal_type = "house cat"
        print("animal type is:", self.animal_type)

    def speak(self):
        print('meow')

    def eat(self):
        super().eat()
        print('im eating tuna')

    def chase(self, animal):
        super().chase(animal)
        print(animal, 'was caught')


cat = HouseCat("blue")
