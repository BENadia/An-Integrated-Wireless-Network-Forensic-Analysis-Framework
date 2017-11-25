# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultatEvil.ui'
#
# Created: Sun Jun 15 19:11:02 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName(_fromUtf8("Dialog3"))
        Dialog3.resize(1205, 649)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog3.setPalette(palette)
        Dialog3.setStyleSheet(_fromUtf8("#Dialog3{\n"
"border:2px solid #1e2bd4;\n"
"border-radius: 1 px;\n"
"background: white;\n"
"}\n"
"#Top_frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4fe;\n"
"}\n"
"QLineEdit {\n"
"\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid #1e2bd4;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"color: #1e2bd4;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e2bd4, stop: 0.1 #1e2bd4, stop: 0.70#1e2bd4, stop: 0.5 #1e2bd4, stop: 1 #1e2bd4);\n"
"border-width: 1px;\n"
"border-color: #1e2bd4;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 6px;\n"
"\n"
"padding-left: 6px;\n"
"padding-right: 5px;\n"
"min-width: 90px;\n"
"max-width: 90px;\n"
"min-height: 14px;\n"
"max-height: 14px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background:#d0e4fe;\n"
"border-color:#1e2bd4;\n"
"border-width: 2px ;\n"
"border-style: solid ;\n"
"border-radius: 10;\n"
"padding:4px;\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"}"))
        Dialog3.setModal(True)
        self.Top_frame = QtGui.QFrame(Dialog3)
        self.Top_frame.setGeometry(QtCore.QRect(10, 10, 1191, 51))
        self.Top_frame.setStyleSheet(_fromUtf8("#Top_frame{\n"
"background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.Top_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Top_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Top_frame.setObjectName(_fromUtf8("Top_frame"))
        self.gridLayout = QtGui.QGridLayout(self.Top_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.Top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.Top_frame)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.Top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.Top_frame)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.Top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.Top_frame)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 0, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.Top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:white;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.Top_frame)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 0, 7, 1, 1)
        self.frame = QtGui.QFrame(Dialog3)
        self.frame.setGeometry(QtCore.QRect(10, 70, 1181, 591))
        self.frame.setStyleSheet(_fromUtf8("#frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_7 = QtGui.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(570, 540, 121, 46))
        self.frame_7.setStyleSheet(_fromUtf8("#frame_7{\n"
"border:#8bf;\n"
"}"))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton = QtGui.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)
        self.Left_frame = QtGui.QFrame(self.frame)
        self.Left_frame.setGeometry(QtCore.QRect(0, 10, 648, 327))
        self.Left_frame.setStyleSheet(_fromUtf8("#Left_frame{\n"
"border:#8bf;\n"
"}"))
        self.Left_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Left_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Left_frame.setObjectName(_fromUtf8("Left_frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Left_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_9 = QtGui.QLabel(self.Left_frame)
        self.label_9.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 2)
        self.label_10 = QtGui.QLabel(self.Left_frame)
        self.label_10.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.Left_frame)
        self.label_6.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_2.addWidget(self.lineEdit_8, 2, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.Left_frame)
        self.label_7.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_2.addWidget(self.lineEdit_9, 3, 1, 1, 2)
        self.label_8 = QtGui.QLabel(self.Left_frame)
        self.label_8.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_2.addWidget(self.lineEdit_14, 4, 1, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout_2.addWidget(self.lineEdit_10, 4, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.Left_frame)
        self.label_11.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 5, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.Left_frame)
        self.label_5.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 2)
        self.lineEdit_11 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout_2.addWidget(self.lineEdit_11, 6, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.Left_frame)
        self.label_12.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout_2.addWidget(self.lineEdit_12, 7, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.Left_frame)
        self.label_14.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 8, 0, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.Left_frame)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_2.addWidget(self.lineEdit_13, 8, 2, 1, 1)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, 370, 1181, 161))
        self.frame_2.setStyleSheet(_fromUtf8("#frame_2{\n"
"border:#8bf;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.tableWidget_4 = QtGui.QTableWidget(self.frame_2)
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 40, 591, 111))
        self.tableWidget_4.setStyleSheet(_fromUtf8("background:#ffffff;"))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_2 = QtGui.QTableWidget(self.frame_2)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(690, 40, 471, 111))
        self.tableWidget_2.setStyleSheet(_fromUtf8("background:#ffffff;"))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.frame_5 = QtGui.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(30, 0, 591, 41))
        self.frame_5.setStyleSheet(_fromUtf8("#frame_5{\n"
"background:white;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_18 = QtGui.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("color:#1e2bd4"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)
        self.frame_6 = QtGui.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(690, 0, 471, 41))
        self.frame_6.setStyleSheet(_fromUtf8("#frame_6{\n"
"background:white;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"}"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_16 = QtGui.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("color:#1e2bd4"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(660, 10, 511, 351))
        self.frame_3.setStyleSheet(_fromUtf8("#frame_3{\n"
"border:#8bf;\n"
"}"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(_fromUtf8("#frame_4{background:white;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_15 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("color:#1e2bd4"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.frame_3)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setStyleSheet(_fromUtf8("background:#ffffff;"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.frame_8 = QtGui.QFrame(self.frame_3)
        self.frame_8.setStyleSheet(_fromUtf8("#frame_3{\n"
"background:#ffffff;\n"
"border:1px solid #1e2bd4;\n"
"border-radius:7px\n"
"}\n"
"#frame_8{background:white;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}"))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_17 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("color:#1e2bd4"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_8, 2, 0, 1, 1)
        self.tableWidget_3 = QtGui.QTableWidget(self.frame_3)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setStyleSheet(_fromUtf8("background:#ffffff;"))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_3, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 550, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog3)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog3.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        Dialog3.setWindowTitle(QtGui.QApplication.translate("Dialog3", "Analysis result of EVIL TWIN attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog3", "SSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog3", "BSSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog3", "MAC address of EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog3", "Type of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog3", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog3", "Creation date of EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog3", "End date of EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog3", "Start date of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog3", "End date of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog3", "Moment of creating EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog3", "Attack duration (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog3", "Number of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog3", "Transmission channel of legitimate access point", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog3", "Transmission channel of EVIL TWIN ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog3", "Sequence number after start date of deauthentification broadcast", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog3", "EVIL TWIN signature", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog3", "Transmission channel before creating EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog3", "Transmission channel after creating EVIL TWIN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog3", "Imprimer Résultats", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog3 = QtGui.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

