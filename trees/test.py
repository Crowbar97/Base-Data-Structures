class Dog:
    def __init__(self):
        self.name = 'jack'
        self.nick = 'ralf'

    def __set_name(self, name='bob'):
        print('NEW NAME!')

    def _say(self):
        print('woof!')

d = Dog()
print(dir(d))
d._say()
d._Dog__set_name()
d.__set_name()