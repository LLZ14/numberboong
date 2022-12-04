#server
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    global onw_username,server,jies,conn
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    msgbox.showinfo("tips","正在连接……")
    conn.send(str(username).encode('utf-8'))
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
    global onw_username,conn,host,port,num
    root1.destroy()
    main_sureui()
def success_sign_tip():
    msgbox.showinfo(title='提示',message='注册成功')
    root.quit()
    pass
def fail_tip():
    msgbox.showerror(title='错误消息框',message='用户已经登录！')
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
    global input1,input2,root,conn

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
def login():
    global to,username1,flag,conn
    conn,addr = server.accept()

    msgname=conn.recv(1024).decode('utf-8')
    # if msgname !="":
    msgname=str(msgname)
    print(msgname)
    db = pymysql.connect(host='localhost',user='root',password='',database='st',port=3306)
    cur = db.cursor()
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
        if username1 == entry1 and password1 == entry2 and msgname != entry1:
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
        root.destroy()
        loginui()

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
def click1(event):
    global entryCd,labelHello,cd,msg,txt1,num2,onw_nameuser,conn,i,opnum
    nomsg=conn.recv(1024).endoce('utf-8')
    nomsg=int(nomsg)
    if nomsg == num:
        msgbox.showinfo('tips','对方赢了')
        msgbox.showinfo("tips","game over!!!")
        server.close()
    if nomsg < num:
        msgbox.showinfo("tips","对方猜小了")
        msgbox.showinfo("tips","请你输入！")
        opnum.config(text="对方输入的是"+str(nomsg))
    if nomsg > num:
        msgbox.showinfo("tips","对方猜大了")
        msgbox.showinfo("tips","请你输入！")

    cd = int(entryCd.get())
    labelHello.config(text="你输入的数字是：%d " % cd)
    print(cd)
    txt1 = cd
    x = cd
    msg = str(cd)
    if int(msg) < num:
        update_small()
    if int(msg) > num:
        update_big()
    if int(msg) ==num:
        update_binggo()
        conn.send("over".encode('utf-8'))

    conn.send(msg.encode("utf-8"))

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
def changetxt():
    global i,optxt,msg,root1,opnum
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,weishu
    # if i >1:
    msg = conn.recv(1024).decode('utf8')
    print(msg)
    optxt=msg
    opnum.config(text="对方输入的是"+str(msg))

    # if i==0:
    #     opnum.config(text="等待对方输入！")

def main_soneui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir,opnum
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,weishu,optxt,i
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))


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
    m.add_cascade(label='退出',command=clickexit)

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command=truenum)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'
    # msgbox.showinfo("tips","等待对方输入！！！")

    mainnum = '这是一个' + str(weishu) + '位数'
    l_name = "欢迎你," + onw_username
    optxt="等待用户输入"
    root1['menu'] = m


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
    i=i+1
    print(i)

    root1.mainloop()
def clickbegin():
    global weishu,num,conn,i
    #判断用户是否连接了
    i=0

    # while True:
    #     try :
    #         msgbox.showinfo("tips","用户已连接！")
    #         main_soneui()
    weishu=numcollect()
    print("这是一个："+str(weishu)+"位数")
    print("这是答案："+str(num))

    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)

    msgbox.showinfo("tips","waiting for game begin!!!")


    # conn,addr = server.accept()
    msg = conn.recv(1024).decode('utf-8')
    while True:
            if msg !="" and msg == "1":
                print(msg)
                to_client_weishu=weishu
                to_client_num=num
                fone=str(str(to_client_weishu)+"|"+str(to_client_num))
                conn.send(fone.encode('utf-8'))
                msgbox.showinfo("tips","用户已连接！")
                msgbox.showinfo("tips","this is a num of :！"+str(weishu))
                msgbox.showinfo("tips","waiting for rival input !!! ")
                # msg = conn.recv(1024).decode('utf-8')
                print(msg)
                root1.destroy()
                main_soneui()
                break
            if msg=="":
                msgbox.showinfo("tips","waiting!!!")
                continue
            # if msg!="" and msg !="1":
            #     rev=msg
            #     fone=str(weishu)+"|"+str(num)
            #     rev=str(fone)+"|"+str(rev)
            #     a=rev.split("|")
            #     cli=a[2]
            #     print(cli)
            #     print(rev)

    # while
    # main_soneui()
    # root1.destroy()
    # print("4444")
