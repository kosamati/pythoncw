class user:
    password = ""
    def __init__(self, use, pas):
        self.username = use
        self.password = pas
        

    def login(self, a ,b):
        if self.username == a and self.password == b:
            print("Zalogowano")
            return True
        else: 
            return False
def log():
    global c
    a = str(input("Poadj swoją nazwę: "))
    b = str(input("Podaj swoje hasło: "))
    c = u1.login(a, b)




if __name__ == "__main__":
    a = str(input("Poadj nową nazwę: "))
    b = str(input("Podaj nowe hasło: "))
    u1 = user(a, b)
    log()
    while c == False:
        print("Spróbuj ponownie")
        log()