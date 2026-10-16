import socket

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server] Listening on {HOST}:{PORT}...", flush=True)

while True:
    conn, addr = server_socket.accept()
    print(f"[Server] Connected by client address: {addr}", flush=True)
    
    data = conn.recv(1024)
    if data:
        print(f"[Server] Received: {data.decode()}", flush=True)
        conn.sendall(b"Hello from Server! Message received.\r")
    
    conn.close()
