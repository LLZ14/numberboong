# 数字大爆炸



### py代码实现的一个小游戏

说明：

​	玩家打开游戏后会收到游戏提示，需要根据提来猜中数字。

例如：

​	提示：该数是一个三位数！（100-999）

​	玩家输入：520

​	提示：大了！（100-519）

​	玩家输入：444

​	提示：小了！（445-519）

​	玩家输入：456

​	提示：答对了，恭喜，今晚你请客！

#### 1，初步代码

```
import random
#随机生成
num = random.choice(range(0,999))
# num = 1000
#用于测试
#print(num)
i=0
num2 = num
onum = num
#计算位数
while onum >= 1 :
     onum=onum/10
     # print(onum)
     i += 1
# print(i)

#希望import引入简单的模块计算位数
# num2 = 10*10*10
print("提示：该数是一个",i,"位数")
# print("玩家请输入：")
x=int(input("玩家请输入："))
print(x)
# print(num2)
#记录对局次数
j=0
while(1):

    if x > num2:
        print("大了！")
        x=int(input("玩家请再输入："))
        j += 1
    if x < num2:
        print("小了！")
        x=int(input("玩家请再输入："))
        j += 1
    if x==num2:
        j += 1
        break
print("答对了，恭喜，今晚你请客！")
print("一共回答了",j,"次")
```



#### 2，图形界面输入输出

```
#采用PyQT GUI

https://github.com/alejandroautalan/pygubu-designer


用pygubu-designer进行设计
#!/usr/bin/python3
import tkinter as tk


class one(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(one, self).__init__(master, **kw)
        button1 = tk.Button(self)
        button1.configure(
            default="active",
            justify="right",
            relief="flat",
            state="active",
            text='确定')
        button1.grid(column=0, padx=10, row=3, sticky="e")
        entry1 = tk.Entry(self)
        entry1.grid(column=0, padx=80, row=2)
        menubutton1 = tk.Menubutton(self)
        menubutton1.configure(
            compound="bottom",
            font="TkDefaultFont",
            relief="ridge",
            text='———欢迎来到数字大爆炸———')
        menubutton1.grid(column=0, row=0, sticky="n")
        button2 = tk.Button(self)
        button2.configure(justify="left", takefocus=False, text='退出')
        button2.grid(column=0, padx=10, pady=20, row=3, sticky="w")
        message1 = tk.Message(self)
        message1.configure(
            justify="center",
            takefocus=False,
            text='请输入你猜的数字：',
            width=120)
        message1.grid(column=0, ipadx=50, ipady=30, pady=10, row=1)
        self.configure(padx=0, pady=0, relief="flat", takefocus=False)
        self.maxsize(600, 500)
        self.minsize(320, 400)
        self.overrideredirect("True")


if __name__ == "__main__":
    root = tk.Tk()
    widget = one(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

```

![image-20221106224559843](C:\Users\lin\AppData\Roaming\Typora\typora-user-images\image-20221106224559843.png)



```
#!/usr/bin/python3
import tkinter as tk


class TwoApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(padx=0, pady=0, relief="flat", takefocus=False)
        toplevel1.maxsize(600, 500)
        toplevel1.minsize(320, 400)
        toplevel1.overrideredirect("True")
        button1 = tk.Button(toplevel1)
        button1.configure(
            default="active",
            justify="right",
            relief="flat",
            state="active",
            text='确定')
        button1.grid(column=0, padx=10, row=3, sticky="e")
        entry1 = tk.Entry(toplevel1)
        entry1.grid(column=0, padx=80, row=2)
        menubutton1 = tk.Menubutton(toplevel1)
        menubutton1.configure(
            compound="bottom",
            font="TkDefaultFont",
            relief="ridge",
            text='———欢迎来到数字大爆炸———')
        menubutton1.grid(column=0, row=0, sticky="n")
        button2 = tk.Button(toplevel1)
        button2.configure(justify="left", takefocus=False, text='退出')
        button2.grid(column=0, padx=10, pady=20, row=3, sticky="w")
        message1 = tk.Message(toplevel1)
        message1.configure(
            justify="center",
            takefocus=False,
            text='请输入你猜的数字：',
            width=120)
        message1.grid(column=0, ipadx=50, ipady=30, pady=10, row=1)

        # Main widget
        self.mainwindow = toplevel1
        # Main menu
        _main_menu = self.create_menu8(self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)

    def run(self):
        self.mainwindow.mainloop()
        
#添加菜单
    def create_menu8(self, master):
        menu8 = tk.Menu(master)
        menu8.configure(
            activebackground="#0080ff",
            activeborderwidth=5,
            background="#ffffff",
            font="TkTextFont",
            foreground="#000000",
            relief="ridge",
            selectcolor="#ffffff",
            takefocus=True,
            tearoff="true",
            title='菜单')
        menu8.add("command", label='暂停游戏')
        menu8.add("command", label='退出游戏')
        menu8.add("command", label='帮助')
        return menu8


if __name__ == "__main__":
    app = TwoApp()
    app.run()



```













