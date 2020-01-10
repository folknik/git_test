class Numbers(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b
        self.mult = a * b
        self.div = a / b

    @property
    def summ(self):
        return self.sum

    @property
    def multiple(self):
        return self.mult

    @property
    def division(self):
        return self.div


if __name__ == '__main__':
    a = 10.0
    b = 15.0

    if b == 0:
        print("Unfortunately, b = 0")
    else:
        s = Numbers(a, b)
        print("Numbers: {} and {}".format(a, b))
        print("Sum: {}, mult: {}, div: {}".format(s.summ, s.multiple, s.division))