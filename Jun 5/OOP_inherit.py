class grandfather():
    def __init__(self):
        self.body = "weak"
        self.age = "60"

    def work(self):
        print("I can't work")


class father(grandfather):
    def __init__(self, body, age):
        super().__init__()
        self.body = body
        self.age = age

    def work(self):
        print("I am working hard")


class son(father):
    def __init__(self, body, age):
        super().__init__(body,age)

    def play(self):
        print("I am playing")


john = father("strong","25")
sam = son("small","10")

john.work()
sam.play()
sam.work()