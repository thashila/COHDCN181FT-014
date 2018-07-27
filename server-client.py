import socket, sys, argparse                         
from threading import *                       

a=argparse.ArgumentParser()
a.add_argument("serverip",nargs='?',type=str) 
a.add_argument("-p","--portno",type=int)
a.add_argument("-s","--ipadd",type=str) 
args = a.parse_args()


def getmsg(conn):

    try:
        while True:
            data=conn.recv(2048)
            print(data.decode("utf-8"))
                      
    except:
        print("Connection error occured")
        sys.exit()

def client():
    if args.serverip:
        if args.portno:
            print("Client Strated...")
            print("Connected to: "+ args.serverip + ":"+ str(args.portno))
            c=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                c.connect((args.serverip ,args.portno))

            except socket.error as e:
                print(str(e))

            t2=Thread(target=getmsg , args=(c,))
            t2.start()

            try:
                while True:
                    send=input()
                    c.sendall(send.encode("utf-8"))
                    if not send:
                        c.send("\n".encode("utf-8"))

            except:
                print("Connection error occured")
                sys.exit()

                
def server():
    if args.ipadd:
        if args.portno:
            print("Server Started...")
            print("Listing to: " +args.ipadd + " : " + str(args.portno))
            s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                s.bind((args.ipadd ,args.portno))

            except socket.error as e:
                print(str(e))


            s.listen()
            conn , addr=s.accept()
            print("Connected to: " + addr[0]+ " : " + str(addr[1])+ "\n")
            conn.send(str.encode("Connection Estabilished"))

            t1=Thread(target=getmsg , args=(conn,))
            t1.start()

            try:
                while True:
                    send=input()
                    conn.send(send.encode("utf-8"))
                    if not send:
                        conn.send("\n".encode("utf-8"))
            except:
                print("Connection error occured")
                sys.exit()

                                                 
            

server()
client() 
