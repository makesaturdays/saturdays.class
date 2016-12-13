
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from livereload import Server

from core import app
from core.compilers import compile_sass, compile_react


if __name__ == '__main__':
	if app.config['DEBUG']:
		server = Server(app.wsgi_app)
		server.watch(app.path+'/layouts/**/*.html')
		server.watch(app.path+'/react_scripts/*.js', func=compile_react)
		server.watch(app.path+'/styles/*.scss', func=compile_sass, delay='forever')
		server.watch(app.path+'/files/all.css')

		server.serve(port=8080, open_url_delay=1)

	else:
		server = HTTPServer(WSGIContainer(app))
		server.listen(5000)
		IOLoop.instance().start()