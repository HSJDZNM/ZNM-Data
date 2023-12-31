# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class Ui_Form(object):

    def __init__(self):
        self.count_max = 5
        self.count_right = 0
        self.count = 0
        self.count_wrong = 0

    def on_return_pressed(self):
        # 在按下回车键时清空 QLineEdit 的内容
        self.lineEdit_input.clear()

    def generate_question(self):
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        op = random.choice(['+', '-', '*', '/'])
        if op == '-':
            if num1 < num2:
                num1, num2 = num2, num1
        elif op == '/':
            if num1 == 0:
                num1, num2 = num2, num1
        return num1, op, num2

    def check_answer(self, num1, op, num2, answer):
        if op == '+':
            if num1 + num2 == answer:
                return True
        elif op == '/':
            if num1 / num2 == answer:
                return True
        elif op == '*':
            if num1 * num2 == answer:
                return True
        else:
            if num1 - num2 == answer:
                return True
        return False

    def counter(self):
        if self.count_right < self.count_max:
            self.count += 1
            self.num1, self.op, self.num2 = self.generate_question()
            print(f"第{self.count}题 {self.num1} {self.op} {self.num2} = ")
            self.label_arithmetic.setText(f"{self.num1} {self.op} {self.num2} = ")
            self.answer_text = self.lineEdit_input.text()
        else:
            print(f"共{self.count}题，你答对了{self.count_right}题！")
            self.label_record.setText(f"共{self.count}题，你答对了{self.count_right}题！")
            self.answer = None

    def judgment(self):
        self.counter()
        try:
            self.answer = int(self.answer_text)
            if not self.check_answer(self.num1, self.op, self.num2, self.answer):
                print("很遗憾，答错了！")
                self.label.setText("很遗憾，答错了！")
                self.lineEdit_input.clear()
                self.count_wrong += 1
                if self.count_wrong == 5:
                    print(f"答错五次,答案是{self.num1}{self.op}{self.num2}={self.answer}")
                    self.label_arithmetic.setText(f"答错五次,答案是{self.num1}{self.op}{self.num2}={self.answer}")
            else:
                print("恭喜你，答对了！")
                self.label.setText("恭喜你，答对了！")
                self.lineEdit_input.clear()
                self.count_right += 1
        except ValueError:
            print("请输入整数！")
            self.label.setText("请输入整数！")
            self.lineEdit_input.clear()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 500)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(30, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_arithmetic = QtWidgets.QLabel(Form)
        self.label_arithmetic.setGeometry(QtCore.QRect(30, 90, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_arithmetic.setFont(font)
        self.label_arithmetic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arithmetic.setObjectName("label_arithmetic")
        self.label_record = QtWidgets.QLabel(Form)
        self.label_record.setGeometry(QtCore.QRect(254, 31, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_record.setFont(font)
        self.label_record.setAlignment(QtCore.Qt.AlignCenter)
        self.label_record.setObjectName("label_record")
        self.lineEdit_input = QtWidgets.QLineEdit(Form)
        self.lineEdit_input.setGeometry(QtCore.QRect(170, 250, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lineEdit_input.text()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 190, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(430, 330, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(lambda: self.judgment())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 为 QLineEdit 添加按下回车键的事件
        self.lineEdit_input.returnPressed.connect(self.on_return_pressed)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form",
                                            "<html><head/><body><p><span style=\" "
                                            "font-weight:600;\">题目:</span></p></body></html>"))
        self.label_arithmetic.setText(_translate("Form", "<html><head/><body><p>式子</p></body></html>"))
        self.label_record.setText(_translate("Form", "计数"))
        self.lineEdit_input.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "状态"))
        self.pushButton_start.setText(_translate("Form", "开始"))




class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
