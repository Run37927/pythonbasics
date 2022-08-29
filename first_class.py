class Animal:
    fur_color = 'orange'

    def speak(self):
        print('raaaawr')

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    pass


tiger = Tiger()
tiger.speak()
