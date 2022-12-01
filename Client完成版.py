import socket

# username="2"
# username=int(username)

client_01 = socket.socket()
client_01.connect(('127.0.0.1',9002))


# client_01.send(username.encode("utf-8"))
# client_01.send(str(username).encode("utf-8"))

"""
    一开始定义客户端去连接服务器的时候需要发送的
    客户端点击连接按钮发送：
    1，用户名C1=02
    2,提取数据，将收到的信息分离，分别存起来，比如位数，num,利用分片，split分成列表，然后固定a[1]为位数，a[2]为num,a[0]是用户名，a[3]是自己的数据
    a[4]是服务端数据，ok
    3，编写程序，判断n输入是否==a[2],如果是就显示信息提示，退出循环，结束网络连接
    服务器接受到了消息：
    1，将用户名C1存起来  Sc1=C1 send=str(Sc1+"|"+位数+"|"+num+"|"+C1(传过来的数据))
    2,input !=num,提示结果, send=send+input
    3,
    
    
"""
def cone():
    while True:
        info = input('>>>').encode("utf-8")
        if int(info)==dana:
            print("you win!!")
            client_01.send(b'you lose!')
            break
        if int(info)<dana:
            print("you get small!!")
        if int(info)>dana:
            print("you get bigger!!")

        client_01.send(info)
        print(info)
        msg = client_01.recv(1024).decode('utf-8')#接收信息
        print(msg)
        if msg == "over":
            print("you lose!!")
            break
        a=msg.split("|")
        print(a)#a[you]
        # print(a[1])
        info=int(info)
        print(info)#33
        # num=int(a[1])
        b=a
        print(b)

        if msg == 'bye':  #当收到bye时，给服务器回复bye，跳出循环。
            client_01.send(b'bye')
            break

        # if info == num:  #当收到bye时，给服务器回复bye，跳出循环。
        #     client_01.send('you win!!'.encode("utf8"))
        #     break


    client_01.close()


if __name__ == '__main__':
    print("选择：")
    print("1，连接服务器")
    print("2，退出游戏")

    x=input("请选择：")
    if x=="1":
        myname = x.encode("utf-8")

        client_01.send(myname)
        print(myname)
        msg = client_01.recv(1024).decode('utf-8')#接收信息
        a=msg.split("|")
        print(msg)
        print(a)
        print("这是一个"+str(a[0])+"位数")
        print(int(a[1]))
        dana=int(a[1])
        cone()
    elif x=="2":
        print("退出成功！")
        client_01.close()
        
        
        
 

import socket

# username="2"
# username=int(username)

client_01 = socket.socket()
client_01.connect(('127.0.0.1',9002))


# client_01.send(username.encode("utf-8"))
# client_01.send(str(username).encode("utf-8"))

"""
    一开始定义客户端去连接服务器的时候需要发送的
    客户端点击连接按钮发送：
    1，用户名C1=02
    2,提取数据，将收到的信息分离，分别存起来，比如位数，num,利用分片，split分成列表，然后固定a[1]为位数，a[2]为num,a[0]是用户名，a[3]是自己的数据
    a[4]是服务端数据，ok
    3，编写程序，判断n输入是否==a[2],如果是就显示信息提示，退出循环，结束网络连接
    服务器接受到了消息：
    1，将用户名C1存起来  Sc1=C1 send=str(Sc1+"|"+位数+"|"+num+"|"+C1(传过来的数据))
    2,input !=num,提示结果, send=send+input
    3,
    
    
"""
def cone():
    while True:
        info = input('请输入》》》').encode("utf-8")
        if int(info)==dana:
            print("you win!!")
            client_01.send(b'you lose!')
            break
        if int(info)<dana:
            print("you get small!!")
            print("waiting optinal input!!!")
            client_01.send(info)

        if int(info)>dana:
            print("you get bigger!!")
            print("waiting optinal input!!!")
            client_01.send(info)


        # print(info)
        msg = client_01.recv(1024).decode('utf-8')#接收信息

        if msg == "over":
            print("you lose!!")
            break
        if msg!=str(dana):
            print("11111")
            break
        # if int(msg) == int(dana):
        #     print("对方猜的是"+str(msg))
        #     print("对方猜中了！")
        #     client_01.send("你输了".encode("utf-8"))
        # if int(msg) < int(dana):
        #     print("对方猜的是"+str(msg))
        #     print("对方猜小了！")
        # if int(msg) > int(dana):
        #     print("对方猜的是"+str(msg))
        #     print("对方猜大了！")

        a=msg.split("|")
        print(a)#a[you]
        # print(a[1])
        info=int(info)
        print(info)#33
        # num=int(a[1])
        b=a
        print(b)

        if msg == 'bye':  #当收到bye时，给服务器回复bye，跳出循环。
            client_01.send(b'bye')
            break

        # if info == num:  #当收到bye时，给服务器回复bye，跳出循环。
        #     client_01.send('you win!!'.encode("utf8"))
        #     break


    client_01.close()


if __name__ == '__main__':
    print("选择：")
    print("1，连接服务器")
    print("2，退出游戏")

    x=input("请选择：")
    if x=="1":
        myname = x.encode("utf-8")

        client_01.send(myname)
        print(myname)
        msg = client_01.recv(1024).decode('utf-8')#接收信息
        a=msg.split("|")
        print(msg)
        print(a)
        print("这是一个"+str(a[0])+"位数")
        print(int(a[1]))
        dana=int(a[1])
        cone()
        client_01.close()
    elif x=="2":
        print("退出成功！")
        client_01.close()

