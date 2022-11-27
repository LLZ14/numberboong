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

