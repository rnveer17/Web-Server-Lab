# server.py
# Lab 2: Web Server Lab - Essentials of Health Informatics
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"Server is listening on port {serverPort} ...")

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    try:
        message = connectionSocket.recv(1024).decode()
        print("Request received:")
        print(message)

        filename = message.split()[1]
        print(f"Requested file: {filename}")

        f = open(filename[1:])          # strip leading '/'
        outputdata = f.read()
        f.close()

        # Send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print("Response sent.\n")

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>\r\n".encode()
        )
        connectionSocket.close()
        print("404 sent. Client closed.\n")

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data