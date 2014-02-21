from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        f = open(curdir + sep + self.path, 'rb')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f.read())
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()