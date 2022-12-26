#client
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    # client_01 = socket.socket()
    # client_01.connect(('10.1.30.100',9002))

    global onw_username,username2
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    # client_01.send(myname)#第一次发送
    username=str(username)
    username2=str(username)
    client_01.send(username.encode('utf-8'))
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    print("用户"+str(msg)+"已加入！！！")

    root.destroy()
    main_sureui()
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
def success_tip1():
    global onw_username,sk,num
    # sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # host = "10.1.30.100"
    # port = 9090

    # sk.connect((host,port))
    #
    # serverone_name = onw_username
    # sk.send(serverone_name.encode())
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))
    #
    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)
    #
    # conn,addr = server.accept()
    root1.destroy()
    main_sureui()


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
    root.title("数字大爆炸V1.0(client)")
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
    root.title("数字大爆炸V1.0(client)")
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
def judegment_own(x):
    global weishu1,num1
    if x == int(num1):
        update_binggo()
        msgbox.showinfo("tips","game over")
        client_01.send("over".encode('utf-8'))
        client_01.close()

    if x < int(num1):
        update_small()
    if x > int(num1):
        update_big()
def judegment_resvother(x):
    global weishu1,num1
    if x == int(num1):
        update_binggo()
        return "over"
    if x < int(num1):
        update_small()
    if x > int(num1):
        update_big()

def click1(event):
    global entryCd,labelHello,cd,message1,txt1,num2,onw_nameuser,client_01,opnum,i,msg
    i=i+1
    print(i)
    if i == 2:
        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)
        # opnum.config(text="等待对方输入!")
        msg = client_01.recv(1024).decode('utf-8')
        print(msg)
        txt1 = cd
        x = int(cd)
        judegment_own(x)
        print(x)
        message1 = str(cd)
        client_01.send(message1.encode('utf-8'))

    if i>2:

        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)
        # opnum.config(text="对方输入的数字是：%d " % int(msg))
        msg = client_01.recv(1024).decode('utf-8')
        if msg!="":
            opnum.config(text="对方输入的数字是：%d " % int(msg))
            print(msg)
            txt1 = cd

            x = int(cd)
            judegment_own(x)
            print(x)
            message1 = str(cd)
            client_01.send(message1.encode('utf-8'))
        else:
            opnum.config(text="等待对方输入!")
            print(msg)
            txt1 = cd

            x = int(cd)
            judegment_own(x)
            print(x)
            message1 = str(cd)
            client_01.send(message1.encode('utf-8'))



def Clicked2():
    global entryCd,message1,txt1,num2,onw_nameuser,opnum
    cd = client_01.recv(1024).decode('utf-8')
    cd = int(cd)
    opnum.config(text="对方输入的数字是：%d " % cd)
    print(cd)
    # txt1 = cd
    # x = cd
    # message1 = str(cd)
    # client_01.send(message1.encode('utf-8'))
# 单机
def Click_oneself():
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
def com():
    global inputCd,mynum,root1
    cd = float(inputCd.get())
    mynum(root1,text="%.2f" % cd)
    msgbox.showinfo("提示","b小了! !")
