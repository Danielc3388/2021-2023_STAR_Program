class grandfather():
    def __init__(self):
        self.body = "weak"
        self.age = "60"

    def work(self):
        print("I can't work")


class father(grandfather):
    def __init__(self):
        self.body = "strong"
        self.age = "35"

    def work(self):
        print("I am working hard")


class son(father):
    def __init__(self):
        self.body = "small"
        self.age = "10"

    def play(self):
        print("I am playing")


john = father()
sam = son()

john.work()
sam.play()
sam.work()