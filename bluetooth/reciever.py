import bluetooth

# Create a Bluetooth RFCOMM server socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 1))  # Bind explicitly to RFCOMM channel 1
server_sock.listen(1)

print("🔌 Waiting for Bluetooth connection on RFCOMM channel 1...")

# Make the service discoverable
bluetooth.advertise_service(
    server_sock,
    "RPiBTServer",  # Service name
    service_id="00001101-0000-1000-8000-00805F9B34FB",  # Standard SPP UUID
    service_classes=["00001101-0000-1000-8000-00805F9B34FB", bluetooth.SERIAL_PORT_CLASS],
    profiles=[bluetooth.SERIAL_PORT_PROFILE]
)

# Accept a connection
client_sock, client_info = server_sock.accept()
print(f" Accepted connection from {client_info}")

# Receive a message
try:
    data = client_sock.recv(1024)
    if data:
        print("📥 Received:", data.decode())
except Exception as e:
    print(f"❌ Error receiving data: {e}")

# Clean up
client_sock.close()
server_sock.close()
print(" Server closed.")
