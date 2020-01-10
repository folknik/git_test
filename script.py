class Numbers(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b

    @property
    def summ(self):
        return self.sum


if __name__ == '__main__':
    s = Numbers(10, 15)
    print(s.summ)