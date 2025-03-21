import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    A classe manipuladora de requisições para nosso servidor.

    Ela é instanciada uma vez por conexão ao servidor e deve
    sobrescrever o método handle() para implementar a comunicação
    com o cliente.
    """

    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        # apenas envia de volta os mesmos dados, mas em maiúsculas
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "10.25.2.25", 80

    # Criar o servidor, vinculando ao endereço e porta especificados
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Ativar o servidor; isso manterá o servidor rodando até que
        # você interrompa o programa com Ctrl-C
        server.serve_forever()