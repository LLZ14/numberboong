# import socket
# import random
# import threading
#
# # def receiveMessage():
# #     global s
# #     while True:
# #         #接收客户端发送的消息
# #         global addr
# #         data, addr = s.recvfrom(1024)
# #         data=data.decode('utf-8')
# #         if not data:
# #             print('client has exited!')
# #             break
# #         elif data == '连接服务器':
# #             print('client 连接服务器!')
# #         else:
# #             print('received:',data,'from',addr)
# #             p=data.split(",");
# #             x=int(p[0]);
# #             # y=int(p[1]);
# #             print(x)
# #
# #     s.close()
# # def sendMessage(pos):
# #     global s
# #     global addr
# #     s.sendto(pos.encode(),addr)
# #
# # def startNewThread( ):
# #
# #         thread=threading.Thread(target=receiveMessage,args=())
# #         thread.setDaemon(True);
# #         thread.start();
#
# def numcollect():
#     global io,num,num2,onum
#     num = random.choice(range(0,99999))
#     io=0
#     onum = num
#     num2 = num
#     #计算位数
#     while onum >= 1 :
#          onum=onum/10
#          io += 1
#     return io
#
#
# i=numcollect()
# txt = i
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# s.bind(('10.1.30.100', 8888))
# print('Bind UDP on 8888...')
# print(num)
# print(txt)
# while True:
#
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     print('received:',data)
#     p=data.decode('utf-8').split("[]");
#     x=int(p[0])
#     print(x)
#
#     # p=data
#     x=int(p[0]);
#     # y=int(p[1]);
#     # print(p[0],p[1])
#     # pos=str(x+1)+","+str(y+1)
#     pos=str(txt)
#     # pos1=str(num)
#
#     s.sendto(pos.encode('utf-8'),addr)
#     # s.sendto(pos1.encode('utf-8'),addr)
#     print(io)
#
# -*- coding: UTF-8 -*-
#2022.11.21
import socket
import threading
import random

def numcollect():
    global io,num,num2,onum,on
    num = random.choice(range(0,99999))
    io=0
    onum = num
    num2 = num
    #计算位数
    while onum >= 1 :
         onum=onum/10
         io += 1
    return io

def handle_client_request(service_client_socket, ip_port):

    global on
    # service_client_socket.send(b'on')

    while True:

        recv_data = service_client_socket.recv(1024)

        if recv_data:
            message = recv_data.decode()
            print(message)
            print(ip_port)
            print(on)
            print(num)

            service_client_socket.send("已接收...".encode())


        else:
            print("客户端下线了:", ip_port)
            print()
            break

    service_client_socket.close()

if __name__ == '__main__':

    global num,on

    on=numcollect()

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_server_socket.bind(("127.0.0.1", 9090))

    tcp_server_socket.listen(128)

    while True:

        # nu = 520
        # num = str(nu)
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端连接成功:", ip_port)
        service_client_socket.send(b'weclome')
        # service_client_socket.send(('this is :%s') %num.decode('utf-8').encode('utf-8'))
        sub_thread = threading.Thread(target=handle_client_request, args=(service_client_socket, ip_port))
        sub_thread.setDaemon(True)
        sub_thread.start()


    # tcp_server_socket.close()
