from math import sqrt

class Vector3:
	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	def __str__(self):
		return f"Vector3(x: {self.x}, y: {self.y}, z: {self.z})"

	def __repr__(self):
		return str(self)
	
	def __pos__(self):
		return Vector3(self.x, self.y, self.z)

	def __neg__(self):
		return Vector3(-self.x, -self.y, -self.z)

	def __eq__(self, right):
		if isinstance(right, Vector3):
			return self.x == right.x and self.y == right.y and self.z == right.z
		else:
			raise TypeError("unsupported operand type(s) for ==")

	def __ne__(self, right):
		if isinstance(right, Vector3):
			return not self == right
		else:
			raise TypeError("unsupported operand type(s) for !=")

	def __add__(self, right):
		t = type(right)
		if isinstance(right, Vector3):
			return Vector3(self.x + right.x, self.y + right.y, self.z + right.z)
		else:
			raise TypeError("unsupported operand type(s) for +")

	def __sub__(self, right):
		t = type(right)
		if isinstance(right, Vector3):
			return Vector3(self.x - right.x, self.y - right.y, self.z - right.z)
		else:
			raise TypeError("unsupported operand type(s) for -")

	def __mul__(self, right):
		t = type(right)
		if t in { int, float }:
			return Vector3(self.x * right, self.y * right, self.z * right)
		elif isinstance(right, Vector3):
			return Vector3(self.x * right.x, self.y * right.y, self.z * right.z)
		else:
			raise TypeError("unsupported operand type(s) for *")

	def __rmul__(self, left):
		return self * left

	def __truediv__(self, right):
		t = type(right)
		if t in { int, float }:
			return Vector3(self.x / right, self.y / right, self.z / right)
		elif isinstance(right, Vector3):
			return Vector3(self.x / right.x, self.y / right.y, self.z / right.z)
		else:
			raise TypeError("unsupported operand type(s) for /")
	

	@property
	def normalized(self):
		return self.normalize()

	@property
	def norm(self):
		return self.magnitude()


	def dot(self, vec):
		if isinstance(vec, Vector3):
			return self.x * vec.x + self.y * vec.y + self.z * vec.z
		else:
			raise TypeError("unsupported type(s) for Vector3.dot()")

	def cross(self, vec):
		if isinstance(vec, Vector3):
			return Vector3(self.y * vec.z + self.z * vec.y, self.z * vec.x + self.x * vec.z, self.x * vec.y + self.y * vec.x)
		else:
			raise TypeError("unsupported type(s) for Vector3.dot()")

	def sq_magnitude(self):
		return self.dot(self)

	def magnitude(self):
		return sqrt(self.sq_magnitude())

	def normalize(self):
		mag = self.magnitude()
		return Vector3(self.x / mag, self.y / mag, self.z / mag)
