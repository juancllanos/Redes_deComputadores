from socket import *

servidorNombre = "127.0.0.1"
servidorPuertoControl = 12000
#servidorPuertoConection = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuertoControl))

user = input("Ingrese su usuario: ")
clienteSocket.send(bytes('USER ' + user, "utf-8"))

pasw = input("Ingrese su password: ")
clienteSocket.send(bytes(pasw, "utf-8"))

mensajeRespuesta = clienteSocket.recv(1024)

print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))



clienteSocket.close()
