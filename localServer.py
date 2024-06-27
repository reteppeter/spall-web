import http.server
import socketserver
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Open the current directory as a server")
	parser.add_argument("port", default=8000, type=int, help="Port")
	args = parser.parse_args()

	Port = args.port

	Handler = http.server.SimpleHTTPRequestHandler
	Handler.extensions_map.update({
		".js": "application/javascript",
	})

	print("Running server at site:")
	print("http://localhost:{}/".format(Port))

	httpd = socketserver.TCPServer(("", Port), Handler)
	httpd.serve_forever()