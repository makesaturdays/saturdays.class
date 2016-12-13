
import os

DEBUG = os.getenv('DEBUG', 'True')
if DEBUG.lower() == 'true':
	DEBUG = True

elif DEBUG.lower() == 'false':
	DEBUG = False