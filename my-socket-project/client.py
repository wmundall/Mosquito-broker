
import socket
import time

time.sleep(2)

# Try the full container name or service name
HOST = "socket-server"
PORT = 5000

print(f"[Client] Attempting to connect to {HOST}:{PORT}...", flush=True)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a 5-second timeout so it doesn't hang forever if it fails
    s.settimeout(5.0)
    
    s.connect((HOST, PORT))
    print("[Client] Connected successfully!", flush=True)
    
    message = b"AT Z\r"
    s.sendall(message)
    print(f"[Client] Sent: {message}", flush=True)
    
    response = s.recv(1024)
    print(f"[Client] Received reply: {response.decode()}", flush=True)
    s.close()

except socket.timeout:
    print("[Client ERROR] Connection timed out!", flush=True)
except Exception as e:
    print(f"[Client ERROR] Connection failed: {e}", flush=True)
