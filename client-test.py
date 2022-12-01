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
 
    
    
"""
while True:
    info = input('>>>').encode("utf-8")

    client_01.send(info)
    print(info)
    msg = client_01.recv(1024).decode('utf-8')#接收信息
    print(msg)
    a=msg.split("|")
    print(a)
    info=int(info)
    print(info)
    # num=int(a[1])

    if msg == 'bye':  #当收到bye时，给服务器回复bye，跳出循环。
        client_01.send(b'bye')
        break

    # if info == num:  #当收到bye时，给服务器回复bye，跳出循环。
    #     client_01.send('you win!!'.encode("utf8"))
    #     break

    
client_01.close()