def clickexit():
    aconn=msgbox.aconnyesno("提示","是否退出游戏？")
    if aconn==True:
        root1.destroy()

        #server开启监听，点击界面不会消失，tips等待用户加入，用户加入后传出第一个信息，包括位数，答案，str(num)
        #client点击登录后，进入界面，点击开启对局后，同时接受server传过来的信息，进去主界面，开始游戏，输入数字，传到server
        #
def main_sureui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,conn


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

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "退出":
            filemenu.add_command(label=item,command=clickexit)
    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '！！！欢迎来到数字大爆炸！！！'

    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    # btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=lambda: [root1.destroy(),main_soneui_1()])
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=clickbegin)
    btnCalbin.place(x=310,y=170)
    # btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    # msg = conn.recv(1024).decode('utf-8')
    # print(msg)

    root1.mainloop()
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def main_soneui_bad():
    global inputCd,mynum,root1,conn
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
    btnCal = Button(root1,text='确定',width=8,command=btnClicked,font=root1.my_fonto)
    btnCal.place(x=310,y=350)

    root1.mainloop()
def myself_ui():


    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum
    global conn,host,port,o
    # conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # conn.connect((host,port))
    serverone_name = "lin"
    # conn.send(serverone_name.encode())




    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")


    # msgbox.showinfo(title='提示消息框', message=message)

    # conn.sendall(message.encode('utf-8'))
    # funmun=conn.recv(1024).decode()

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "返回游戏":
            filemenu.add_command(label=item,command=success_tip1)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "帮助":
            filemenu.add_command(label=item,command=clickexit)

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '---个人信息---'
    # message=conn.sendall(message.encode('utf-8'))

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
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('10.1.30.100',9002))
    server.listen(5)
    loginui()
    
    #server
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    global onw_username,server,jies,conn
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    msgbox.showinfo("tips","正在连接……")
    conn.send(str(username).encode('utf-8'))
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
    global onw_username,conn,host,port,num
    root1.destroy()
    main_sureui()
def success_sign_tip():
    msgbox.showinfo(title='提示',message='注册成功')
    root.quit()
    pass
def fail_tip():
    msgbox.showerror(title='错误消息框',message='用户已经登录！')
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
    global input1,input2,root,conn

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
def login():
    global to,username1,flag,conn
    conn,addr = server.accept()

    msgname=conn.recv(1024).decode('utf-8')
    # if msgname !="":
    msgname=str(msgname)
    print(msgname)
    db = pymysql.connect(host='localhost',user='root',password='',database='st',port=3306)
    cur = db.cursor()
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
        if username1 == entry1 and password1 == entry2 and msgname != entry1:
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
        root.destroy()
        loginui()

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
def click1(event):
    global entryCd,labelHello,cd,msg,txt1,num2,onw_nameuser,conn,i,opnum
    # nomsg=conn.recv(1024).decode('utf-8')
    # msg = conn.recv(1024).decode('utf-8')
    # nomsg=int(nomsg)
    # if nomsg == num:
    #     msgbox.showinfo('tips','对方赢了')
    #     msgbox.showinfo("tips","game over!!!")
    #     server.close()
    # if nomsg < num:
    #     msgbox.showinfo("tips","对方猜小了")
    #     msgbox.showinfo("tips","请你输入！")
    #     opnum.config(text="对方输入的是"+str(nomsg))
    # if nomsg > num:
    #     msgbox.showinfo("tips","对方猜大了")
    #     msgbox.showinfo("tips","请你输入！")
    # if i ==1:
    #     changetxt()

    cd = int(entryCd.get())
    labelHello.config(text="你输入的数字是：%d " % cd)
    print(cd)
    txt1 = cd
    x = cd
    msg = str(cd)
    if int(msg) < num:
        update_small()
    if int(msg) > num:
        update_big()
    if int(msg) ==num:
        update_binggo()
        conn.send("over".encode('utf-8'))

    conn.send(msg.encode("utf-8"))
    # opn.config(text="你输入的数字是：%d " % int(mss))
    # i=i+1
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
def changetxt():
    global i,optxt,msg
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,opn,weishu
    # if i >1:
    # msg = conn.recv(1024).decode('utf8')
    print(msg)
    # opn.config(text="对方输入的是"+str(msg))
    opn.config(text="输入!")

    # nomsg=conn.recv(1024).endoce('utf-8')
    nomsg=int(msg)
    if nomsg == num:
        msgbox.showinfo('tips','对方赢了')
        msgbox.showinfo("tips","game over!!!")
        server.close()
    if nomsg < num:
        msgbox.showinfo("tips","对方猜小了")
        msgbox.showinfo("tips","请你输入！")
        opn.config(text="对方输入的是"+str(nomsg))
    if nomsg > num:
        msgbox.showinfo("tips","对方猜大了")
        msgbox.showinfo("tips","请你输入！")

    # if i==0:
    #     opnum.config(text="等待对方输入！")