#### 3，打包exe文件

```
pyinstaller -Fw 
```

### py1.0

​	希望可以实现局域网内游戏

​	增加玩家数量，实现udp传输

​	增加玩家信息录入与显示

​	增加互动功能

​	增加对局记录

#### 1,图形化

<img src="C:\Users\lin\AppData\Roaming\Typora\typora-user-images\image-20221127144339857.png" alt="image-20221127144339857" style="zoom:50%;" />

```
显示一个Windows窗口，初始大小为800x600。
from tkinter import *
win = Tk();
win.geometry("800x600")
win.mainloop()					#进入消息循环，也就是显示窗口


from tkinter import *
root = Tk()
def hello():								#菜单项事件函数，可以每个菜单项单独写
    print("你单击主菜单")
m = Menu(root)
for item in ['文件','编辑','视图']: 				#添加菜单项
    m.add_command(label =item, command = hello)
root['menu'] = m							#附加主菜单到窗口
root.mainloop()



```

```
from tkinter import *
def hello():
    print(v.get())

root = Tk()
root.geometry('730x436')
root.title('numbong')
v = StringVar()
m = Menu(root)
filemenu = Menu(m)
filemenu1 = Menu(m)
for item in ['开始匹配','个人信息','退出']:
    filemenu.add_command(label =item, command = hello)
for item in ['back','white','blue']:
    filemenu1.add_command(label =item, command = hello)
m.add_cascade(label ='菜单', menu = filemenu)
m.add_cascade(label ='主题', menu = filemenu1)
# filemenu.add_checkbutton(label = '自动保存',command = hello,variable = v)
root['menu'] = m
root.mainloop()


```

