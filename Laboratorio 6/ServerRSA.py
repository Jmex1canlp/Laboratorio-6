import socket
import sys
import Crypto
import random
import RSA
#funciones    
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

#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Puerto y servidor que debe escuchar
ser.bind(("localhost", 8050))
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(5)
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
print(D)
while True:
        #Llaves
        conexion, addr = ser.accept()
        print('nueva conexion')
        print(addr)
        print("------------Sincronizando con cliente llaves publicas recividas------------------\n")
        Peticion = ser.recv(1024)
        N=int(Peticion)
        respuesta = ser.recv(1024)
        E=int(respuesta)
        print("------------Llave publica------------------\n")
        print("La llave publica es [",N,',',E,"]\n")
        print('**********************************************')
        file = open("mensajeentrada.txt", "r")
        L=[N,E]
        mensaje_entrada = str(file.readline())
        file.close()
        mensaje_cifrado=RSA.cifrarmensaje(mensaje_entrada,L)
        mensaje_cifrado=str(mensaje_cifrado)
        conexion.send(mensaje_cifrado.encode('ascii'))
        print('conectando con cliente para mandar mensaje de entrada cifrada')
#Cerramos la instancia del socket cliente y servidor
conexion.close()
