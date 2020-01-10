class Numbers(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b
        self.mult = a * b

    @property
    def summ(self):
        return self.sum

    @property
    def multiple(self):
        return self.mult


if __name__ == '__main__':
    s = Numbers(10, 15)
    print(s.summ)
    print(s.multiple)