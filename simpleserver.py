# -*- coding: utf-8 -*-
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    try:
        address = ('', 8080)
        handler = SimpleHTTPRequestHandler
        server = HTTPServer(address, handler)
        print('Starting server, use <Ctrl-C> to stop')
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print('Server stopped.')


if __name__ == "__main__":
    main()
