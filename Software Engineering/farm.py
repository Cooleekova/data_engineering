class Goose:
    def __init__(self, name, weight, voice='Ga-ga-ga'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

    def egg(self):
        return f'Яйца собраны у гуся {self.name} {type(self)}'


grey_goose = Goose('Серый', 5)
white_goose = Goose('Белый', 5)


class Cow:
    def __init__(self, name, weight, voice='Moo!'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.5

    def say(self):
        print(self.voice)

    def milk(self, liter):
        self.weight -= liter


manya = Cow('Манька', 100)


class Sheep:
    def __init__(self, name, weight, voice='Bee!'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

    def wool(self, wool):
        self.weight -= wool


barashek = Sheep('Барашек', 60)
kudryaviy = Sheep('Кудрявый', 60)


class Chicken:
    def __init__(self, name, weight, voice='Ko-ko-ko'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

    def egg(self):
        return f'Я собрала яйца {self.name} {type(self)}'


koko = Chicken('koko', 3)
kukareku = Chicken('kukareku', 3)


class Goat:
    def __init__(self, name, weight, voice='Meee'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

    def milk(self, liter):
        self.weight -= liter


roga = Goat('Roga', 50)
kopyta = Goat('kopyta', 50)


class Duck:
    def __init__(self, name, weight, voice='Krya-krya'):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

    def egg(self):
        return f'Я собрала яйца {self.name} {type(self)}'


kryakva = Duck('Kryakva', 4)

# список всех животных на ферме
animals = [grey_goose, white_goose, manya, barashek, kudryaviy, koko, kukareku, roga, kopyta, kryakva]

# кормить всех животных
for animal in animals:
    if type(animal) == Goose or Chicken or Duck:
        animal.feed(1)
    elif type(animal) == Cow or Sheep or Goat:
        animal.feed(10)
    print(f'Я накормила {animal.name} {type(animal)}')

print()

# доить корову и коз
for animal in animals:
    if type(animal) == Cow or type(animal) == Goat:
        animal.milk(3)
        print(f'Я подоила {animal.name} {type(animal)}')

print()

# стричь овец
for animal in animals:
    if type(animal) == Sheep:
        animal.wool(2)
        print(f'Я постригла {animal.name} {type(animal)}')

print()

# собирать яйца гусей, кур и уток
for animal in animals:
    if type(animal) == Goose or type(animal) == Chicken or type(animal) == Duck:
        print(animal.egg())

print()

# голоса животных
for animal in animals:
    print(f'{animal.name} говорит {animal.voice}')

print()

# посчитать общий вес животных и вычислить самое тяжёлое животное
weight_sum = 0
for animal in animals:
    weight_sum += animal.weight
print(f'Общий вес всех животных на ферме: {int(weight_sum)} килограмм')

biggest = 0
biggest_name = ''
for animal in animals:
    if animal.weight > biggest:
        biggest = animal.weight
        biggest_name = animal.name
print(f'Самое тяжёлое живтоное - {biggest_name}, весит {biggest} кг')