def login_for_you():
    msgbox.showinfo("提示","请登录!")
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
def cone(Dan):
    global flag,client_01
    dana=Dan


    info = input('请输入》》》').encode("utf-8")
    if info=="":
             client_01.close()

    if int(info)==dana:
             print("you win!!")
             client_01.send(b'lose')
             client_01.close()

    if int(info)<dana:
             print("you get small!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    if int(info)>dana:
             print("you get bigger!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    msg = client_01.recv(1024).decode('utf-8')
    if msg == "over":
            # print("you lose!!")
             print("对方猜的是"+str(dana))
             print("你输了")
             print("--------------------")
             flag=0
             client_01.close()
             # socket.close()
             # print(msg)
    a=msg.split("|")
                # print(a[3])


    print("对方猜的是："+str(a[3]))
    if int(a[3])<dana:
             print("对方猜小了")
    if int(a[3])>dana:
             print("对方猜大了")
def main_soneui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir,weishu1
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,client_01,i
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    # weishu=numcollect()
    print("这是一个："+str(weishu1)+"位数")
    print("这是答案："+str(num1))



# """
#     一开始定义客户端去连接服务器的时候需要发送的
#     客户端点击连接按钮发送：
#     1，用户名C1=02
#     2,提取数据，将收到的信息分离，分别存起来，比如位数，num,利用分片，split分成列表，然后固定a[1]为位数，a[2]为num,a[0]是用户名，a[3]是自己的数据
#     a[4]是服务端数据，ok
#     3，编写程序，判断n输入是否==a[2],如果是就显示信息提示，退出循环，结束网络连接
#     服务器接受到了消息：
#     1，将用户名C1存起来  Sc1=C1 send=str(Sc1+"|"+位数+"|"+num+"|"+C1(传过来的数据))
#     2,input !=num,提示结果, send=send+input"""

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
            filemenu.add_command(label=item,command=truenum1)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'




    mainnum = '这是一个' + str(weishu1) + '位数'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    optxt="对方等待你输入"
    print(i)
    # if i > 1:
    #     print(i)
    #     msg = client_01.recv(1024).decode('utf-8')
    #     if msg !="":
    # 
    #         optxt="对方输入的是"+str(msg)
    #         optxt=optxt
    #         opnum.config(text=optxt)
    # 
    #     else:
    #         optxt=optxt
    #         opnum.config(text="对方等待你输入")
    # else:
    #     print(i)
    i=i+1
    print(i)
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text=optxt,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)


    root1.mainloop()
def clickbegin(x):
    global weishu1,num1,client_01,conn,i
    msgbox.showinfo("tips","等待用户加入！！!")
    i=0
    x="1"

    # conn,addr = client_01.accept()

    myname = x.encode("utf-8")
    client_01.send(myname)
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    a=msg.split("|")
    print(a)
    weishu1=a[0]
    num1=a[1]
    print(a[0])
    print(a[1])
    root1.destroy()
    main_soneui()


def clickexit():
    ask=msgbox.askyesno("提示","是否退出游戏？")
    if ask:
        root1.destroy()
def main_sureui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum

    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
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
    # funum = message
    # mainnum = str(funum)
    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto)
    btnCalbin.place(x=310,y=170)
    btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    root1.mainloop()
#单机答案
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def truenum1():
    global num1
    # tn=str(num)
    tn = num1
    msgbox.showinfo("答案",tn)
#单机
def main_soneui_bad():
    global inputCd,mynum,root1,sk
    global entryCd,cd,message,txt1,num2
    global labelHello,opnum,numfir
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=login_for_you)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command=login_for_you)
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
    Bt = Button(root1,text='确定',width=8,command=Click_oneself,font=root1.my_fonto)
    Bt.place(x=310,y=350)

    root1.mainloop()
def myself_ui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,opnum
    global port,o,client_01
    serverone_name = "lin"
    client_01.send(serverone_name.encode())
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏主界面","游戏大厅",'返回登录界面',"帮助"]:

        if item == "返回游戏主界面":
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
    client_01 = socket.socket()
    client_01.connect(('10.1.30.100',9002))
    loginui()
    # main_soneui()
    
    
    
    
    #client
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    # client_01 = socket.socket()
    # client_01.connect(('10.1.30.100',9002))

    global onw_username,username2
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    # client_01.send(myname)#第一次发送
    username=str(username)
    username2=str(username)
    client_01.send(username.encode('utf-8'))
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    print("用户"+str(msg)+"已加入！！！")

    root.destroy()
    main_sureui()
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
def success_tip1():
    global onw_username,sk,num
    # sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # host = "10.1.30.100"
    # port = 9090

    # sk.connect((host,port))
    #
    # serverone_name = onw_username
    # sk.send(serverone_name.encode())
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))
    #
    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)
    #
    # conn,addr = server.accept()
    root1.destroy()
    main_sureui()


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
    root.title("数字大爆炸V1.0(client)")
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
    root.title("数字大爆炸V1.0(client)")
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
def judegment_own(x):
    global weishu1,num1
    if x == int(num1):
        update_binggo()
        msgbox.showinfo("tips","game over")
        client_01.send("over".encode('utf-8'))
        client_01.close()

    if x < int(num1):
        update_small()
    if x > int(num1):
        update_big()
def judegment_resvother(x):
    global weishu1,num1
    if int(x) == int(num1):
        update_binggo()
        return "over"
    if int(x) < int(num1):
        update_small()
    if int(x)> int(num1):
        update_big()

