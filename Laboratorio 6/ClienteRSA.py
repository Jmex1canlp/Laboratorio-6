import socket
import sys
import Crypto
import random
#funciones
#Descriptar
def PandQ():
        L=[]
        primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
        P= random.choice(primos)
        primos.remove(P)
        Q= random.choice(primos)
        L.append(P)
        L.append(Q)
        n=P*Q
        o=(P-1)*(Q-1)
        L.append(n)
        L.append(o)
        return L
def mcd(e,o):
    r=o%e
    while r!=0:
        o=e
        e=r
        r=o%e
    return e
#Variables
host = 'localhost'
port = 8050
#Creación de un objeto socket (lado cliente)
obj = socket.socket() 
#Conexión con el servidor.
obj.connect((host, port))
print("Conectado al servidor")
#variable
L=PandQ()
print(L)
P=L[0]
Q=L[1]
N=L[2]
O=L[3]
E=2
Le=[]
while E<O:
    m=mcd(E,O)
    if m==1:
        Le.append(E)
        E=E+1
    else:
        E=E+1
print(Le)
E=random.choice(Le)
K=1
r=(1+(K)*(O))%(E)
while r!=0:
    K=K+1
    r=(1+(K)*(O))%(E)
D=(1+(K)*(O))/(E)
#Llaves
print("------------Llaves privadas------------------\n")
print("La llave privada  es [",N,',',D,"]\n")
#Con el método send, enviamos llaves publicas al servidor que sincronizamos
NN=str(N)
DD=str(E)
obj.send(NN.encode('ascii'))
obj.send(NN.encode('ascii'))
print("------------Llave publica------------------\n")
print("La llave publica es [",N,',',E,"]\n")
print('**********************************************')

#recivimos el mensaje cifrado por parte del servidor
Peticion = obj.recv(1024)
#para posterior con la clave privada decifrar este mensaje el cual es.
print('conectando con servidor descriptando mensaje enviado por servidor')
l=[N,D]
mensaje_Descifrado=RSA.descifrarmensaje(Peticion,l)
print("\tMensaje Descifrado : "+str(mensaje_Descifrado))
file = open("mensajerecibido.txt", "w+")
    file.write(mensaje_Descifrado)
    file.close()
#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")
