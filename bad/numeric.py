from __future__ import division


class number(object):

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other
        return self.value

    def __sub__(self, other):
        self.value -= other
        return self.value

    def __rsub__(self, other):
        self.value = other - self.value
        return self.value

    def __mul__(self, other):
        self.value *= other
        return self.value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other

    def __truediv__(self, other):
        self.value = self.value / other
        return self.value

    def __rtruediv__(self, other):
        self.value = other / self.value
        return self.value

    __str__ = __repr__
    __radd__ = __add__
    __rmul__ = __mul__
