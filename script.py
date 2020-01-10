import sys

num1, num2 = float(sys.argv[1]), float(sys.argv[2])

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
    if num2 == 0:
        print("Unfortunately, b = 0")
    else:
        s = Numbers(num1, num2)
        print("Numbers: {} and {}".format(num1, num2))
        print("Sum: {}, mult: {}, div: {}".format(s.summ, s.multiple, s.division))