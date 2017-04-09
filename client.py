import socket

# IP Server y puerto
host = "127.0.0.1"
port = 5035

def SocketReconnect(mySocket,host,port):
    try:
        mySocket.connect((host,port))
        return True       
    except:
        return False  
 
def Main():
    while True:

        print ('Conectando al servidor...')

        # Welcome 
        while True:
            try:
                mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mySocket.connect((host,port))
                data = mySocket.recv(1024).decode()
                if data:               
                    print (data)
                
                msgWelcome = mySocket.recv(1024).decode()
                if msgWelcome:               
                    print (msgWelcome)
                
                break        
            except:
                continue

        # Menu login/register
        while True:
            op_input = input('> ')

            try:
                mySocket.send(op_input.encode())
                data = mySocket.recv(1024).decode()
                
                if data:               
                    print (data)
                
                if op_input == 'salir':
                    mySocket.close()
                    return
            
            except:
                print ('Servidor desconectado')
                break

               
        while True:

            message = input('> ')

            if message == 'salir':
                print ('Desconectado')
                mySocket.close()
                return

            try:
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                if data:               
                    print ('Recibido por servidor: ' + data)
            
            except:
                print ('Servidor desconectado')
                break

            
    
 
if __name__ == '__main__':
    Main()