def main_soneui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir,mss
    global entryCd,labelHello,cd,message,txt1,host,port,opn,weishu,optxt,i
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))
    # if str(i)=="1":
    # while True:
    # msg = conn.recv(1024).decode('utf8')
    #     if not msg:
    #         print(msg)
    #
    #         break



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
    m.add_cascade(label='退出',command=clickexit)

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command=truenum)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'
    # msgbox.showinfo("tips","等待对方输入！！！")

    mainnum = '这是一个' + str(weishu) + '位数'
    l_name = "欢迎你," + onw_username
    # optxt="等待对方输入"
    root1['menu'] = m


    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opn= Label(root1,text=mss,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opn.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)
    # i=i+1
    # print(i)

    root1.mainloop()
def clickbegin():
    global weishu,num,conn,i,mss
    #判断用户是否连接了
    i=0

    # while True:
    #     try :
    #         msgbox.showinfo("tips","用户已连接！")
    #         main_soneui()
    weishu=numcollect()
    print("这是一个："+str(weishu)+"位数")
    print("这是答案："+str(num))

    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)

    msgbox.showinfo("tips","waiting for game begin!!!")


    # conn,addr = server.accept()
    msg = conn.recv(1024).decode('utf-8')
    while True:
            if msg !="" and msg == "1":
                print(msg)
                to_client_weishu=weishu
                to_client_num=num
                fone=str(str(to_client_weishu)+"|"+str(to_client_num))
                conn.send(fone.encode('utf-8'))
                # msgbox.showinfo("tips","用户已连接！")
                # msgbox.showinfo("tips","this is a num of :！"+str(weishu))
                # msgbox.showinfo("tips","waiting for rival input !!! ")
                # msg = conn.recv(1024).decode('utf-8')
                # print(msg)
                root1.destroy()
                mss = conn.recv(1024).decode('utf-8')
                print("这是对面的"+mss)
                main_soneui()
                # main_two()
                # msgbox.showinfo("tips","对方先猜！！")
                # main_soneui()
                break
            if msg=="":
                msgbox.showinfo("tips","waiting!!!")
                continue
            # if msg!="" and msg !="1":
            #     rev=msg
            #     fone=str(weishu)+"|"+str(num)
            #     rev=str(fone)+"|"+str(rev)
            #     a=rev.split("|")
            #     cli=a[2]
            #     print(cli)
            #     print(rev)

    # while
    # main_soneui()
    # root1.destroy()
    # print("4444")
# def main_two():
#     global conn,mss
#     global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
#     global entryCd,labelHello,cd,message,txt1,host,port,conn
#     mss = conn.recv(1024).decode('utf-8')
#     print(mss)
#     main_soneui()
def clickexit():
    aconn=msgbox.aconnyesno("提示","是否退出游戏？")
    if aconn==True:
        root1.destroy()

        #server开启监听，点击界面不会消失，tips等待用户加入，用户加入后传出第一个信息，包括位数，答案，str(num)
        #client点击登录后，进入界面，点击开启对局后，同时接受server传过来的信息，进去主界面，开始游戏，输入数字，传到server
        #
