from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime


class MyHttpRequestHandler(BaseHTTPRequestHandler):
    # Simple request handler, only supports GET.
    def do_GET(self):
        print('do_GET() starting to rpocess request')
        my_message = 'Hello from server at ' + str(datetime.today())
        byte_msg = bytes(my_message, 'utf-8')
        self.send_response(200)
        self.send_header("Content-type", 'text/plain; charset-utf-8')
        self.send_header('Content-length', str(len(byte_msg)))
        self.end_headers()
        print('do_GET() replying with message')
        self.wfile.write(byte_msg)


def main():
    print('Setting up server...')
    server_address = ('localhost', 8080)
    httpd = ThreadingHTTPServer(server_address, MyHttpRequestHandler)
    httpd.serve_forever()
    # after starting server, type localhost:8080 in the browser url bar to test


if __name__ == '__main__':
    main()
