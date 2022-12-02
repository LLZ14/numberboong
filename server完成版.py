# import socket
# import random
#
# def numcollect():
#     global io,num,num2,onum
#     num = random.choice(range(0,99999))
#     io = 0
#     onum = num
#     num2 = num
#     # 计算位数
#     while onum >= 1:
#         onum = onum / 10
#         io += 1
#     return io
#
#
# def theone():
#
#     weishu=numcollect()
#     # print("这是一个："+str(weishu)+"位数")
#     print("这是答案："+str(num))
#
#     server = socket.socket()
#     server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     server.bind(('10.1.30.100',9002))
#     server.listen()
#     #while语句作用：（当客户端关闭后）接受新客户端的连接，实现服务端不间断地提供服务。
#     while True:
#         conn,addr = server.accept()
#         #while语句作用：接受来自客户端的消息、打印，回复消息；当客户端的消息中包含‘bye’时，断开本次连接。
#         while True:
#             msg = conn.recv(1024).decode('utf-8')
#
#             # print.type(msg)
#             msgri=msg
#             mesg=str(msg)
#             # if isinstance(msg,str):
#             #     print("this is str type!")
#             #     # continue
#             if str(num) == msg:      #当收到的信息包含bye，给客户端发送bye，跳出当前while循环
#                 conn.send(b'binggo!you are right!')
#                 break
#             if msg == "1":
#                 fone=str(str(weishu)+"|"+str(num))
#                 print("用户连接成功！")
#                 print("这是一个"+str(weishu)+"位数")
#                 print("等待对方输入！")
#
#
#
#                 conn.send(str(fone).encode("utf-8"))
#             elif msg == "2":
#                 print("用户下线！")
#                 conn.close()
#                 break
#             elif msg !="1" and msg != "2":
#                 # print("这是一个"+str(weishu)+"位数")
#
#                 info1 = str(str(weishu)+"|"+str(num)+"|"+mesg)
#                 # if
#                 # print(info1)
#                 a2=info1.split("|")
#                 print(a2)
#                 # print(a2[1])
#                 print(a2[2])
#                 if int(a2[2])==num:
#                     print("你赢了")
#                     break
#
#                 if int(a2[2])<num:
#                     print("对方猜的是"+str(a2[2]))
#                     print("对方猜的小了")
#
#                 if int(a2[2])>num:
#                     print("对方猜的是"+str(a2[2]))
#                     print("对方猜的大了")
#
#
#                 if int(msgri)==num:
#                     print("对方猜的是"+str(a2[2]))
#                     print("你输了！")
#                 print("-----------------")
#                 info = input('该你输入了>>>')
#                 info = int(info)
#                 # print(info)
#                 if info == num:
#                     print("well!你赢了！！!")
#                     conn.send("over".encode('utf-8'))
#                     conn.close()
#                     break
#
#                 if info > num:
#                     print("oh!你猜猜小了!")
#                     print("等待对方输入！")
#                     # conn.send(str(info).encode('utf-8'))
#
#                 if info < num:
#                     print("oh!你猜猜小了!")
#                     print("等待对方输入！")
#
#                     # conn.send(str(info).encode('utf-8'))
#
#                 print("================")
#                 # print(info)
#                 # info=str(info)
#                 # info = str(str(info1)+"|"+str(info))
#                 # print(info)
#                 conn.send(str(info).encode('utf-8'))
#
#
#
# if __name__ == '__main__':
#     theone()
#
#
# # 判断类型
# # num = input("input your write:")
# # if isinstance(num,int):
# #     print("this is int type!")
# # elif isinstance(num,str):
# #     print("this is str type")
import socket
import random

def numcollect():
    global io,num,num2,onum
    num = random.choice(range(0,99999))
    io = 0
    onum = num
    num2 = num
    # 计算位数
    while onum >= 1:
        onum = onum / 10
        io += 1
    return io


def theone():
    weishu=numcollect()
    print("这是一个："+str(weishu)+"位数")
    print("这是答案："+str(num))

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('10.1.30.100',9002))
    server.listen(5)
    #while语句作用：（当客户端关闭后）接受新客户端的连接，实现服务端不间断地提供服务。
    # while True:
    conn,addr = server.accept()
        # msg1 = conn.recv(1024).decode("utf-8")
        # print(msg1)

        #while语句作用：接受来自客户端的消息、打印，回复消息；当客户端的消息中包含‘bye’时，断开本次连接。
    while True:
            msg = conn.recv(1024).decode('utf-8')

            # print.type(msg)
            msgri=msg
            mesg=str(msg)
            # if isinstance(msg,str):
            #     print("this is str type!")
            #     # continue
            if num == msg:      #当收到的信息包含bye，给客户端发送bye，跳出当前while循环
                conn.send(b'binggo!you are right!')
                break
            if msg == "1":
                fone=str(str(weishu)+"|"+str(num))
                print("用户连接成功！")
                print("等待对方输入！")

                conn.send(str(fone).encode("utf-8"))
            elif msg == "2":
                print("用户下线！")
                conn.close()
                break
            elif msg !="1" and msg != "2":
                print("这是一个"+str(num)+"位数")

                info1 = str(str(weishu)+"|"+str(num)+"|"+mesg)
                # if
                print(info1)
                a2=info1.split("|")
                print(a2)
                print(a2[1])
                # 对方的
                if int(a2[2])==num:
                    print("你输了")
                    break

                if int(a2[2])<num:
                    print("对方猜的是"+str(a2[2]))
                    print("对方猜的小了")

                if int(a2[2])>num:
                    print("对方猜的是"+str(a2[2]))
                    print("对方猜的大了")


                if int(msgri)==num:
                    print("对方猜的是"+str(a2[2]))
                    print("你输了！")

                info = input('该你输入了>>>')
                info = int(info)
                # print(info)
                if info == num:
                    print("well!你赢了！！!")
                    conn.send("over".encode('utf-8'))
                    conn.close()
                    socket.close()
                    break

                if info > num:
                    print("oh!你猜大了!")
                    print("等待对方输入！")
                    # conn.send(str(info).encode('utf-8'))

                if info < num:
                    print("oh!你猜小了!")
                    print("等待对方输入！")

                    # conn.send(str(info).encode('utf-8'))


                # print(info)
                info=str(info)
                info = str(str(info1)+"|"+str(info))
                # print(info)
                conn.send(info.encode('utf-8'))



if __name__ == '__main__':
    theone()


# 判断类型
# num = input("input your write:")
# if isinstance(num,int):
#     print("this is int type!")
# elif isinstance(num,str):
#     print("this is str type")
