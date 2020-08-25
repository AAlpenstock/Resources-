# coding=gbk
# 经验和收获
# 可以设置全局变量来定义窗口位置（使用次数不能多），便于更改

import sys,json,time,os,random
from PyQt5.QtWidgets import QMenu,QApplication,QFontDialog,QSpinBox,QMessageBox,QInputDialog,QTextBrowser,\
    QMainWindow,QPushButton,QFileDialog,QCheckBox,QAction ,QLabel,QTextEdit,QLCDNumber,QLineEdit
from PyQt5 import QtCore,QtGui
#全局变量
INILAB = (10, 300)

class MyPlan(QMainWindow):

    def __init__(self):
        super().__init__()
        # 时间标准初始化
        self.minute = 49
        self.mic = 59
        self.second = 59
        self.iniUI()

    def iniUI(self):
        """
        初始化ui
        :return:
        """
        # 窗口
        self.move(1100,0)
        self.setFixedSize(247, 725)
        self.setWindowTitle('MyPlan1.01')
        image = QtGui.QPixmap()
        image.load(r"myresource/花儿.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(image)) #背景图片
        # palette1.setColor(self.backgroundRole(), QtGui.QColor(192, 253, 123))  # 背景颜色
        self.setPalette(palette1)
        # self.setAutoFillBackground(False)


        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            QtCore.Qt.WindowCloseButtonHint |      # 使能关闭按钮
                            QtCore.Qt.WindowStaysOnTopHint)        # 窗体总在最前端

        # 状态栏
        self.my_menubar()
        # 文本框
        self.textbox()
        # 展现标签
        self.my_showlab()
        # 展现按键
        self.my_bottonpush()
        # 最后展现上面内容
        self.show()


    def textbox(self):
        """
        设置输入框
        :return:
        """
        self.lt = QLineEdit(self)
        self.myok = QCheckBox(self)
        self.tx = QTextBrowser(self)
        self.btx = QTextEdit(self)

        self.lt.setGeometry(10, 120, 231, 20)
        self.myok.setGeometry(180, 150, 68, 16)
        self.tx.setGeometry(10, 170, 231, 58)
        self.btx.setGeometry(10, 370, 231, 310)


        self.myok.setText('完成任务')
        self.myok.stateChanged.connect(self.readline)

    def readline(self):
        # 读取行数
        with open('myresource/my_plan.txt', 'r', encoding='UTF-8') as f:
            self.lt.setText(f.readline())
            # 执行完后剩余计划
            remainplan = f.read().replace(f.readline(), "")
            self.tx.setText(remainplan)

            with open('myresource/my_plan.txt', 'w', encoding='UTF-8') as f:
                # 重新写入内容
                f.write(remainplan)



    def my_bottonpush(self):
        """
        我的按键
        :return:
        """
        self.btstart = QPushButton('开始', self)
        self.btfunc = QPushButton('功能', self)
        self.btplan = QPushButton('加载计划', self)
        self.btsave = QPushButton('保存笔记', self)

        self.btstart.setGeometry(170, 30, 71, 31)
        self.btfunc.setGeometry(10, 230, 75, 23)
        self.btplan.setGeometry(160, 230, 75, 23)
        self.btsave.setGeometry(160, 690,75,23)
        # 设置数字显示
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(20, 30, 140, 60)
        self.lcd.setDigitCount(8)
        self.btstart.clicked.connect(self.timestart)
        self.btplan.clicked.connect(self.autoplan)
        # self.btfunc.clicked.connect(self.my_messsage)
        self.btsave.clicked.connect(self.btsavefile)

    def autoplan(self):
        with open('myresource/my_plan.txt','r',encoding='UTF-8',errors='ignore') as f:
            self.tx.setText(f.read())

    def btsavefile(self):
        my_time = time.asctime(time.localtime())[4:10]
        if os.path.exists(f'C:/Users/Administrator/PycharmProjects/untitled/MyPlan1.0/myresource/2020{my_time}.txt'):
            with open(f'myresource/2020{my_time}.txt', 'a', encoding='UTF-8', errors='ignore') as f:
                f.write(self.btx.toPlainText())
                self.btx.setText("")
        else:
            with open(f'myresource/2020{my_time}.txt','w',encoding='UTF-8',errors='ignore') as f:
                f.write(self.btx.toPlainText())




    def my_showlab(self):
        """
        我的标签
        :return:
        """
        self.lab1 = QLabel(self)
        self.lab2 = QLabel(self)
        self.lab3 = QLabel(self)
        self.lab4 = QLabel(self)
        self.Sb4 = QSpinBox(self)
        self.Sb5 = QSpinBox(self)
        self.Sb6 = QSpinBox(self)

        self.Sb4.setRange(0, 100)
        self.Sb5.setRange(0, 100)
        self.Sb6.setRange(0, 100)

        self.Sb4.setSingleStep(1)
        self.Sb5.setSingleStep(1)
        self.Sb6.setSingleStep(1)

        self.lab1.setStyleSheet(
            "border-image: url(source/None.png);color:rgb(47,79,79);font-size:14px;font-family:SimSun;")
        self.lab2.setStyleSheet(
            "border-image: url(source/None.png);color:rgb(47,79,79);font-size:14px;font-family:SimSun;")
        self.lab3.setStyleSheet(
            "border-image: url(source/None.png);color:rgb(47,79,79);font-size:14px;font-family:SimSun;")
        self.lab4.setStyleSheet(
            "border-image: url(source/None.png);color:rgb(0,0,205);font-size:15px;font-family:Georgia;")
        # font = QtGui.QFont()
        # font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        # font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小

        self.labdirection = QLabel(self)
        self.labdirection.setStyleSheet("border-image: url(source/None.png);color:rgb(255,0,0);font-size:25px;font-family:SimSun;")

        x, y = INILAB
        self.lab1.move(x, y)
        self.lab2.move(x, y+20)
        self.lab3.move(x, y+40)
        self.lab4.setGeometry(x, y-50, 250, 60)
        self.Sb4.setGeometry(x+90, y+5, 30, 20)
        self.Sb5.setGeometry(x+90, y+25, 30, 20)
        self.Sb6.setGeometry(x+90, y+45, 30, 20)
        self.labdirection.setGeometry(x+157,y+30,80,40)

        self.btTarget = QPushButton(self)
        self.btTarget.setGeometry(x+150, y,75, 23)
        self.btTarget.setText('当前目标')
        self.btTarget.clicked.connect(self.showDialog)

        self.lab1.setText('successful')
        self.lab2.setText('failure')
        self.lab3.setText('fool')
        self.lab4.setText('计划是核心，任务奖励满足需求')
        with open('myresource/keep.txt', 'r', encoding='UTF-8', errors='ignore') as f:
            content = f.read()
            content = content.replace("'", '"')
            self.data = json.loads(content)

            self.Sb4.setValue(int(self.data['successful']))
            self.Sb5.setValue(int(self.data['failure']))
            self.Sb6.setValue(int(self.data['fool']))
        if int(self.data['successful']) % 9 == 0 and int(self.data['successful']) != 0:
            self.my_award()



    def showDialog(self):
        text, ok = QInputDialog.getText(self, '当前目标', '请输入当前目标：')
        if ok:
            self.labdirection.setText(text)

    def timestart(self):
        """
        设计槽里刷新事件
        :return:
        """
        self.time = QtCore.QTimer()
        self.time.start()
        # 刷新次数，在这里Interval是间距
        self.time.setInterval(15)
        # 刷新事件开启，实际上只有它会在事件循环里不断刷新，上面的代码调用一次执行一次
        self.time.timeout.connect(self.ontime)

    def ontime(self):
        """
        设计每次刷新时数值，
        :return:
        """
        self.mic -= 1
        if self.mic == 0:
            self.second -= 1
            self.mic = 59
        if self.second == 0:
            self.second = 59
            self.minute -= 1
        # 坚持玩一轮，文本里degree + 1
        if self.minute < 0:
            self.minute = 49
            self.mic = 59
            self.second = 59
            self.readline()
            # 执行停止事件
            self.time.stop()
            # 转到等待执行
            self.btstart.clicked.connect(self.timestart)
        # 格式化 display类似于print
        self.lcd.display('%2d:%2d:%2d'%(self.minute,self.second,self.mic))

    def my_menubar(self):
        """
        菜单栏设置
        :return:
        """
        menubar = self.menuBar()
        # 没有self，是因为这个菜单是附加在窗口的，子菜单也得用self
        file = menubar.addMenu('文件(&F)')
        self.loadfile = QAction('打开文件(&O)', self)
        savefile = QAction('保存文件文件(&s)', self)
        # 功能菜单
        loadfunc = QMenu('功能模块', self)
        # 待加功能
        self.setfont = QAction('字体设置', self)
        self.background = QAction('背景选择',self)
        self.setfont.triggered.connect(self.choicefont)
        loadfunc.addAction(self.setfont)
        self.loadfile.triggered.connect(self.openfile)
        # 以上待加功能
        file.addAction(self.loadfile)
        file.addAction(savefile)
        file.addSeparator()
        file.addMenu(loadfunc)

    def my_award(self):
        """
        奖励文本读入
        :return:
        """
        with open('myresource/award.txt', 'r', encoding='UTF-8') as f:
            # 替换成""包裹的字符串，方便使用json
            content = f.read().replace("'", '"')
            # json.loads 将字符串文本转换 数据结构（可字典or元组)
            # 注意一次加载字符串数量是有限的大概为300多
            long_list_data = json.loads(content)
            # 随机获取列表里一个小列表，[0]是为去括号，因为loads转换时会加一层括号
            short_list_data = random.choices(long_list_data)[0]
            # 使用choices生成的也是列表
            data = random.choices(short_list_data)[0]
            QMessageBox.about(self,'奖励窗口',data)

            # 对子序列操作是无法对原有文件产生作用,要直接对内容进行操作
            num = long_list_data.index(short_list_data)
            # 删子列表里数据
            short_list_data.remove(data)
            # 完成原列表的替换
            long_list_data[num] = short_list_data
            with open('myresource/award.txt', 'w', encoding='UTF-8') as f:
                # 重新写入内容
                f.write(str(long_list_data))

    def openfile(self):
        """
        打开文件
        :return:
        """
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')
        # fname[0] 路径
        if fname[0]:
            with open(fname[0], 'r',encoding='UTF-8',errors='ignore') as f:
                self.tx.setText(f.read())

    def choicefont(self):
        # 菜单栏，字体设置
        font, ok = QFontDialog.getFont()
        if ok:
            # 字体是用Current,只有它有current
            self.btx.setCurrentFont(font)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '都保存了没！！！', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            with open('myresource/keep.txt', 'w', encoding='UTF-8', errors='ignore') as f:
                date = dict()
                date['successful'] = self.Sb4.text()
                date['failure'] = self.Sb5.text()
                date['fool'] = self.Sb6.text()
                f.write(str(date))
            event.accept()
        else:
            event.ignore()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPlan()
    sys.exit(app.exec_())