def click1(event):
    global entryCd,labelHello,cd,message1,txt1,num2,onw_nameuser,client_01,opnum,i,msg
    if i==1:#第一次发猜的数字
        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)
        opnum.config(text="等待rival的输入!")
        # msg = client_01.recv(1024).decode('utf-8')
        # print(msg)
        txt1 = cd
        x = int(cd)
        judegment_own(x)
        print(x)
        message1 = str(cd)
        client_01.send(message1.encode('utf-8'))
        while True:
            msg = client_01.recv(1024).decode('utf-8')
            print("这是事件里的："+msg)
            opnum.config(text="对方猜的是"+msg)
            judegment_resvother(msg)
            break
        i=i+1
        print(i)
    if i>=2:
        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)

        txt1 = cd
        x = int(cd)
        judegment_own(x)
        print(x)
        message1 = str(cd)
        client_01.send(message1.encode('utf-8'))

        msg = client_01.recv(1024).decode('utf-8')
        print(msg)
        opnum.config(text="对方猜的是"+msg)
        judegment_resvother(msg)
        i=i+1
        print(i)



def Clicked2():
    global entryCd,message1,txt1,num2,onw_nameuser,opnum
    cd = client_01.recv(1024).decode('utf-8')
    cd = int(cd)
    opnum.config(text="对方输入的数字是：%d " % cd)
    print(cd)
    # txt1 = cd
    # x = cd
    # message1 = str(cd)
    # client_01.send(message1.encode('utf-8'))
# 单机
def Click_oneself():
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
def com():
    global inputCd,mynum,root1
    cd = float(inputCd.get())
    mynum(root1,text="%.2f" % cd)
    msgbox.showinfo("提示","b小了! !")
def login_for_you():
    msgbox.showinfo("提示","请登录!")
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
def cone(Dan):
    global flag,client_01
    dana=Dan


    info = input('请输入》》》').encode("utf-8")
    if info=="":
             client_01.close()

    if int(info)==dana:
             print("you win!!")
             client_01.send(b'lose')
             client_01.close()

    if int(info)<dana:
             print("you get small!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    if int(info)>dana:
             print("you get bigger!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    msg = client_01.recv(1024).decode('utf-8')
    if msg == "over":
            # print("you lose!!")
             print("对方猜的是"+str(dana))
             print("你输了")
             print("--------------------")
             flag=0
             client_01.close()
             # socket.close()
             # print(msg)
    a=msg.split("|")
                # print(a[3])


    print("对方猜的是："+str(a[3]))
    if int(a[3])<dana:
             print("对方猜小了")
    if int(a[3])>dana:
             print("对方猜大了")
def main_soneui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir,weishu1
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,client_01,i
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    # weishu=numcollect()
    print("这是一个："+str(weishu1)+"位数")
    print("这是答案："+str(num1))

# """
#     一开始定义客户端去连接服务器的时候需要发送的
#     客户端点击连接按钮发送：
#     1，用户名C1=02
#     2,提取数据，将收到的信息分离，分别存起来，比如位数，num,利用分片，split分成列表，然后固定a[1]为位数，a[2]为num,a[0]是用户名，a[3]是自己的数据
#     a[4]是服务端数据，ok
#     3，编写程序，判断n输入是否==a[2],如果是就显示信息提示，退出循环，结束网络连接
#     服务器接受到了消息：
#     1，将用户名C1存起来  Sc1=C1 send=str(Sc1+"|"+位数+"|"+num+"|"+C1(传过来的数据))
#     2,input !=num,提示结果, send=send+input"""

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
            filemenu.add_command(label=item,command=truenum1)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'




    mainnum = '这是一个' + str(weishu1) + '位数'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    optxt="对方等待你输入"
    # if i > 1:
    #     print(i)
    #     msg = client_01.recv(1024).decode('utf-8')
    #     if msg !="":
    #
    #         optxt="对方输入的是"+str(msg)
    #         optxt=optxt
    #         opnum.config(text=optxt)
    #
    #     else:
    #         optxt=optxt
    #         opnum.config(text="对方等待你输入")
    # else:
    #     print(i)
    # i=i+1
    print("这是main的i的次数："+str(i))
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text=optxt,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)
    root1.mainloop()
def clickbegin(x):
    global weishu1,num1,client_01,conn,i
    msgbox.showinfo("tips","等待用户加入！！!")
    i=0
    x="1"

    # conn,addr = client_01.accept()

    myname = x.encode("utf-8")
    client_01.send(myname)
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    a=msg.split("|")
    print(a)
    weishu1=a[0]
    num1=a[1]
    print(a[0])
    print(a[1])
    i=i+1
    print(i)
    root1.destroy()
    main_soneui()


def clickexit():
    ask=msgbox.askyesno("提示","是否退出游戏？")
    if ask:
        root1.destroy()
def main_sureui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum

    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
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
    # funum = message
    # mainnum = str(funum)
    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto)
    btnCalbin.place(x=310,y=170)
    btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    root1.mainloop()
