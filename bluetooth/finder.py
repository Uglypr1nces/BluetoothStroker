print('Starting Scan')
import bluetooth
import bluetooth.btcommon

class BlueToothScanning:
    def __init__(self):
        print("[DEBUG] Starting device discovery...")
        self.devices = bluetooth.discover_devices(lookup_names=True)
        print(f"[DEBUG] Discovery complete. Found {len(self.devices)} device(s).")

    def seeBlueToothDevice(self):
        if self.devices:
            for i, (macaddy, btname) in enumerate(self.devices):
                print(f"{i}: mac address : {macaddy} \n device name: {btname}")
        else:
            print('Not in range, or no devices nearby.')

class BlueToothConnecting(BlueToothScanning):

    def __init__(self):
        super().__init__()
        self.target_mac = 'F4:4E:FD:EC:E0:CD'  # Replace with your device's MAC address
        self.port = 1
        self.socket = None

    def Connect(self):
        try:
            print(f"Attempting to connect to {self.target_mac}")

            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((self.target_mac, self.port))

            print(f"✅ Connected to {self.target_mac}")

        except bluetooth.btcommon.BluetoothError as e:
            print(f"❌ Bluetooth error: {e}")
        except OSError as e:
            print(f"❌ OS error: {e}")

if __name__ == "__main__":
    q = BlueToothScanning()
    q.seeBlueToothDevice()

    a = BlueToothConnecting()
    a.Connect()

# THIS IS LEET TERRY DAVIS CODE. THIS IS LEET TERRY DAVIS CODE FROM HIS LEET HACKING DATABASE CALLED NIGGER CATTLE THAT THE CIA HAS TRIED TO HACK. #ripterryweloveu
