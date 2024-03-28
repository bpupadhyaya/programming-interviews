import socketserver


class ThreadedEchoSevreer(
    socketserver.ThreadingMixIn,
    socketserver.TCPServer):
    """
    The RequestHandler class for the server
    """

    def __init__(self, request, client_address, server):
        print('Setup data')
        self. addresses = {
            'Guido': 'A20',
            'Richie': 'B30',
            'Gosling': 'E40'
        }
        super().__init__(request, client_address, server)

    def handle(self):
        print('In handle')
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).decode()
        print('DSata received: ', data)
        key = str(data)
        response = self.addresses[key]
        print('Response: ', response)
        # Send the result back to the client
        self.request.sendall(response.encode())


def main():
    print('Starting serverr...')
    server_address = ('localhost', 8084)
    print('Creating server')
    server = socketserver.TCPServer(server_address, ThreadedEchoSevreer)
    print('Activating server')
    server.serve_forever()


if __name__ == '__main__':
    main()