#单机答案
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def truenum1():
    global num1
    # tn=str(num)
    tn = num1
    msgbox.showinfo("答案",tn)
#单机
def main_soneui_bad():
    global inputCd,mynum,root1,sk
    global entryCd,cd,message,txt1,num2
    global labelHello,opnum,numfir
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=login_for_you)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command=login_for_you)
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
    Bt = Button(root1,text='确定',width=8,command=Click_oneself,font=root1.my_fonto)
    Bt.place(x=310,y=350)

    root1.mainloop()
def myself_ui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,opnum
    global port,o,client_01
    serverone_name = "lin"
    client_01.send(serverone_name.encode())
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏主界面","游戏大厅",'返回登录界面',"帮助"]:

        if item == "返回游戏主界面":
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
    client_01 = socket.socket()
    client_01.connect(('10.1.30.100',9002))
    loginui()
    # main_soneui()


    
    #client
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    # client_01 = socket.socket()
    # client_01.connect(('10.1.30.100',9002))

    global onw_username,username2
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    # client_01.send(myname)#第一次发送
    username=str(username)
    username2=str(username)
    client_01.send(username.encode('utf-8'))
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    print("用户"+str(msg)+"已加入！！！")

    root.destroy()
    main_sureui()
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
def success_tip1():
    global onw_username,sk,num
    # sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # host = "10.1.30.100"
    # port = 9090

    # sk.connect((host,port))
    #
    # serverone_name = onw_username
    # sk.send(serverone_name.encode())
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))
    #
    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)
    #
    # conn,addr = server.accept()
    root1.destroy()
    main_sureui()


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
    root.title("数字大爆炸V1.0(client)")
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
    root.title("数字大爆炸V1.0(client)")
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
def judegment_own(x):
    global weishu1,num1
    if x == int(num1):
        update_binggo()
        msgbox.showinfo("tips","game over")
        client_01.send("over".encode('utf-8'))
        client_01.close()

    if x < int(num1):
        update_small()
    if x > int(num1):
        update_big()
def judegment_resvother(x):
    global weishu1,num1
    if int(x) == int(num1):
        update_binggoo()
        return "over"
    if int(x) < int(num1):
        update_smallo()
    if int(x)> int(num1):
        update_bigo()

def click1(event):
    global entryCd,labelHello,cd,message1,txt1,num2,onw_nameuser,client_01,opnum,i,msg
    if i==1:#第一次发猜的数字
        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)
        opnum.config(text="等待rival的输入!")
        # msg = client_01.recv(1024).decode('utf-8')
        # print(msg)
        txt1 = cd
        x = int(cd)
        judegment_own(x)
        print(x)
        message1 = str(cd)
        client_01.send(message1.encode('utf-8'))
        while True:
            msg = client_01.recv(1024).decode('utf-8')
            print("这是事件里的："+msg)
            opnum.config(text="对方猜的是"+msg)
            judegment_resvother(msg)
            break
        i=i+1
        print(i)
    if i>=2:
        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        judegment_own(cd)

        txt1 = cd
        x = int(cd)
        judegment_own(x)
        print(x)
        message1 = str(cd)
        client_01.send(message1.encode('utf-8'))

        msg = client_01.recv(1024).decode('utf-8')
        print(msg)
        opnum.config(text="对方猜的是"+msg)
        judegment_resvother(msg)
        i=i+1
        print(i)



def Clicked2():
    global entryCd,message1,txt1,num2,onw_nameuser,opnum
    cd = client_01.recv(1024).decode('utf-8')
    cd = int(cd)
    opnum.config(text="对方输入的数字是：%d " % cd)
    print(cd)
    # txt1 = cd
    # x = cd
    # message1 = str(cd)
    # client_01.send(message1.encode('utf-8'))
# 单机
def Click_oneself():
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
def com():
    global inputCd,mynum,root1
    cd = float(inputCd.get())
    mynum(root1,text="%.2f" % cd)
    msgbox.showinfo("提示","b小了! !")
def login_for_you():
    msgbox.showinfo("提示","请登录!")
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
def update_bigo():
    msgbox.showinfo("提示","rival猜大了!")
def update_smallo():
    msgbox.showinfo("提示","rival猜小了!")
