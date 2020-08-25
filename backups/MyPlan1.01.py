# coding=gbk
# ������ջ�
# ��������ȫ�ֱ��������崰��λ�ã�ʹ�ô������ࣩܶ�����ڸ���

import sys,json,time,os,random
from PyQt5.QtWidgets import QMenu,QApplication,QFontDialog,QSpinBox,QMessageBox,QInputDialog,QTextBrowser,\
    QMainWindow,QPushButton,QFileDialog,QCheckBox,QAction ,QLabel,QTextEdit,QLCDNumber,QLineEdit
from PyQt5 import QtCore,QtGui
#ȫ�ֱ���
INILAB = (10, 300)

class MyPlan(QMainWindow):

    def __init__(self):
        super().__init__()
        # ʱ���׼��ʼ��
        self.minute = 49
        self.mic = 59
        self.second = 59
        self.iniUI()

    def iniUI(self):
        """
        ��ʼ��ui
        :return:
        """
        # ����
        self.move(1100,0)
        self.setFixedSize(247, 725)
        self.setWindowTitle('MyPlan1.01')
        image = QtGui.QPixmap()
        image.load(r"myresource/����.jpg")
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(image)) #����ͼƬ
        # palette1.setColor(self.backgroundRole(), QtGui.QColor(192, 253, 123))  # ������ɫ
        self.setPalette(palette1)
        # self.setAutoFillBackground(False)


        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # ʹ����С����ť
                            QtCore.Qt.WindowCloseButtonHint |      # ʹ�ܹرհ�ť
                            QtCore.Qt.WindowStaysOnTopHint)        # ����������ǰ��

        # ״̬��
        self.my_menubar()
        # �ı���
        self.textbox()
        # չ�ֱ�ǩ
        self.my_showlab()
        # չ�ְ���
        self.my_bottonpush()
        # ���չ����������
        self.show()


    def textbox(self):
        """
        ���������
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


        self.myok.setText('�������')
        self.myok.stateChanged.connect(self.readline)

    def readline(self):
        # ��ȡ����
        with open('myresource/my_plan.txt', 'r', encoding='UTF-8') as f:
            self.lt.setText(f.readline())
            # ִ�����ʣ��ƻ�
            remainplan = f.read().replace(f.readline(), "")
            self.tx.setText(remainplan)

            with open('myresource/my_plan.txt', 'w', encoding='UTF-8') as f:
                # ����д������
                f.write(remainplan)



    def my_bottonpush(self):
        """
        �ҵİ���
        :return:
        """
        self.btstart = QPushButton('��ʼ', self)
        self.btfunc = QPushButton('����', self)
        self.btplan = QPushButton('���ؼƻ�', self)
        self.btsave = QPushButton('����ʼ�', self)

        self.btstart.setGeometry(170, 30, 71, 31)
        self.btfunc.setGeometry(10, 230, 75, 23)
        self.btplan.setGeometry(160, 230, 75, 23)
        self.btsave.setGeometry(160, 690,75,23)
        # ����������ʾ
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
        �ҵı�ǩ
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
        # font.setFamily("Arial")  # ������������ó��Լ���Ҫ����������
        # font.setPointSize(18)  # ����������ֿ������ó��Լ���Ҫ�������С

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
        self.btTarget.setText('��ǰĿ��')
        self.btTarget.clicked.connect(self.showDialog)

        self.lab1.setText('successful')
        self.lab2.setText('failure')
        self.lab3.setText('fool')
        self.lab4.setText('�ƻ��Ǻ��ģ���������������')
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
        text, ok = QInputDialog.getText(self, '��ǰĿ��', '�����뵱ǰĿ�꣺')
        if ok:
            self.labdirection.setText(text)

    def timestart(self):
        """
        ��Ʋ���ˢ���¼�
        :return:
        """
        self.time = QtCore.QTimer()
        self.time.start()
        # ˢ�´�����������Interval�Ǽ��
        self.time.setInterval(15)
        # ˢ���¼�������ʵ����ֻ���������¼�ѭ���ﲻ��ˢ�£�����Ĵ������һ��ִ��һ��
        self.time.timeout.connect(self.ontime)

    def ontime(self):
        """
        ���ÿ��ˢ��ʱ��ֵ��
        :return:
        """
        self.mic -= 1
        if self.mic == 0:
            self.second -= 1
            self.mic = 59
        if self.second == 0:
            self.second = 59
            self.minute -= 1
        # �����һ�֣��ı���degree + 1
        if self.minute < 0:
            self.minute = 49
            self.mic = 59
            self.second = 59
            self.readline()
            # ִ��ֹͣ�¼�
            self.time.stop()
            # ת���ȴ�ִ��
            self.btstart.clicked.connect(self.timestart)
        # ��ʽ�� display������print
        self.lcd.display('%2d:%2d:%2d'%(self.minute,self.second,self.mic))

    def my_menubar(self):
        """
        �˵�������
        :return:
        """
        menubar = self.menuBar()
        # û��self������Ϊ����˵��Ǹ����ڴ��ڵģ��Ӳ˵�Ҳ����self
        file = menubar.addMenu('�ļ�(&F)')
        self.loadfile = QAction('���ļ�(&O)', self)
        savefile = QAction('�����ļ��ļ�(&s)', self)
        # ���ܲ˵�
        loadfunc = QMenu('����ģ��', self)
        # ���ӹ���
        self.setfont = QAction('��������', self)
        self.background = QAction('����ѡ��',self)
        self.setfont.triggered.connect(self.choicefont)
        loadfunc.addAction(self.setfont)
        self.loadfile.triggered.connect(self.openfile)
        # ���ϴ��ӹ���
        file.addAction(self.loadfile)
        file.addAction(savefile)
        file.addSeparator()
        file.addMenu(loadfunc)

    def my_award(self):
        """
        �����ı�����
        :return:
        """
        with open('myresource/award.txt', 'r', encoding='UTF-8') as f:
            # �滻��""�������ַ���������ʹ��json
            content = f.read().replace("'", '"')
            # json.loads ���ַ����ı�ת�� ���ݽṹ�����ֵ�orԪ��)
            # ע��һ�μ����ַ������������޵Ĵ��Ϊ300��
            long_list_data = json.loads(content)
            # �����ȡ�б���һ��С�б�[0]��Ϊȥ���ţ���Ϊloadsת��ʱ���һ������
            short_list_data = random.choices(long_list_data)[0]
            # ʹ��choices���ɵ�Ҳ���б�
            data = random.choices(short_list_data)[0]
            QMessageBox.about(self,'��������',data)

            # �������в������޷���ԭ���ļ���������,Ҫֱ�Ӷ����ݽ��в���
            num = long_list_data.index(short_list_data)
            # ɾ���б�������
            short_list_data.remove(data)
            # ���ԭ�б���滻
            long_list_data[num] = short_list_data
            with open('myresource/award.txt', 'w', encoding='UTF-8') as f:
                # ����д������
                f.write(str(long_list_data))

    def openfile(self):
        """
        ���ļ�
        :return:
        """
        fname = QFileDialog.getOpenFileName(self, '���ļ�','./')
        # fname[0] ·��
        if fname[0]:
            with open(fname[0], 'r',encoding='UTF-8',errors='ignore') as f:
                self.tx.setText(f.read())

    def choicefont(self):
        # �˵�������������
        font, ok = QFontDialog.getFont()
        if ok:
            # ��������Current,ֻ������current
            self.btx.setCurrentFont(font)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'ȷ��', '��������û������', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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

