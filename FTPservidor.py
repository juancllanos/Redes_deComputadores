from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")

usrs = ['juanc','juanf', 'andres']
pasws = ['hi','sun', 'bye']

conexionSocket, clienteDireccion = servidorSocket.accept()
print("Conexión establecida con ", clienteDireccion)

usr = str( conexionSocket.recv(1024), "utf-8" )
if usr in usrs :
    print("Usuario ingresado correctamente ...")
    conexionSocket.send(bytes('Ingrese su contraseña: ', "utf-8"))
#conexionSocket.send(bytes('Ingrese su contraseña: ', "utf-8"))

psw = str( conexionSocket.recv(1024), "utf-8" )
if index(usrs) == pasws(index(usr)):
    conexionSocket.send(bytes('Contraseña Correcta', "utf-8"))
    while 1:

    print("Mensaje recibido de ", clienteDireccion)
    print('Mensaje Cliente ',mensaje)
    mensajeRespuesta = mensaje.upper() + " Maquina"
    print('Mensaje Respuesta ',mensajeRespuesta)
    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    conexionSocket.close()