def update_binggoo():
    msgbox.showinfo("提示","太遗憾了，对方赢了，你输了! !")
def cone(Dan):
    global flag,client_01
    dana=Dan


    info = input('请输入》》》').encode("utf-8")
    if info=="":
             client_01.close()

    if int(info)==dana:
             print("you win!!")
             client_01.send(b'lose')
             client_01.close()

    if int(info)<dana:
             print("you get small!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    if int(info)>dana:
             print("you get bigger!!")
             print("waiting optinal input!!!")
             client_01.send(info)

    msg = client_01.recv(1024).decode('utf-8')
    if msg == "over":
            # print("you lose!!")
             print("对方猜的是"+str(dana))
             print("你输了")
             print("--------------------")
             flag=0
             client_01.close()
             # socket.close()
             # print(msg)
    a=msg.split("|")
                # print(a[3])


    print("对方猜的是："+str(a[3]))
    if int(a[3])<dana:
             print("对方猜小了")
    if int(a[3])>dana:
             print("对方猜大了")
def main_soneui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir,weishu1
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,client_01,i
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    # weishu=numcollect()
    print("这是一个："+str(weishu1)+"位数")
    print("这是答案："+str(num1))

# """
#     一开始定义客户端去连接服务器的时候需要发送的
#     客户端点击连接按钮发送：
#     1，用户名C1=02
#     2,提取数据，将收到的信息分离，分别存起来，比如位数，num,利用分片，split分成列表，然后固定a[1]为位数，a[2]为num,a[0]是用户名，a[3]是自己的数据
#     a[4]是服务端数据，ok
#     3，编写程序，判断n输入是否==a[2],如果是就显示信息提示，退出循环，结束网络连接
#     服务器接受到了消息：
#     1，将用户名C1存起来  Sc1=C1 send=str(Sc1+"|"+位数+"|"+num+"|"+C1(传过来的数据))
#     2,input !=num,提示结果, send=send+input"""

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
            filemenu.add_command(label=item,command=truenum1)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'




    mainnum = '这是一个' + str(weishu1) + '位数'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    optxt="对方等待你输入"
    # if i > 1:
    #     print(i)
    #     msg = client_01.recv(1024).decode('utf-8')
    #     if msg !="":
    #
    #         optxt="对方输入的是"+str(msg)
    #         optxt=optxt
    #         opnum.config(text=optxt)
    #
    #     else:
    #         optxt=optxt
    #         opnum.config(text="对方等待你输入")
    # else:
    #     print(i)
    # i=i+1
    print("这是main的i的次数："+str(i))
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opnum = Label(root1,text=optxt,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opnum.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)
    root1.mainloop()
def clickbegin(x):
    global weishu1,num1,client_01,conn,i
    msgbox.showinfo("tips","等待用户加入！！!")
    i=0
    x="1"

    # conn,addr = client_01.accept()

    myname = x.encode("utf-8")
    client_01.send(myname)
    msg = client_01.recv(1024).decode('utf-8')
    print(msg)
    a=msg.split("|")
    print(a)
    weishu1=a[0]
    num1=a[1]
    print(a[0])
    print(a[1])
    i=i+1
    print(i)
    root1.destroy()
    main_soneui()


def clickexit():
    ask=msgbox.askyesno("提示","是否退出游戏？")
    if ask:
        root1.destroy()
def main_sureui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum

    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
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
    # funum = message
    # mainnum = str(funum)
    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto)
    btnCalbin.place(x=310,y=170)
    btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    root1.mainloop()
#单机答案
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def truenum1():
    global num1
    # tn=str(num)
    tn = num1
    msgbox.showinfo("答案",tn)
#单机
def main_soneui_bad():
    global inputCd,mynum,root1,sk
    global entryCd,cd,message,txt1,num2
    global labelHello,opnum,numfir
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=login_for_you)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command=login_for_you)
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
    Bt = Button(root1,text='确定',width=8,command=Click_oneself,font=root1.my_fonto)
    Bt.place(x=310,y=350)

    root1.mainloop()
def myself_ui():
    global inputCd,mynum,root1,sk,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,opnum
    global port,o,client_01
    serverone_name = "lin"
    client_01.send(serverone_name.encode())
    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0(client)")
    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏主界面","游戏大厅",'返回登录界面',"帮助"]:

        if item == "返回游戏主界面":
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
    client_01 = socket.socket()
    client_01.connect(('10.1.30.100',9002))
    loginui()
    # main_soneui()