```
登录注册

import  requests
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import pymysql

def success_tip(username):
    msgbox.showinfo(title='消息提示框', message= '登录成功')
    root.destroy()
    pass
def success_sign_tip():
    msgbox.showinfo(title='消息提示框', message= '注册成功')
    root.destroy()

def fail_tip():
    fail = msgbox.showerror(title='错误消息框', message='用户名或密码错误')
def fail_sign_tip():
    fail = msgbox.showerror(title='错误消息框', message='注册失败！')
def loginui():
    global input1,input2,root
    root = Tk()
    root.resizable(False,False)
    m=Menu(root)
    filemenu = Menu(m,tearoff="off")
    m.add_cascade(label ='选择模式', menu = filemenu,command=lambda:[root.destroy(),main_soneui()])
    for item in ["游客"]:
        if item == "游客":
            filemenu.add_command(label=item,command=lambda:[root.destroy(),main_soneui()])
    root.my_font=font.Font(font=("华文行楷",25,font.BOLD))
    root.my_font_two=font.Font(font=("宋体",15,font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width']=580;
    root['height']=300;
    Label(root,text ='登录界面',width=40,font=root.my_font).place(x=2,y=25)
    Label(root,text ='用户名',width=35,font=root.my_font_two ).place(x=2,y=100)
    input1=Entry(root,width=32)
    input1.place(x=240,y=100)
    Label(root,text ='密码',width=35,font=root.my_font_two).place(x=2,y=160)
    input2=Entry(root,width=32)
    input2.place(x=240,y=160)
    Button(root,text='登录',width=6,font=root.my_font_two,command=auto_login).place(x=235,y=210)
    Button(root,text='注册',width=6,font=root.my_font_two,command=lambda:[root.destroy(),sign_in()]).place(x=373,y=210)
    root['menu'] = m
    root.mainloop()

def sign_in():
    global inputone,inputtwo,inputthree,inputf
    root = Tk()
    root.resizable(False,False)
    root.my_font=font.Font(font=("华文行楷",25,font.BOLD))
    root.my_font_two=font.Font(font=("宋体",15,font.BOLD))
    root.my_font_th=font.Font(font=("宋体",12,font.BOLD))
    root.geometry('730x436+480+100')
    root.title("数字大爆炸V1.0")
    root['width']=580;
    root['height']=300;
    Label(root,text ='注册界面',width=40,font=root.my_font).place(x=2,y=25)
    Label(root,text ='用户名',width=35,font=root.my_font_two ).place(x=2,y=100)
    inputone=Entry(root,width=32)
    inputone.place(x=240,y=100)
    Label(root,text ='密码',width=35,font=root.my_font_two).place(x=2,y=160)
    inputtwo=Entry(root,width=32)
    inputtwo.place(x=240,y=160)
    Label(root,text ='密码',width=35,font=root.my_font_two).place(x=2,y=220)
    inputthree=Entry(root,width=32)
    inputthree.place(x=240,y=220)
    Label(root,text ='手机号',width=35,font=root.my_font_two).place(x=2,y=280)
    inputf=Entry(root,width=32)
    inputf.place(x=240,y=280)
    Button(root,text='返回登录',width=8,font=root.my_font_th,command=loginui).place(x=235,y=310)
    Button(root,text='注册',width=8,font=root.my_font_th,command=auto_sign).place(x=380,y=310)

    root.mainloop()

# def get_proe():
#   proe = requests.get("http://yijuzhan.com/api/word.php?m=json")
#   if proe.status_code != 200:
#     return get_proe()
#   re1 = proe.json()['content']
#   re2 = proe.json()['source']
#   return re1+re2
#   print(get_proe())


def auto_login():
    db = pymysql.connect(host='localhost', user='root', password='', database='stu', port=3306)
    cur = db.cursor()  # 获取操作游标
    sql = 'SELECT * FROM tstudent'
    entry1 = input1.get()
    entry2 = input2.get()
    flag = True
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    for row in results:
        username = row[1]
        password = row[2]
        print(username)
        print(password)

        if username == entry1 and password == entry2:
            print('登陆成功')
            username = row[0]
            success_tip(username)
            flag = True
            break
        else:
            flag = False
    if flag == False:
            fail_tip()

def auto_sign():
    db = pymysql.connect(host='localhost', user='root', password='', database='stu', port=3306)
    cur = db.cursor()  # 获取操作游标

    entryo = inputone.get()
    entryt = inputtwo.get()
    entryth = inputthree.get()
    entryf = inputf.get()
    flag = False
    if entryt == entryth :
        flag = True
        cur.execute('insert into user values ("%s","%s","%s")' % (entryo,entryt,entryf))
        success_sign_tip()
    else:
        flag = False
    if flag == False:
        fail_tip()

def loginfalse():
    print(111)
def tryone():
    print(111)
def hello1():
    print("6666")
def hello():
    msgbox.showinfo("提示","welcome to use this tool!")



def main_soneui():
    root1 = Tk()
    root1.resizable(False,False)
    root1.geometry('730x436+480+100')
    root1.title("数字大爆炸V1.0")

    m = Menu(root1)
    filemenu = Menu(m,tearoff="off")
    filemenu1 = Menu(m,tearoff="off")

    m.add_cascade(label ='菜单', menu = filemenu)
    m.add_cascade(label ='主题', menu = filemenu1)
    for item in ["个人信息","游戏大厅",'返回登录界面',"帮助"]:

        if item == "个人信息":
            filemenu.add_command(label=item,command="")
        if item == "游戏大厅":
            filemenu.add_command(label=item,command="")
        if item == "帮助":
            filemenu.add_command(label=item,command="")
        if item == "返回登录界面":
            filemenu.add_command(label=item,command=lambda:[root1.destroy(),loginui()])

    for item in ['暗黑','明亮']:

        if item == "暗黑":
            filemenu1.add_command(label=item,command="")
        if item == "明亮":
            filemenu1.add_command(label=item,command="")
    root1['menu'] = m



    root1.mainloop()



if __name__ == '__main__':
    # style = Style(theme='sandstone')
    loginui()



```



#### 2,基础实现代码

```
import random
#随机生成
num = random.choice(range(0,999))
# num = 1000
#用于测试
#print(num)
i=0
num2 = num
onum = num
#计算位数
while onum >= 1 :
     onum=onum/10
     # print(onum)
     i += 1
# print(i)

#希望import引入简单的模块计算位数
# num2 = 10*10*10
print("提示：该数是一个",i,"位数")
# print("玩家请输入：")
x=int(input("玩家请输入："))
print(x)
# print(num2)
#记录对局次数
j=0
while(1):

    if x > num2:
        print("大了！")
        x=int(input("玩家请再输入："))
        j += 1
    if x < num2:
        print("小了！")
        x=int(input("玩家请再输入："))
        j += 1
    if x==num2:
        j += 1
        break
print("答对了，恭喜，今晚你请客！")
print("一共回答了",j,"次")
```

#### 3,网络编程

​	Server端

```

```

​	client
