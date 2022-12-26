###12月了，赶紧做完吧
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
    print(weishu)
    print(num)

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',9002))
    server.listen()
    #while语句作用：（当客户端关闭后）接受新客户端的连接，实现服务端不间断地提供服务。
    while True:
        conn,addr = server.accept()
        #while语句作用：接受来自客户端的消息、打印，回复消息；当客户端的消息中包含‘bye’时，断开本次连接。
        while True:
            msg = conn.recv(1024).decode('utf-8')

            # print.type(msg)
            msgri=msg
            mesg=str(msg)
            # if isinstance(msg,str):
            #     print("this is str type!")
            #     # continue
            if num == int(msg):      #当收到的信息包含bye，给客户端发送bye，跳出当前while循环
                conn.send(b'binggo!you are right!')
                break

            info1 = str(str(weishu)+"|"+str(num)+"|"+mesg)
            # if
            print(info1)
            a2=info1.split("|")
            print(a2)
            print(a2[1])

            if int(msgri)==num:
                print("你输了！")
                break
            info = input('>>>')
            info = int(info)
            print(info)
            if info == num:
                print("well!you win!")
                conn.send("you lose !!!!".encode('utf-8'))

            if info > num:
                print("well!big one")
                conn.send(str(info).encode('utf-8'))

            if info < num:
                print("well!small one!")
                conn.send(str(info).encode('utf-8'))


            print(info)
            info=str(info)
            info = str(str(info1)+"|"+str(info))
            print(info)
            conn.send(info.encode('utf-8'))

if __name__ == '__main__':
    theone()

# 判断类型
# num = input("input your write:")
# if isinstance(num,int):
#     print("this is int type!")
# elif isinstance(num,str):
#     print("this is str type")
