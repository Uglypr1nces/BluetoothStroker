pyserver_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
print(f"Waiting for connection on RFCOMM channel {port}")

client_sock, address = server_sock.accept()
print(f"Accepted connection from {address}")

data = client_sock.recv(1024)
print("Received:", data.decode())

client_sock.close()
server_sock.close()
