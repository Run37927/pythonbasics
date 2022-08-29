class Animal:
    fur_color = 'orange'

    def speak(self):
        print('raaaawr')

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    def speak(self):
        print('meow')

class HouseCat(Animal):
    fur_color = 'black'
    def speak(self):
        print("hellow")

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)
