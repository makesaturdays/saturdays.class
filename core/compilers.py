from core import app

import sass
from babeljs import transformer


def compile_sass(input='/styles/all.scss', output='/files/all.css'):
	compiled = sass.compile(filename=app.path+input, output_style='compressed')

	file = open(app.path+output, 'w')
	file.write(compiled)
	file.close()

	return compiled


def compile_react(input='/react_scripts/app.js', output='/files/app.js'):
	compiled = transformer.transform(app.path+input)

	file = open(app.path+output, 'w')
	file.write(compiled)
	file.close()

	return compiled