def main_sureui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,conn


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

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "退出":
            filemenu.add_command(label=item,command=clickexit)
    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '！！！欢迎来到数字大爆炸！！！'

    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    # btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=lambda: [root1.destroy(),main_soneui_1()])
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=clickbegin)
    btnCalbin.place(x=310,y=170)
    # btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    # msg = conn.recv(1024).decode('utf-8')
    # print(msg)

    root1.mainloop()
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def main_soneui_bad():
    global inputCd,mynum,root1,conn
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
    btnCal = Button(root1,text='确定',width=8,command=btnClicked,font=root1.my_fonto)
    btnCal.place(x=310,y=350)

    root1.mainloop()
def myself_ui():


    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum
    global conn,host,port,o
    # conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # conn.connect((host,port))
    serverone_name = "lin"
    # conn.send(serverone_name.encode())




    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")


    # msgbox.showinfo(title='提示消息框', message=message)

    # conn.sendall(message.encode('utf-8'))
    # funmun=conn.recv(1024).decode()

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "返回游戏":
            filemenu.add_command(label=item,command=success_tip1)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "帮助":
            filemenu.add_command(label=item,command=clickexit)

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '---个人信息---'
    # message=conn.sendall(message.encode('utf-8'))

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
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('10.1.30.100',9002))
    server.listen(5)
    loginui()
v3.0

#server
import random
import requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql
import socket
import tkinter as tk
def success_tip(username):
    global onw_username,server,jies,conn
    onw_username = username
    msgbox.showinfo(title='消息提示框',message='用户' + username + '登录成功')
    msgbox.showinfo("tips","正在连接……")
    conn.send(str(username).encode('utf-8'))
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
    global onw_username,conn,host,port,num
    root1.destroy()
    main_sureui()
def success_sign_tip():
    msgbox.showinfo(title='提示',message='注册成功')
    root.quit()
    pass
def fail_tip():
    msgbox.showerror(title='错误消息框',message='用户已经登录！')
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
    global input1,input2,root,conn

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
def login():
    global to,username1,flag,conn
    conn,addr = server.accept()

    msgname=conn.recv(1024).decode('utf-8')
    # if msgname !="":
    msgname=str(msgname)
    print(msgname)
    db = pymysql.connect(host='localhost',user='root',password='',database='st',port=3306)
    cur = db.cursor()
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
        if username1 == entry1 and password1 == entry2 and msgname != entry1:
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
        root.destroy()
        loginui()

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
def click1(event):
    global entryCd,labelHello,cd,msg,txt1,num2,onw_nameuser,conn,i,opnum
    # nomsg=conn.recv(1024).decode('utf-8')
    # msg = conn.recv(1024).decode('utf-8')
    # nomsg=int(nomsg)
    # if nomsg == num:
    #     msgbox.showinfo('tips','对方赢了')
    #     msgbox.showinfo("tips","game over!!!")
    #     server.close()
    # if nomsg < num:
    #     msgbox.showinfo("tips","对方猜小了")
    #     msgbox.showinfo("tips","请你输入！")
    #     opnum.config(text="对方输入的是"+str(nomsg))
    # if nomsg > num:
    #     msgbox.showinfo("tips","对方猜大了")
    #     msgbox.showinfo("tips","请你输入！")
    if i ==1:

        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        print(cd)
        txt1 = cd
        x = cd
        msg = str(cd)
        if int(msg) < num:
            update_small()
        if int(msg) > num:
            update_big()
        if int(msg) ==num:
            update_binggo()
            conn.send("over".encode('utf-8'))

        conn.send(msg.encode("utf-8"))
        i=i+1
        print(i)
    if i>=2:
        msg = conn.recv(1024).decode('utf-8')
        nomsg=int(msg)
        opn.config(text="对方输入的数字是：%d " % nomsg)
        # if nomsg == num:
        #     msgbox.showinfo('tips','对方赢了')
        #     msgbox.showinfo("tips","game over!!!")
        #     server.close()
        # if nomsg < num:
        #     msgbox.showinfo("tips","对方猜小了")
        #     msgbox.showinfo("tips","请你输入！")
        #     # opnum.config(text="对方输入的是"+str(nomsg))
        # if nomsg > num:
        #     msgbox.showinfo("tips","对方猜大了")
        #     msgbox.showinfo("tips","请你输入！")

        cd = int(entryCd.get())
        labelHello.config(text="你输入的数字是：%d " % cd)
        print(cd)
        txt1 = cd
        x = cd
        msg = str(cd)
        if int(msg) < num:
            update_small()
        if int(msg) > num:
            update_big()
        if int(msg) ==num:
            update_binggo()
            conn.send("over".encode('utf-8'))

        conn.send(msg.encode("utf-8"))
    # opn.config(text="你输入的数字是：%d " % int(mss))
    # i=i+1
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
def changetxt():
    global i,optxt,msg
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,opn,weishu
    # if i >1:
    # msg = conn.recv(1024).decode('utf8')
    print(msg)
    # opn.config(text="对方输入的是"+str(msg))
    opn.config(text="输入!")

    # nomsg=conn.recv(1024).endoce('utf-8')
    nomsg=int(msg)
    if nomsg == num:
        msgbox.showinfo('tips','对方赢了')
        msgbox.showinfo("tips","game over!!!")
        server.close()
    if nomsg < num:
        msgbox.showinfo("tips","对方猜小了")
        msgbox.showinfo("tips","请你输入！")
        opn.config(text="对方输入的是"+str(nomsg))
    if nomsg > num:
        msgbox.showinfo("tips","对方猜大了")
        msgbox.showinfo("tips","请你输入！")

    # if i==0:
    #     opnum.config(text="等待对方输入！")

