import sys
import socket
import struct
import time
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send

def generate_icmp_packet(destination_ip, identification, seq_number, payload):
    packet = IP(dst=destination_ip)/ICMP(id=identification, seq=seq_number)/payload
    return packet

def main():
    if len(sys.argv) != 4:
        print("Uso: python3 icmp_cesar.py <ip_destino> <texto> <corrimiento>")
        sys.exit(1)

    destination_ip = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])

    seq_number = 1

    for char in text:
        timestamp = int(time.time())  # Timestamp coherente
        id_value = seq_number  # Usar el número de secuencia como ID
        payload_data = char.encode()  # Convertir el carácter a bytes

        # Crear el payload ICMP siguiendo los requisitos
        payload = struct.pack('!QII', timestamp, id_value, seq_number) + payload_data

        # Enviar el paquete ICMP
        icmp_packet = generate_icmp_packet(destination_ip, id_value, seq_number, payload)
        send(icmp_packet, verbose=False)

        print(f"Enviado carácter '{char}' a {destination_ip}")

        seq_number += 1

if __name__ == "__main__":
    main()
