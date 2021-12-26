import socket

ClientSocket = socket.socket()
host = '192.168.56.5'
port = 8888

print('Waiting for connection...')
try:
        ClientSocket.connect((host, port))
except socket.error as e:
        print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

print(r"""
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--
   WELCOME TO ONLINE PYTHON'S CALCULATOR
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--
1. Logarithmic(Log) Expression
2. Square Root Expression
3. Exponential Expression

               """)

while True:

        status = 0
        while(status == 0):
                option = input("Please enter type of operation (1|2|3): ")
                if(option == '1'):
                        value1 = input("Please enter the value: ")
                        status = 1
                elif(option == '2'):
                        value1 = input("Please enter the value: ")
                        status = 1
                elif(option == '3'):
                        value1 = input("Please enter the value: ")
                        status = 1
                else:
                        print("Invalid input ! \nPlease enter again !\n")
                        status = 0


        Input = option + " " +  value1
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        print("\n")

ClientSocket.close()
