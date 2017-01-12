
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from livereload import Server
from flask import request, abort, redirect

from core import app
from core.pages import page

from threading import Thread
import webview
import webbrowser


@app.route('/browser')
def browser():
	webbrowser.open_new('http://localhost:8080')
	
	return redirect('/start')


if __name__ == '__main__':
	if app.config['DEBUG']:

		thread = Thread(target=app.run, kwargs={'port': 8080, 'threaded': True, 'use_reloader': False})
		thread.daemon = True
		thread.start()

		webview.create_window('Class', 'http://localhost:8080/start')

	else:
		server = HTTPServer(WSGIContainer(app))
		server.listen(5000)
		IOLoop.instance().start()


