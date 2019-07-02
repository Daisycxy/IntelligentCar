import sys
import pymysql
import time
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 连接mysql
db = pymysql.connect("localhost", "root", "Question0901-", "my_db", charset='utf8')
# 设置游标
# cursor = db.cursor()
# sql语句
# cursor.execute("SELECT py FROM my_db.directive")
# 设置游标
#设置数组
arrr=["w","a","s","d",""]
#判断状态 0为初始化，1为普通，2为自动，3为循迹
flag=0;

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI(self)
    def initUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(back/back.jpg);}")
        self.setWindowIcon(QtGui.QIcon('back/icon.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 220, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 280, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 280, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.open_conn = QtWidgets.QPushButton(self.centralwidget)
        self.open_conn.setGeometry(QtCore.QRect(50, 80, 201, 91))
        self.open_conn.setObjectName("disconn")
        self.open_conn.setStyleSheet("QPushButton{border-image:url('button/open_conn1.png'); }"
                                   "QPushButton:hover{border-image:url('button/open_conn2.png');}"
                                   "QPushButton:pressed{border-image:url('button/open_conn3.png'); }")
        self.open_conn.clicked.connect(self.on_click9)
        self.disconn = QtWidgets.QPushButton(self.centralwidget)
        self.disconn.setGeometry(QtCore.QRect(500, 80, 201, 91))
        self.disconn.setObjectName("disconn")
        self.disconn.setStyleSheet("QPushButton{border-image:url('button/disconn1.png'); }"
                                 "QPushButton:hover{border-image:url('button/disconn2.png');}"
                                 "QPushButton:pressed{border-image:url('button/disconn3.png'); }")
        self.disconn.clicked.connect(self.on_click10)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(50, 370, 201, 91))
        self.start.setObjectName("start")
        self.start.setStyleSheet("QPushButton{border-image:url('button/start1.png'); }"
                                 "QPushButton:hover{border-image:url('button/start2.png');}"
                                 "QPushButton:pressed{border-image:url('button/start3.png'); }")
        self.start.clicked.connect(self.on_click1)
        self.automatic = QtWidgets.QPushButton(self.centralwidget)
        self.automatic.setGeometry(QtCore.QRect(50, 460, 201, 91))
        self.automatic.setObjectName("automatic")
        self.automatic.setStyleSheet("QPushButton{border-image:url('button/automatic1.png'); }"
                                     "QPushButton:hover{border-image:url('button/automatic2.png');}"
                                     "QPushButton:pressed{border-image:url('button/automatic3.png'); }")
        self.automatic.clicked.connect(self.on_click2)
        self.tracking = QtWidgets.QPushButton(self.centralwidget)
        self.tracking.setGeometry(QtCore.QRect(50, 550, 201, 91))
        self.tracking.setObjectName("tracking")
        self.tracking.setStyleSheet("QPushButton{border-image:url('button/tracking1.png'); }"
                                    "QPushButton:hover{border-image:url('button/tracking2.png');}"
                                    "QPushButton:pressed{border-image:url('button/tracking3.png'); }")
        self.tracking.clicked.connect(self.on_click3)
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(500, 300, 111, 111))
        self.forward.setObjectName("forward")
        self.forward.setStyleSheet("QPushButton{border-image:url('button/forward1.png'); }"
                                   "QPushButton:hover{border-image:url('button/forward2.png');}"
                                   "QPushButton:pressed{border-image:url('button/forward3.png'); }")
        self.forward.clicked.connect(self.on_click4)
        self.retreat = QtWidgets.QPushButton(self.centralwidget)
        self.retreat.setGeometry(QtCore.QRect(500, 540, 111, 111))
        self.retreat.setObjectName("retreat")
        self.retreat.setStyleSheet("QPushButton{border-image:url('button/retreat1.png'); }"
                                   "QPushButton:hover{border-image:url('button/retreat2.png');}"
                                   "QPushButton:pressed{border-image:url('button/retreat3.png'); }")
        self.retreat.clicked.connect(self.on_click5)
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(380, 420, 111, 111))
        self.left.setObjectName("left")
        self.left.setStyleSheet("QPushButton{border-image:url('button/left1.png'); }"
                                "QPushButton:hover{border-image:url('button/left2.png');}"
                                "QPushButton:pressed{border-image:url('button/left3.png'); }")
        self.left.clicked.connect(self.on_click6)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(620, 420, 111, 111))
        self.right.setObjectName("right")
        self.right.setStyleSheet("QPushButton{border-image:url('button/right1.png'); }"
                                 "QPushButton:hover{border-image:url('button/right2.png');}"
                                 "QPushButton:pressed{border-image:url('button/right3.png'); }")
        self.right.clicked.connect(self.on_click7)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(500, 420, 111, 111))
        self.stop.setObjectName("stop")
        self.stop.setStyleSheet("QPushButton{border-image:url('button/stop1.png'); }"
                                "QPushButton:hover{border-image:url('button/stop2.png');}"
                                "QPushButton:pressed{border-image:url('button/stop3.png'); }")
        self.stop.clicked.connect(self.on_click8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IntelligentCar"))
        self.label.setText(_translate("MainWindow", "当前识别物体："))
        self.label_2.setText(_translate("MainWindow", "当前状态："))
        self.automatic.setText(_translate("MainWindow", " "))
        self.tracking.setText(_translate("MainWindow", " "))
        self.start.setText(_translate("MainWindow", " "))
        self.forward.setText(_translate("MainWindow", " "))
        self.retreat.setText(_translate("MainWindow", " "))
        self.left.setText(_translate("MainWindow", " "))
        self.right.setText(_translate("MainWindow", " "))
        self.stop.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", "---"))
        self.label_4.setText(_translate("MainWindow", "---"))
        self.disconn.setText(_translate("MainWindow", ""))
        self.open_conn.setText(_translate("MainWindow", ""))
        
    @pyqtSlot()
    def on_click1(self):
            self.label_4.setText("普通模式")
            print("开始")
    def on_click2(self):
            self.label_4.setText("自动行驶")
            print("自动行驶")
    def on_click3(self):
        self.label_4.setText("循迹行驶")
        print("循迹行驶")
    def on_click4(self):
            cursor = db.cursor()
            cursor.execute("update car set id=id+1 where id>=1")
            cursor.execute("update car set bc=bc+2 where bc>=1")
            cursor.execute("INSERT INTO car values('1','w','1')");
            db.commit();
            print("前进")
    def on_click5(self):
        #普通模式
            cursor = db.cursor()
            cursor.execute("update car set id=id+1 where id>=1")
            cursor.execute("update car set bc=bc+2 where bc>=1")
            cursor.execute("INSERT INTO car values('1','s','1')");
            db.commit();
            print("后退")

    def on_click6(self):
        #普通模式
            cursor = db.cursor()
            cursor.execute("update my_db.car set id=id+1 where id>=1")
            cursor.execute("update my_db.car set bc=bc+2 where bc>=1")
            cursor.execute("INSERT INTO car values('1','a','1')");
            db.commit();
            print("左转")
    def on_click7(self):
        # 普通模式
            cursor = db.cursor()
            cursor.execute("update my_db.car set id=id+1 where id>=1")
            cursor.execute("update my_db.car set bc=bc+2 where bc>=1")
            cursor.execute("INSERT INTO car values('1','d','1')");
            db.commit();
            print("右转")
        #
    def on_click8(self):
        cursor = db.cursor()
        cursor.execute("update my_db.car set id=id+1 where id>=1")
        cursor.execute("update my_db.car set bc=bc+2 where bc>=1")
        cursor.execute("INSERT INTO car values('1','0','1')");
        db.commit();
        flag=0;
        self.label_4.setText("---")
        print("停止")
    def on_click9(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        QMessageBox.information(self,"Information","Connect Successfully!")
        print("开启连接")
    def on_click10(self):
        QMessageBox.information(self, "Information", "Remove Connection Successfully!")
        db.close()
        print("断开连接")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
