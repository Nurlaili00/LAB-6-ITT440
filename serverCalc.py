from multiprocessing import Process
import errno
import socket
import math
import sys
import time


print(r"""
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--
   WELCOME TO ONLINE PYTHON'S CALCULATOR
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--
               """)

def Log(x):
        print(f"|***|Calculating log({x})")
        x = int(x)
        try:
                answer = math.log(x)
        except:
                answer = "The calculation unsuccessful! Please try again..."

        return answer

def Sqrt(x):
        print(f"|***|Calculating square root of {x}")
        x = int(x)
        if(x >= 0):
                try:
                        answer = math.sqrt(x)
                except:
                        answer = "The calculation unsuccessful! Please try again..."
        else:
                answer = "The calculation unsuccessful! Cannot negative value!"

        return answer

def Exp(x):
        print(f"|***|Calculating exponential of {x}")
        x = float(x)
        try:
                answer = math.exp(x)
        except:
                answer = "The calculation unsuccessful! Please try again..."

        return answer


def process_start(s_sock):
        s_sock.send(str.encode('Connection is successful!!!\n'))
        while True:
                data = s_sock.recv(2048)

                data = data.decode('utf-8')
                try:
                        option, value1 = data.split(" ", 2)
                except:
                        print("Unable to calculate! Client is disconnected...\n")

                if not data:
                        break

                if(option == '1'): #log
                        answer = Log(value1)
                elif(option == '2'): #sqrt
                        answer = Sqrt(value1)
                elif(option == '3'):  #exp
                        answer = Exp(value1)

                message = "The answer is  %s." % str(answer)
                print("|***|Calculation Completed!\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                s_sock.sendall(str.encode(message))


        s_sock.close()

if __name__ == '__main__':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 8888))
        print("Listening input from clients...")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock, s_addr = s.accept()
                                p = Process(target = process_start, args = (s_sock,))
                                p.start()

                        except socket.error:
                                print('Socket error!')

        except Exception as e:
                print('An exception occured!')
                print(e)
                sys.exit(1)

        finally:
                s.close()
