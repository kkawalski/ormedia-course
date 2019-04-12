from math import pi


class Apple:

	def __init__(self, color, taste, kind, weight ):
		self.color = color
		self.taste = taste
		self.kind = kind
		self.weight = weight


class Circle:

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return pi*self.radius**2

circ = Circle(4)
print(circ.area())


class  Person():

	def __init__(self, first_name, last_name, qualification=1):
		self.first_name = first_name
		self.last_name = last_name
		self.qualification = qualification

	def __repr__(self):
		return "Employee {} {} is {}".format(self.first_name, self.last_name, self.qualification)


class Triangle:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c	

	def area(self):
		p = (self.a + self.b + self.c)/2
		return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

tri = Triangle(1, 2, 2)
print(tri.area())


class Rectangle():

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def calculate_perimetr(self):
		return (self.a + self.b)*2


class Square(Rectangle):

	def __init__(self, a):
		super().__init__(a, a)

	def calculate_perimetr(self):
		return super().calculate_perimetr()

	def change_size(self, ch):
		if ch + self.a < 1:
			print("Error")
			pass
		self.a += ch
		self.b += ch

sq = Square(4)
rec = Rectangle(3, 4)
print(sq.calculate_perimetr(), rec.calculate_perimetr())
