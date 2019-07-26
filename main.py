from modules.image import Image

def main():
	Image.output([
		[(1, 0, 1), (0, 1, 0), (1, 0, 1)],
		[(0, 1, 0), (1, 0, 1), (0, 1, 0)],
		[(1, 0, 1), (0, 1, 0), (1, 0, 1)]
	], lambda color: color * 255, "output")

if __name__ == "__main__":
	main()
