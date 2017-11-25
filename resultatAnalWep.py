# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultatAnalWep.ui'
#
# Created: Sun Jun 15 19:10:34 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName(_fromUtf8("Dialog1"))
        Dialog1.resize(1180, 748)
        Dialog1.setStyleSheet(_fromUtf8("#Dialog1{\n"
"background:white;\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"}\n"
"#frame_3{\n"
"border:#8bf;\n"
"}\n"
"#frame_2{\n"
"border:#8bf;\n"
"}\n"
"#frame_5{\n"
"border:#8bf;\n"
"}\n"
"\n"
"#frame{\n"
"border:#8bf;\n"
"}\n"
"#top_frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4fe;\n"
"}\n"
"#bottom_frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4fe;\n"
"}\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid #1e2bd4;\n"
"border-radius: 8px;\n"
"}\n"
"QComboBox{\n"
"\n"
"border-style: solid;\n"
"border: 2px solid #1e2bd4;\n"
"\n"
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
"QTableWidget{\n"
"background:#d0e4fe;\n"
"border-color:#1e2bd4;\n"
"border-width: 2px ;\n"
"border-style: solid ;\n"
"border-radius: 10;\n"
"padding:4px;\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"}\n"
"#frame_6{\n"
"background:#8bf;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}\n"
"#frame_7{\n"
"background:#8bf;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}\n"
"#frame_8{\n"
"background:#8bf;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}"))
        self.top_frame = QtGui.QFrame(Dialog1)
        self.top_frame.setGeometry(QtCore.QRect(-1, 3, 1181, 51))
        self.top_frame.setStyleSheet(_fromUtf8("background-color:#ffffff"))
        self.top_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.top_frame.setObjectName(_fromUtf8("top_frame"))
        self.gridLayout = QtGui.QGridLayout(self.top_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_17 = QtGui.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.bottom_frame = QtGui.QFrame(Dialog1)
        self.bottom_frame.setGeometry(QtCore.QRect(10, 60, 1161, 671))
        self.bottom_frame.setStyleSheet(_fromUtf8("#bottom_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.bottom_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottom_frame.setObjectName(_fromUtf8("bottom_frame"))
        self.frame = QtGui.QFrame(self.bottom_frame)
        self.frame.setGeometry(QtCore.QRect(10, 50, 511, 292))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_15 = QtGui.QLabel(self.frame)
        self.label_15.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.frame)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 1, 1, 2)
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.frame)
        self.lineEdit_13.setEnabled(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_2.addWidget(self.lineEdit_13, 1, 1, 1, 2)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.frame)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_2.addWidget(self.lineEdit_14, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 2)
        self.lineEdit_7 = QtGui.QLineEdit(self.frame)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 2)
        self.lineEdit_6 = QtGui.QLineEdit(self.frame)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame)
        self.label_13.setStyleSheet(_fromUtf8("color:#ffffff"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.frame)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout_2.addWidget(self.lineEdit_10, 5, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.frame)
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout_2.addWidget(self.lineEdit_11, 6, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 7, 0, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.frame)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout_2.addWidget(self.lineEdit_12, 7, 2, 1, 1)
        self.frame_2 = QtGui.QFrame(self.bottom_frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 0, 1101, 49))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_18 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 4, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 5, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 6, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_3.addWidget(self.lineEdit_8, 0, 7, 1, 1)
        self.frame_3 = QtGui.QFrame(self.bottom_frame)
        self.frame_3.setGeometry(QtCore.QRect(530, 59, 571, 259))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tableWidget_4 = QtGui.QTableWidget(self.frame_3)
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget_4, 2, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setStyleSheet(_fromUtf8("#frame_4{background:white;\n"
"border:2px solid #1e2bd4;\n"
"border-radius:7px\n"
"}"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_4 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtGui.QFrame(self.bottom_frame)
        self.frame_5.setGeometry(QtCore.QRect(10, 360, 1131, 211))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(28, 9, 381, 43))
        self.frame_6.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_3 = QtGui.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.frame_7 = QtGui.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(460, 9, 301, 43))
        self.frame_7.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_2 = QtGui.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame_8 = QtGui.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(830, 9, 251, 43))
        self.frame_8.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget_3 = QtGui.QTableWidget(self.frame_5)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(9, 58, 421, 144))
        self.tableWidget_3.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_2 = QtGui.QTableWidget(self.frame_5)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(440, 60, 341, 144))
        self.tableWidget_2.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget = QtGui.QTableWidget(self.frame_5)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(790, 60, 331, 144))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_9 = QtGui.QFrame(self.bottom_frame)
        self.frame_9.setGeometry(QtCore.QRect(390, 570, 271, 48))
        self.frame_9.setStyleSheet(_fromUtf8("#frame_9{\n"
"border:#8bf;\n"
"}"))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_9)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.frame_9)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 105, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(105, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog1)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog1.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(QtGui.QApplication.translate("Dialog1", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog1", "                                                                                 Analysis result of WEP cracking attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog1", "Start date of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog1", "End date of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog1", "Attack duration (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog1", "Deauthentification frames sent to suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog1", "broadcast data frames by suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog1", "Initialization vector before attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog1", "Initialization vector during attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog1", "Initialization vector after attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog1", "SSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog1", "BSSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog1", "MAC address of suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog1", "Type of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog1", "                                                 Timeline of suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog1", "Source and destinations of data frames", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog1", "Number of data frames", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog1", "Associated stations", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog1", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog1", "Print", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog1 = QtGui.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

