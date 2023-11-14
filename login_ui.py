# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        self.Login_page = QtWidgets.QWidget(Form)
        self.Login_page.setGeometry(QtCore.QRect(30, 30, 370, 480))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.Login_page.setFont(font)
        self.Login_page.setObjectName("Login_page")
        self.label = QtWidgets.QLabel(self.Login_page)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/Egg.jpg);\n"
"border-radius:20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Login_page)
        self.label_2.setGeometry(QtCore.QRect(40, 49, 280, 381))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,150);\n"
"border-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Login_page)
        self.label_3.setGeometry(QtCore.QRect(120, 70, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(105, 118, 132);")
        self.label_3.setObjectName("label_3")
        self.userID = QtWidgets.QLineEdit(self.Login_page)
        self.userID.setGeometry(QtCore.QRect(80, 140, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.userID.setFont(font)
        self.userID.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgb(105, 118, 132);\n"
"padding-bottom:7px;")
        self.userID.setObjectName("userID")
        self.password = QtWidgets.QLineEdit(self.Login_page)
        self.password.setGeometry(QtCore.QRect(80, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgb(105, 118, 132);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.Login_page)
        self.loginButton.setGeometry(QtCore.QRect(80, 260, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#loginButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"QPushButton#loginButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Login_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 360, 223, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(105, 118, 132);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    background-color: transparent; /* 배경색을 투명하게 설정 */\n"
"    color: rgba(85, 98, 112, 255); /* 기본 글꼴 색상 설정 */\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-left: 5px; /* 클릭 시 왼쪽 여백 추가 */\n"
"    padding-top: 5px; /* 클릭 시 위쪽 여백 추가 */\n"
"    color: rgba(91, 88, 53, 255); /* 클릭 시 글꼴 색상 변경 */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3 {\n"
"    background-color: transparent; /* 배경색을 투명하게 설정 */\n"
"    color: rgba(85, 98, 112, 255); /* 기본 글꼴 색상 설정 */\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    padding-left: 5px; /* 클릭 시 왼쪽 여백 추가 */\n"
"    padding-top: 5px; /* 클릭 시 위쪽 여백 추가 */\n"
"    color: rgba(91, 88, 53, 255); /* 클릭 시 글꼴 색상 변경 */\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background-color: transparent; /* 배경색을 투명하게 설정 */\n"
"    color: rgba(85, 98, 112, 255); /* 기본 글꼴 색상 설정 */\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover {\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-left: 5px; /* 클릭 시 왼쪽 여백 추가 */\n"
"    padding-top: 5px; /* 클릭 시 위쪽 여백 추가 */\n"
"    color: rgba(91, 88, 53, 255); /* 클릭 시 글꼴 색상 변경 */\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Login_page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 320, 197, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(105, 118, 132);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.createAccButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.createAccButton.setFont(font)
        self.createAccButton.setStyleSheet("QPushButton#createAccButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 50), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#createAccButton:hover {\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"\n"
"QPushButton#createAccButton:pressed {\n"
"    padding-left: 5px; /* 클릭 시 왼쪽 여백 추가 */\n"
"    padding-top: 5px; /* 클릭 시 위쪽 여백 추가 */\n"
"    color: rgba(91, 88, 53, 255); /* 클릭 시 글꼴 색상 변경 */\n"
"}")
        self.createAccButton.setObjectName("createAccButton")
        self.horizontalLayout_2.addWidget(self.createAccButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "LOG-IN"))
        self.userID.setPlaceholderText(_translate("Form", "ID"))
        self.password.setPlaceholderText(_translate("Form", " Password"))
        self.loginButton.setText(_translate("Form", "Log In"))
        self.label_4.setText(_translate("Form", "Login with Social media"))
        self.pushButton_2.setText(_translate("Form", "Ú"))
        self.pushButton_3.setText(_translate("Form", "À"))
        self.pushButton_4.setText(_translate("Form", "Í"))
        self.label_5.setText(_translate("Form", "Click to Sign up >>>"))
        self.createAccButton.setText(_translate("Form", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
