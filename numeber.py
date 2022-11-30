import random

import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    msgbox.showinfo(title='消息提示框', message='登录成功')
    root.destroy()

def success_sign_tip():
    msgbox.showinfo(title='消息提示框', message='注册成功')
    root.quit()
    pass

def fail_tip():
    msgbox.showerror(title='错误消息框', message='用户名或密码错误')


def fail_sign_tip():
    msgbox.showerror(title='错误消息框', message='注册失败！')
    root.quit()
    pass
def fail_sign_tip_username():
    msgbox.showerror(title='错误消息框', message='用户名重复,注册失败！')
    root.quit()
    pass
def fail_sign_tip_pwd():
    msgbox.showerror(title='错误消息框', message='密码不一致,注册失败！')
    root.quit()
    pass
def fail_sign_tip_one():
    msgbox.showerror(title='错误消息框', message='请输入相关信息！！')
    root.quit()
    pass

def loginui():
    global input1, input2, root
    root = Tk()
    root.resizable(False, False)
    m = Menu(root)
    filemenu = Menu(m, tearoff="off")
    m.add_cascade(label='选择模式', menu=filemenu, command=lambda: [root.destroy(), main_soneui()])
    for item in ["游客"]:
        if item == "游客":
            filemenu.add_command(label=item, command=lambda: [root.destroy(), main_soneui_bad()])
    root.my_font = font.Font(font=("华文行楷", 25, font.BOLD))
    root.my_font_two = font.Font(font=("宋体", 15, font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width'] = 580;
    root['height'] = 300;
    Label(root, text='登录界面', width=40, font=root.my_font).place(x=2, y=25)
    Label(root, text='用户名', width=35, font=root.my_font_two).place(x=2, y=100)
    input1 = Entry(root, width=32)
    input1.place(x=240, y=100)
    Label(root, text='密码', width=35, font=root.my_font_two).place(x=2, y=160)
    input2 = Entry(root, width=32, show="*")
    input2.place(x=240, y=160)
    Button(root, text='登录', width=6, font=root.my_font_two, command=login).place(x=235, y=210)
    Button(root, text='注册', width=6, font=root.my_font_two, command=lambda: [root.destroy(), sign_in()]).place(x=373,y=210)
    root['menu'] = m
    root.mainloop()
def sign_in():
    global inputone, inputtwo, inputthree, inputf,root
    root = Tk()
    root.resizable(False, False)
    root.my_font = font.Font(font=("华文行楷", 25, font.BOLD))
    root.my_font_two = font.Font(font=("宋体", 15, font.BOLD))
    root.my_font_th = font.Font(font=("宋体", 12, font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width'] = 580;
    root['height'] = 300;
    Label(root, text='注册界面', width=40, font=root.my_font).place(x=2, y=25)
    Label(root, text='用户名', width=35, font=root.my_font_two).place(x=2, y=100)
    inputone = Entry(root, width=32)
    inputone.place(x=240, y=100)
    Label(root, text='密码', width=35, font=root.my_font_two).place(x=2, y=160)
    # inputtwo=Entry(root,width=32,show="*")
    inputtwo = Entry(root, width=32)
    inputtwo.place(x=240, y=160)
    Label(root, text='密码', width=35, font=root.my_font_two).place(x=2, y=220)
    # inputthree=Entry(root,width=32,show="*")
    inputthree = Entry(root, width=32)
    inputthree.place(x=240, y=220)
    Label(root, text='手机号', width=35, font=root.my_font_two).place(x=2, y=280)
    inputf = Entry(root, width=32)
    inputf.place(x=240, y=280)
    Button(root, text='返回登录', width=8, font=root.my_font_th, command=lambda: [root.destroy(),loginui()]).place(x=235, y=310)
    Button(root, text='注册', width=8, font=root.my_font_th, command=sign).place(x=380, y=310)
    root.mainloop()
# def get_proe():
#   global txt1
#   proe = requests.get("http://yijuzhan.com/api/word.php?m=json")
#   if proe.status_code != 200:
#     return get_proe()
#   re1 = proe.json()['content']
#   re2 = proe.json()['source']
#   txt1= re1

  # return re1+re2
def login():
    global to,username,fLag
    db = pymysql.connect(host='localhost', user='root', password='', database='st', port=3306)
    cur = db.cursor()  # 获取操作游标
    sql = 'SELECT * FROM user'
    entry1 = input1.get()
    entry2 = input2.get()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    for row in results:
        username = row[0]
        password = row[1]
        print(username)
        print(password)
        if username == entry1 and password == entry2:
            print('登陆成功')
            # to = 1
            username = row[0]
            success_tip(username)
            flag = True
            main_soneui()
            break
        else:
            flag = False
    if flag == False:
        fail_tip()
def sign():
    global flag
    db = pymysql.connect(host='localhost', user='root', password='', database='st', port=3306)
    cur = db.cursor()  # 获取操作游标
    sql = 'SELECT * FROM user'
    entryo = inputone.get()
    entryt = inputtwo.get()
    entryth = inputthree.get()
    entryf = inputf.get()
    # flag = True
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    for row in results:
        username = row[0]
        password = row[1]
        print(username)
        print(password)
        if entryo !="":
            if username == entryo:
                flag = False
                print('注册失败！用户名重复！')
                fail_sign_tip_username()
                break
            else:
                if entryt == entryth:
                    flag = True
                    cur.execute('insert into user (username,pwd,tel) values ("%s","%s","%s")' % (entryo, entryt, entryf))
                    break
                else:
                    flag = False
                    fail_sign_tip_pwd()
                    break
        else:
            fail_sign_tip_one()
            flag = False
            break
    if not flag:
        root.destroy()
        sign_in()
    else:
        success_sign_tip()
        root.destroy()
        loginui()


def loginfalse():
    print(111)


def tryone():
    print(111)


def hello1():
    print("6666")
def  btnClicked1():
    global entryCd,labelHello,cd,message,txt1,num2
    cd = int(entryCd.get())
    labelHello.config(text = "你输入的数字是：%d " %cd)
    print(cd)
    txt1=cd
    x=cd
    message=str(cd)
    sk.send(message.encode())
def  btnClicked():
    global entryCd,labelHello,cd,message,txt1,opnum,num2
    cd = int(entryCd.get())
    opnum.config(text = "你输入的数字是：%d " %cd)
    print(cd)
    txt1=cd
    x=cd
    message=str(cd)
    if x > num2:
        update_big()
    if x < num2:
        update_small()
    if x==num2:
        update()
    return 0
    # print("答对了，恭喜，今晚你请客！")
    # print("一共回答了",j,"次")
    # print(message)
    # sk.send(message.encode())


def com():
    global inputCd,mynum,root1
    cd = float(inputCd.get())
    mynum(root1,text="%.2f" % cd)
    msgbox.showinfo("提示", "b小了! !")

    # elif num > 20:
    #     update_big()

def hello():
    msgbox.showinfo("提示", "welcome to use this tool!")
def update():
    msgbox.showinfo("提示", "答对了，你太厉害了666! !")
def update_big():
    msgbox.showinfo("提示", "比它大了，你小脑瓜子怎么想的!")
def update_small():
    msgbox.showinfo("提示", "比它小了，你大脑瓜子怎么想的! !")
def update_binggo():
    msgbox.showinfo("提示", "太棒了"+username+"你是怎么想到的! !")
def main_soneui():
    global inputCd,mynum,root1,sk
    global entryCd,labelHello,cd,message,txt1


    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷", 30, font.BOLD))
    root1.my_fonto = font.Font(font=("宋体", 15, font.BOLD))
    root1.resizable(False, False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")

    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host ="127.0.0.1"
    port = 9090

    sk.connect((host, port))
    message = "connect······"
    msgbox.showinfo(title='提示消息框', message=message)

    sk.sendall(message.encode('utf-8'))
    msgbox.showinfo(title='提示消息框', message=sk.recv(1024).decode())

    # i = 0
    # while i<1:
    #     try:
    #         # message = input(">>>")
    #         # sk.send(message.encode())
    #         # print(sk.recv(1024).decode('utf-8'))
    #         xo=sk.recv(1024).decode('utf-8')
    #     except KeyboardInterrupt:
    #         break
    #
    # sk.close()




    m = Menu(root1)
    filemenu = Menu(m, tearoff="off")
    filemenu1 = Menu(m, tearoff="off")

    m.add_cascade(label='菜单', menu=filemenu)
    m.add_cascade(label='主题', menu=filemenu1)
    for item in ["个人信息", "游戏大厅", '返回登录界面', "帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item, command="")
        if item == "游戏大厅":
            filemenu.add_command(label=item, command="")
        if item == "帮助":
            filemenu.add_command(label=item, command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item, command=lambda: [root1.destroy(), loginui()])

    for item in ['暗黑', '明亮']:

        if item == "暗黑":
            filemenu1.add_command(label=item, command="")
        if item == "明亮":
            filemenu1.add_command(label=item, command="")
    # get_proe()
    txt='！！！欢迎来到数字大爆炸！！！'
    mainnum = ''
    root1['menu'] = m

    Label(root1, text=txt,heigh=2, width=35,font=root1.my_font).place(x=10,y=10)
    num=Label(root1, text=mainnum,bg='#3f8dbb' ,heigh=2,width=60,font=root1.my_fonto).place(x=26,y=110)
    labelHello=tk.Label(root1, text="txt1",bg='#3f8dbb' , heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum=Label(root1, text="txt1",bg='#3f8dbb' , heigh=2,width=60,font=root1.my_fonto).place(x=26,y=230)
    Label(root1, text='请输入你要猜的数字:',font=root1.my_fonto, width=22).place(x=246, y=280)
    entryCd=Entry(root1, width=36)
    entryCd.place(x=240, y=310)


    # cd1=cd
    # print(cd)

    # message=str(cd)
    # print(message)
    # sk.send(message.encode())
    # xo=sk.recv(1024).decode('utf-8')
    # Button(root1, text='确定', width=8, command=com,font=root1.my_fonto).place(x=310, y=350)
    btnCal=Button(root1, text='确定', width=8, command = btnClicked1,font=root1.my_fonto)
    btnCal.place(x=310, y=350)



    root1.mainloop()

def numcollect():
    global io,num,num2,onum
    num = random.choice(range(0,99999))
    io=0
    onum = num
    num2 = num
    #计算位数
    while onum >= 1 :
         onum=onum/10
         io += 1
    return io


def main_soneui_bad():
    global inputCd,mynum,root1,sk
    global entryCd,labelHello,cd,message,txt1,opnum,num2


    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷", 30, font.BOLD))
    root1.my_fonto = font.Font(font=("宋体", 15, font.BOLD))
    root1.resizable(False, False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")


    m = Menu(root1)
    filemenu = Menu(m, tearoff="off")
    filemenu1 = Menu(m, tearoff="off")

    m.add_cascade(label='菜单', menu=filemenu)
    m.add_cascade(label='主题', menu=filemenu1)
    for item in ["个人信息", "游戏大厅", '返回登录界面', "帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item, command="")
        if item == "游戏大厅":
            filemenu.add_command(label=item, command="")
        if item == "帮助":
            filemenu.add_command(label=item, command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item, command=lambda: [root1.destroy(), loginui()])

    for item in ['暗黑', '明亮']:

        if item == "暗黑":
            filemenu1.add_command(label=item, command="")
        if item == "明亮":
            filemenu1.add_command(label=item, command="")

    numBig=numcollect()
    print(num2)
    nu = str(numBig)
    nu = "该数字的位数是:"+nu
    txt='！！！欢迎来到数字大爆炸！！！'
    mainnum = '登录解锁对战玩法'
    root1['menu'] = m

    Label(root1, text=txt,heigh=2, width=35,font=root1.my_font).place(x=10,y=10)
    num=Label(root1, text=mainnum,bg='#3f8dbb' ,heigh=2,width=60,font=root1.my_fonto).place(x=26,y=110)
    labelHello=tk.Label(root1, text=nu,bg='#3f8dbb' , heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum=Label(root1, text="txt2",bg='#3f8dbb' , heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    Label(root1, text='请输入你要猜的数字:',font=root1.my_fonto, width=22).place(x=246, y=280)
    entryCd=Entry(root1, width=36)
    entryCd.place(x=240, y=310)


    btnCal=Button(root1, text='确定', width=8, command = btnClicked,font=root1.my_fonto)
    btnCal.place(x=310, y=350)



    root1.mainloop()


if __name__ == '__main__':
   
    loginui()

import socket

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
        print(msg)
        if 'bye' in msg:      #当收到的信息包含bye，给客户端发送bye，跳出当前while循环
            conn.send(b'bye')
            break
        info = input('>>>').encode('utf-8')
        conn.send(info)
conn.close()

server.close()


import socket

client_01 = socket.socket()
client_01.connect(('127.0.0.1',9002))

while True:
    info = input('>>>').encode('utf-8')
    client_01.send(b'from c1:'+info)
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    if msg == 'bye':  #当收到bye时，给服务器回复bye，跳出循环。
        client_01.send(b'bye')
        break
client_01.close()


# import socket,threading
#
# # 导入socket模块
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# i=0
# trun = 0
# mynum=-1
# # data="01"
# # s.sendto(data.encode('utf-8'), ('10.1.30.100', 8888))
# # addr = '10.1.30.100'
# while i < 2 :
#     # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     x=input("请输入你猜的数字：")
#     # # if
#     # # y= input("请输入y坐标")
#     #data=str(x)+","+str(y)
#     data=str(x)
#     s.sendto(data.encode('utf-8'), ('10.1.30.100', 8888))
#     # 接收服务器数据:
#     data2, addr = s.recvfrom(1024)
#     p=data2.decode('utf-8')
#     tr=p+'位数'
#     # y=int(p[0])
#     print("该数是: " , data2.decode('utf-8')) 	# decode()解码
#     print(tr)
#     data, addr = s.recvfrom(1024)
#     # print('Received from %s:%s.' % addr)
#     # print('received:',data)
#     # x=input("请输入你猜的数字：")
#     # # if
#     # # y= input("请输入y坐标")
#     # # data=str(x)+","+str(y)
#     # data1=str(x)
#     # s.sendto(data1.encode('utf-8'), ('10.1.30.100', 8888))
# -*- coding: UTF-8 -*-
# import socket               # 导入 socket 模块
#
# if __name__ == '__main__':
#     sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # 创建 socket 对象
#
#     host ="192.168.36.36"
#     port = 9090
#
#     sk.connect((host, port))
#     message = "connect······"
#     sk.sendall(message.encode('utf-8'))
#     print(sk.recv(1024).decode())
#
#     i = 0
#     while True:
#         try:
#             message = input(">>>")
#             sk.send(message.encode())
#             print(sk.recv(1024).decode('utf-8'))
#         except KeyboardInterrupt:
#             break
#
#     sk.close()

import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk


def success_tip(username):
    global onw_username,sk,host,port
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = "10.1.30.100"
    port = 9090

    sk.connect((host,port))

    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    serverone_name = onw_username
    sk.send(serverone_name.encode())
    root.destroy()
    main_soneui()

def success_tip1():
    global onw_username,sk,host,port
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # host = "10.1.30.100"
    # port = 9090

    sk.connect((host,port))

    serverone_name = onw_username
    sk.send(serverone_name.encode())
    root1.destroy()
    main_soneui()


def success_sign_tip():
    msgbox.showinfo(title='提示',message='注册成功')
    root.quit()
    pass


def fail_tip():
    msgbox.showerror(title='错误消息框',message='用户名或密码错误')


def fail_sign_tip():
    msgbox.showerror(title='错误消息框',message='注册失败！')
    root.quit()
    pass


def fail_sign_tip_username():
    msgbox.showerror(title='注册失败',message='用户名重复!!！')
    pass


def fail_sign_tip_pwd():
    msgbox.showerror(title='注册失败',message='密码不一致！！')
    root.quit()
    pass


def fail_sign_tip_one():
    msgbox.showerror(title='错误消息框',message='请输入相关信息！！')
    root.quit()
    sign_in()
    pass


def loginui():
    global input1,input2,root
    root = Tk()
    root.resizable(False,False)
    m = Menu(root)
    filemenu = Menu(m,tearoff="off")
    m.add_cascade(label='选择模式',menu=filemenu,command=lambda: [root.destroy(),main_soneui()])
    for item in ["单机"]:
        if item == "单机":
            filemenu.add_command(label=item,command=lambda: [root.destroy(),main_soneui_bad()])
    root.my_font = font.Font(font=("华文行楷",25,font.BOLD))
    root.my_font_two = font.Font(font=("宋体",15,font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width'] = 580;
    root['height'] = 300;
    Label(root,text='登录界面',width=40,font=root.my_font).place(x=2,y=25)
    Label(root,text='用户名',width=35,font=root.my_font_two).place(x=2,y=100)
    input1 = Entry(root,width=32)
    input1.place(x=240,y=100)
    Label(root,text='密码',width=35,font=root.my_font_two).place(x=2,y=160)
    input2 = Entry(root,width=32,show="*")
    input2.place(x=240,y=160)
    Button(root,text='登录',width=6,font=root.my_font_two,command=login).place(x=235,y=210)
    Button(root,text='注册',width=6,font=root.my_font_two,command=lambda: [root.destroy(),sign_in()]).place(x=373,y=210)
    root['menu'] = m
    root.mainloop()


def sign_in():
    global inputone,inputtwo,inputthree,inputf,root
    root = Tk()
    root.resizable(False,False)
    root.my_font = font.Font(font=("华文行楷",25,font.BOLD))
    root.my_font_two = font.Font(font=("宋体",15,font.BOLD))
    root.my_font_th = font.Font(font=("宋体",12,font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width'] = 580;
    root['height'] = 300;
    Label(root,text='注册界面',width=40,font=root.my_font).place(x=2,y=25)
    Label(root,text='用户名',width=35,font=root.my_font_two).place(x=2,y=100)
    inputone = Entry(root,width=32)
    inputone.place(x=240,y=100)
    Label(root,text='密码',width=35,font=root.my_font_two).place(x=2,y=160)
    # inputtwo=Entry(root,width=32,show="*")
    inputtwo = Entry(root,width=32)
    inputtwo.place(x=240,y=160)
    Label(root,text='密码',width=35,font=root.my_font_two).place(x=2,y=220)
    # inputthree=Entry(root,width=32,show="*")
    inputthree = Entry(root,width=32)
    inputthree.place(x=240,y=220)
    Label(root,text='手机号',width=35,font=root.my_font_two).place(x=2,y=280)
    inputf = Entry(root,width=32)
    inputf.place(x=240,y=280)
    Button(root,text='返回登录',width=8,font=root.my_font_th,command=lambda: [root.destroy(),loginui()]).place(x=235,y=310)
    Button(root,text='注册',width=8,font=root.my_font_th,command=sign).place(x=380,y=310)
    root.mainloop()


def get_proe():
    global txt2
    proe = requests.get("http://yijuzhan.com/api/word.php?m=json")
    if proe.status_code != 200:
        return get_proe()
    re1 = proe.json()['content']
    re2 = proe.json()['source']
    txt2 = re1


def get_proe1():
    global mainnum
    proe = requests.get("http://yijuzhan.com/api/word.php?m=json")
    if proe.status_code != 200:
        return get_proe()
    re1 = proe.json()['content']
    re2 = proe.json()['source']
    mainnum = re1

    # return re1+re2


def login():
    global to,username1,flag
    db = pymysql.connect(host='localhost',user='root',password='',database='st',port=3306)
    cur = db.cursor()  # 获取操作游标
    sql = 'SELECT * FROM user'
    entry1 = input1.get()
    entry2 = input2.get()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    for row in results:
        username1 = row[0]
        password1 = row[1]
        print(username1)
        print(password1)
        if username1 == entry1 and password1 == entry2:
            print('登陆成功')
            # to = 1
            username1 = row[0]
            success_tip(username1)
            flag = True
            # get_proe1()
            # main_soneui()
            break
        else:
            flag = False
    if flag == False:
        fail_tip()


def sign_two_pwd(entryo,entryt,entryth,entryf):
    global cur,flag1
    if entryt == entryth:
        # flag1 = 1
        cur.execute('insert into user (username,pwd,tel) values ("%s","%s","%s")' % (entryo,entryt,entryf))
        success_sign_tip()
        root.destroy()
        loginui()
    else:
        # flag1 = 0
        fail_sign_tip_pwd()


def sign():
    global cur,flag1
    db = pymysql.connect(host='localhost',user='root',password='',database='st',port=3306)
    cur = db.cursor()
    sql = 'SELECT username FROM user'
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    entryo = inputone.get()
    entryt = inputtwo.get()
    entryth = inputthree.get()
    entryf = inputf.get()
    # print(entryo)

    name = []
    for row in results:
        username = row[0]
        name.append(username)
    print(name)

    if entryt == entryth:
        flag1 = True
        for i in range(len(name)):
            if entryo != "":
                if name[i] == entryo:
                    flag1 = False
                    fail_sign_tip_username()
                    # print(name[i])
                    break
        if flag1:
            sign_two_pwd(entryo,entryt,entryth,entryf)
        # else:
        #     fail_sign_tip()

    else:
        fail_sign_tip_pwd()


def loginfalse():
    print(111)


def tryone():
    print(111)


def hello1():
    print("6666")
def style22():
    msgbox.showinfo(title='提示',message='登录即可领取该主题！')
def style2():
    global labelHello,opnum,numfir
    labelHello.config(bg="#3cada9")
    opnum.config(bg="#3cada9")
    numfir.config(bg="#3cada9")
def style():
    global labelHello,opnum,numfir
    labelHello.config(bg="white")
    opnum.config(bg="white")
    numfir.config(bg="white")


def click1(event):
    global entryCd,labelHello,cd,message1,txt1,num2,onw_nameuser
    cd = int(entryCd.get())
    get_proe1()
    labelHello.config(text="你输入的数字是：%d " % cd)
    print(cd)
    txt1 = cd
    x = cd
    message1 = str(cd)
    sk.send(message1.encode())


def btnClicked2():
    global entryCd,labelHello,cd,message1,txt1,num2,onw_nameuser
    cd = int(entryCd.get())
    get_proe1()
    labelHello.config(text="你输入的数字是：%d " % cd)
    print(cd)
    txt1 = cd
    x = cd
    message1 = str(cd)
    sk.send(message1.encode())


# 单机
def btnClicked():
    global entryCd,labelHello,cd,message,txt1,opnum,num2,root1
    cd = int(entryCd.get())
    opnum.config(text="你输入的数字是：%d " % cd)
    print(cd)
    txt1 = cd
    x = cd
    message = str(cd)
    if num == 8494:
        if x == 8494:
            update()
        else:
            truenum()
    else:
        while 1:
            if x == 8494:
                truenum()
                break
            if x > num2:
                update_big()
                break
            if x < num2:
                update_small()
                break
            if x == num2:
                update()
                break

    # print("答对了，恭喜，今晚你请客！")
    # print("一共回答了",j,"次")
    # print(message)
    # sk.send(message.encode())


def com():
    global inputCd,mynum,root1
    cd = float(inputCd.get())
    mynum(root1,text="%.2f" % cd)
    msgbox.showinfo("提示","b小了! !")


def hello():
    msgbox.showinfo("提示","welcome to use this tool!")


def updatename():
    global onw_username
    msgbox.showinfo("提示","答对了，" + onw_username + "你太厉害了666! !")
    msgbox.showinfo("提示","游戏结束")
    root.destroy()
    main_soneui()


def update():
    global root1
    msgbox.showinfo("提示","答对了，你太厉害了666! !")
    msgbox.showinfo("提示","游戏结束")
    root1.destroy()
    loginui()


def update_big():
    msgbox.showinfo("提示","比它大了，你小脑瓜子怎么想的!")


def update_small():
    msgbox.showinfo("提示","比它小了，你大脑瓜子怎么想的! !")


def update_binggo():
    msgbox.showinfo("提示","太棒了" + username1 + "你是怎么想到的! !")


def main_soneui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum

    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")

    message = ""
    # msgbox.showinfo(title='提示消息框', message=message)

    # sk.sendall(message.encode('utf-8'))
    # funmun=sk.recv(1024).decode()

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '！！！欢迎来到数字大爆炸！！！'
    # message=sk.sendall(message.encode('utf-8'))
    message = sk.recv(1024).decode()
    funum = message
    mainnum = str(funum)

    mainnum = '这是一个' + funum + '位数'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m

    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text='txt1',bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)

    root1.mainloop()


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


def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)


def main_soneui_bad():
    global inputCd,mynum,root1,sk
    global entryCd,cd,message,txt1,num2
    global labelHello,opnum,numfir
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command="")
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command=truenum)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style22)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    numBig = numcollect()
    print(num2)
    nu = str(numBig)
    nu = "该数字的位数是:" + nu
    txt = '！！！欢迎来到数字大爆炸！！！'
    mainnum = '登录解锁对战玩法'
    root1['menu'] = m
    # get_proe()
    txt2 = "随风而去"
    Label(root1,text=txt,heigh=2,width=35,font=root1.my_font).place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=nu,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text=txt2,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22).place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)
    btnCal = Button(root1,text='确定',width=8,command=btnClicked,font=root1.my_fonto)
    btnCal.place(x=310,y=350)

    root1.mainloop()
def myself_ui():


    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum
    global sk,host,port,o
    # sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # sk.connect((host,port))
    serverone_name = "lin"
    sk.send(serverone_name.encode())




    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")

    message = ""
    # msgbox.showinfo(title='提示消息框', message=message)

    # sk.sendall(message.encode('utf-8'))
    # funmun=sk.recv(1024).decode()

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏","游戏大厅",'返回登录界面',"帮助"]:

        if item == "返回游戏":
            filemenu.add_command(label=item,command=success_tip1)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '---个人信息---'
    # message=sk.sendall(message.encode('utf-8'))

    mainnum = str(onw_username)
    l_name = "等级：1级"
    root1['menu'] = m

    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numlfir = Label(root1,text='用户：'+mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numlfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text='未开通会员！！！',bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)


    root1.mainloop()



if __name__ == '__main__':
    loginui()

