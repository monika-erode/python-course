import socket
import threading

# List to keep track of connected clients
clients = []

# Function to handle messages from a single client
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{address} says: {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to send a message to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Main server logic
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.29.159', 5555))  # Localhost + Port 5555
    server.listen()
    print("[SERVER STARTED] Listening for connections...")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
