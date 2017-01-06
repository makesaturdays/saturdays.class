from core import app

import os
import sass
from babeljs import transformer


def compile_sass(input='/styles/all.scss', output='/files/all.css'):
	compiled = sass.compile(filename=app.path+input, output_style='compressed')

	file = open(app.path+output, 'w')
	file.write(compiled)
	file.close()

	return compiled


def compile_react(input='/react_scripts', output='/files/app.js'):
	compiled = ''
	for filename in os.listdir(app.path+input):
		file = open(app.path+input+'/'+filename, 'r')
		compiled += file.read()
		file.close()

	file = open(app.path+output, 'w')
	file.write(transformer.transform_string(compiled))
	file.close()

	return compiled
