from modules.image import Image
from modules.vector3 import Vector3

def main():
	print(Vector3(1, 2, 3))
	print(+Vector3(1, 2, 3))
	print(-Vector3(1, 2, 3))

	print(Vector3(1, 2, 3) is Vector3(1, 2, 3))
	print(Vector3(1, 2, 3) == Vector3(1, 2, 3))
	print(Vector3(1, 2, 3) != Vector3(2, 2, 3))

	print(Vector3(1, 2, 3) + Vector3(2, 2, 2))

	print(Vector3(1, 2, 3) - Vector3(2, 2, 2))

	print(Vector3(1, 2, 3) * Vector3(2, 2, 2))
	print(Vector3(1, 2, 3) * 2)
	print(2 * Vector3(1, 2, 3))

	print(Vector3(1, 2, 3) / Vector3(2, 2, 2))
	print(Vector3(1, 2, 3) / 2)

	print(Vector3(1, 2, 3).normalized)
	print(Vector3(1, 2, 3).norm)

	print(Vector3(1, 2, 3).dot(Vector3(2, 2, 2)))
	print(Vector3(1, 2, 3).cross(Vector3(2, 2, 2)))
	print(Vector3(1, 2, 3).sq_magnitude())
	print(Vector3(1, 2, 3).magnitude())
	print(Vector3(1, 2, 3).normalize())

	Image.output([
		[(1, 0, 1), (0, 1, 0), (1, 0, 1)],
		[(0, 1, 0), (1, 0, 1), (0, 1, 0)],
		[(1, 0, 1), (0, 1, 0), (1, 0, 1)]
	], lambda color: color * 255, "output")

if __name__ == "__main__":
	main()
