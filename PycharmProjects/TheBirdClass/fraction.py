def __add__(self, other):
    num = self.num * other.den + self.den * other.num
    den = self.den * other.den
    return Fraction(num, den)