def main_soneui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir,mss
    global entryCd,labelHello,cd,message,txt1,host,port,opn,weishu,optxt,i
    # weishu=numcollect()
    # print("这是一个："+str(weishu)+"位数")
    # print("这是答案："+str(num))
    # if str(i)=="1":
    # while True:
    # msg = conn.recv(1024).decode('utf8')
    #     if not msg:
    #         print(msg)
    #
    #         break



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
    m.add_cascade(label='退出',command=clickexit)

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command=truenum)
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)

    txt = '！！！欢迎来到数字大爆炸！！！'
    # msgbox.showinfo("tips","等待对方输入！！！")

    mainnum = '这是一个' + str(weishu) + '位数'
    l_name = "欢迎你," + onw_username
    # optxt="等待对方输入"
    root1['menu'] = m


    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=mainnum,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    labelHello = tk.Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    labelHello.place(x=26,y=170)
    opn=Label(root1,text=mss,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    opn.place(x=26,y=230)
    tin = Label(root1,text='请输入你要猜的数字:',font=root1.my_fonto,width=22)
    tin.place(x=246,y=280)
    entryCd = Entry(root1,width=36)
    entryCd.place(x=240,y=310)

    btnCal = Button(root1,text='确定',width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=350)
    btnCal.bind("<Button-1>",click1)
    # i=i+1
    # print(i)

    root1.mainloop()
def clickbegin():
    global weishu,num,conn,i,mss
    #判断用户是否连接了
    i=0

    # while True:
    #     try :
    #         msgbox.showinfo("tips","用户已连接！")
    #         main_soneui()
    weishu=numcollect()
    print("这是一个："+str(weishu)+"位数")
    print("这是答案："+str(num))

    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # server.bind(('10.1.30.100',9002))
    # server.listen(5)

    msgbox.showinfo("tips","waiting for game begin!!!")


    # conn,addr = server.accept()
    msg = conn.recv(1024).decode('utf-8')
    while True:
            if msg !="" and msg == "1":
                print(msg)
                to_client_weishu=weishu
                to_client_num=num
                fone=str(str(to_client_weishu)+"|"+str(to_client_num))
                conn.send(fone.encode('utf-8'))
                # msgbox.showinfo("tips","用户已连接！")
                # msgbox.showinfo("tips","this is a num of :！"+str(weishu))
                # msgbox.showinfo("tips","waiting for rival input !!! ")
                # msg = conn.recv(1024).decode('utf-8')
                # print(msg)
                root1.destroy()
                mss = conn.recv(1024).decode('utf-8')
                print("这是对面的"+mss)
                i=i+1
                main_soneui()
                # main_two()
                # msgbox.showinfo("tips","对方先猜！！")
                # main_soneui()
                break
            if msg=="":
                msgbox.showinfo("tips","waiting!!!")
                continue
            # if msg!="" and msg !="1":
            #     rev=msg
            #     fone=str(weishu)+"|"+str(num)
            #     rev=str(fone)+"|"+str(rev)
            #     a=rev.split("|")
            #     cli=a[2]
            #     print(cli)
            #     print(rev)

    # while
    # main_soneui()
    # root1.destroy()
    # print("4444")
# def main_two():
#     global conn,mss
#     global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
#     global entryCd,labelHello,cd,message,txt1,host,port,conn
#     mss = conn.recv(1024).decode('utf-8')
#     print(mss)
#     main_soneui()
def clickexit():
    aconn=msgbox.aconnyesno("提示","是否退出游戏？")
    if aconn==True:
        root1.destroy()

        #server开启监听，点击界面不会消失，tips等待用户加入，用户加入后传出第一个信息，包括位数，答案，str(num)
        #client点击登录后，进入界面，点击开启对局后，同时接受server传过来的信息，进去主界面，开始游戏，输入数字，传到server
        #
def main_sureui():
    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum,conn


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

    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),myself_ui()])
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "退出":
            filemenu.add_command(label=item,command=clickexit)
    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '！！！欢迎来到数字大爆炸！！！'

    mainnum = '开始对局'
    l_name = "欢迎你," + onw_username
    root1['menu'] = m
    ones = Label(root1,text=txt,heigh=2,width=35,font=root1.my_font)
    ones.place(x=10,y=10)
    numfir = Label(root1,text=l_name,bg='#3f8dbb',heigh=2,width=60,font=root1.my_fonto)
    numfir.place(x=26,y=110)
    # btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=lambda: [root1.destroy(),main_soneui_1()])
    btnCalbin = Button(root1,text='开始对局',width=8,font=root1.my_fonto,command=clickbegin)
    btnCalbin.place(x=310,y=170)
    # btnCalbin.bind("<Button-1>",clickbegin)
    btnCal = Button(root1,text='退出游戏',command=clickexit,width=8,font=root1.my_fonto)
    btnCal.place(x=310,y=230)
    # msg = conn.recv(1024).decode('utf-8')
    # print(msg)

    root1.mainloop()
