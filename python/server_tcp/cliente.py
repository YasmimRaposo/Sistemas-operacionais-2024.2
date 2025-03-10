import socket
import sys

HOST, PORT = "10.25.2.25", 80
data = " ".join(sys.argv[1:])

# Criar um socket (SOCK_STREAM significa um socket TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Conectar ao servidor e enviar dados
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receber dados do servidor e encerrar
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))