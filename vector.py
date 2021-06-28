"""Módulo vector.py
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1+v2
    Vector(4, 5)
	
	branch test
"""

def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

def __mul__(self, scalar):
	return Vector(self.x * scalar, self.y * scalar)

def __abs__(self):
        return hypot(self.x, self.y)