def truenum():
    # tn=str(num)
    tn = num
    msgbox.showinfo("答案",tn)
def main_soneui_bad():
    global inputCd,mynum,root1,conn
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
    btnCal = Button(root1,text='确定',width=8,command=btnClicked,font=root1.my_fonto)
    btnCal.place(x=310,y=350)

    root1.mainloop()
def myself_ui():


    global inputCd,mynum,root1,conn,mainnum,onw_nameuser,numfir
    global entryCd,labelHello,cd,message,txt1,host,port,opnum
    global conn,host,port,o
    # conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # conn.connect((host,port))
    serverone_name = "lin"
    # conn.send(serverone_name.encode())




    root1 = Tk()
    root1.my_font = font.Font(font=("华文行楷",30,font.BOLD))
    root1.my_fonto = font.Font(font=("宋体",15,font.BOLD))
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")


    # msgbox.showinfo(title='提示消息框', message=message)

    # conn.sendall(message.encode('utf-8'))
    # funmun=conn.recv(1024).decode()

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label='菜单',menu=filemenu)
    m.add_cascade(label='主题',menu=filemenu1)
    for item in ["返回游戏","游戏大厅",'返回登录界面',"帮助","退出"]:

        if item == "返回游戏":
            filemenu.add_command(label=item,command=success_tip1)
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda: [root1.destroy(),loginui()])
        if item == "帮助":
            filemenu.add_command(label=item,command=clickexit)

    for item in ['青春','明亮']:

        if item == "青春":
            filemenu1.add_command(label=item,command=style2)
        if item == "明亮":
            filemenu1.add_command(label=item,command=style)
    # get_proe()
    txt = '---个人信息---'
    # message=conn.sendall(message.encode('utf-8'))

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
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('10.1.30.100',9002))
    server.listen(5)
    loginui()

