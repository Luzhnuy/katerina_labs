import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('192.168.88.89', 5050))
client = []
print('Start Server')
while True:
    data, addres = sock.recvfrom(1024)
    print(data.decode('utf-8'))
    if addres not in client:
        client.append(addres)
        for clients in client:
            if clients == addres:
                continue
    sock.sendto(data,clients)
