from datetime import datetime
import os.path as path
from os import makedirs as mkdir

class Image:
	@classmethod
	def output(cls, array, f, dir="output"):
		if not path.isdir(path.abspath(dir)):
			mkdir(dir)
		filename = datetime.now().strftime("%Y%m%d-%H%M%S") + ".ppm"
		file = open(path.abspath(dir + "/" + filename), "w")

		width = len(array)
		height = 0 if width == 0 else len(array[0])
		ret = "P3\n"
		ret += str(width)
		ret += " "
		ret += str(height)
		ret += "\n"
		ret += "255\n"
		for col in array:
			for color in col:
				for i, value in enumerate(color):
					if i != 0:
						ret += " "
					ret += str(f(value))
				ret += "\n"
		
		file.write(ret)
		file.close()
