#Shane Harris
from socket import *
#Setting up server
HOST = '127.5.9.1'
serverPort = 54790
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((HOST, serverPort))
serverSocket.listen(1)
print('The server is Ready to recieve...')
print('IP: ',HOST)
print('serverPort',serverPort)
while 1:
	connectionSocket, addr = serverSocket.accept()
	try:
		print('Connected with: ',addr)
		print('connectionSocket: ',connectionSocket)
		acceptedRequest = connectionSocket.recv(1024).decode()
		print('Accepted Request: ',acceptedRequest)
		httpFile = acceptedRequest.split()[1]
		print("After split \n")
		print("The requested file: ",httpFile,'\n')
		file = open(httpFile[1:])
		print('Printing file',file)
		output = file.readlines()
		file.close()
		print('Printing output',output)
		connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
		for i in range(0, len(output)):
			connectionSocket.send(output[i].encode())
			connectionSocket.send('\r\n'.encode())
			print(output[i])
		connectionSocket.close()
	except IOError:
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
		connectionSocket.close()
