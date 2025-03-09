import socket
import threading

HOST = "127.0.0.1"  # Server's IP address
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def send_messages():
    while True:
        message = input()
        client_socket.sendall(message.encode())

def receive_messages():
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print("Received:", message.decode())

# Start threads for sending and receiving messages
threading.Thread(target=send_messages).start()
threading.Thread(target=receive_messages).start()