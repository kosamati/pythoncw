class animal:
    def __init__(self, n, t, c):
        self.name  = n
        self.type = t
        self.color = c
    def eat(self):
        print(f'{self.type} {self.name} zjadł obiad')
    def move(self):
        print(f'{self.type} {self.name} zmienił położenie')

if __name__ == "__main__":
    cat1 = animal("Pusia", "kot", "czarny")
    dog1 = animal("Azor", "Pies", "czarny")
    cat1.eat()
    dog1.move()

