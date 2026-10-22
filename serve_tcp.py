import socket
# inizializzazione socket ipv4 con TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind della porta e indirizzo ip
server_socket.bind(('localhost', 2211))
# mettere in ascolto il server 
server_socket.listen(5)
print("Server in ascolto su porta 2211...")
# 
while True:
# accettare richiesta
    client_socket, client_address = server_socket.accept()
    print(f"Connessione stabilita con il client: {client_address}")
# ricevere dati dal client
    data = client_socket.recv(1024)
    print(f"Dati ricevuti dal client: {data.decode()}")
#  mandare dati
    client_socket.send(b"Hello from server!")
# chiudere socket
    client_socket.close()
