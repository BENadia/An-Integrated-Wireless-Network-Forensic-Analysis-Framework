# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultatDoS.ui'
#
# Created: Sun Jun 15 19:10:48 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(1084, 573)
        Dialog2.setStyleSheet(_fromUtf8("#Dialog2{\n"
"border:2px solid #1e2bd4;\n"
"border-radius: 1 px;\n"
"background: white;\n"
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
"}"))
        Dialog2.setModal(True)
        self.top_frame = QtGui.QFrame(Dialog2)
        self.top_frame.setGeometry(QtCore.QRect(9, 9, 1046, 51))
        self.top_frame.setStyleSheet(_fromUtf8("#top_frame{\n"
"background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.top_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.top_frame.setObjectName(_fromUtf8("top_frame"))
        self.gridLayout = QtGui.QGridLayout(self.top_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.top_frame)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.top_frame)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.top_frame)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 0, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:white"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.top_frame)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout.addWidget(self.lineEdit_12, 0, 7, 1, 1)
        self.bottom_frame = QtGui.QFrame(Dialog2)
        self.bottom_frame.setGeometry(QtCore.QRect(110, 70, 781, 436))
        self.bottom_frame.setStyleSheet(_fromUtf8("#bottom_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.bottom_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottom_frame.setObjectName(_fromUtf8("bottom_frame"))
        self.label_6 = QtGui.QLabel(self.bottom_frame)
        self.label_6.setGeometry(QtCore.QRect(11, 11, 371, 21))
        self.label_6.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 10, 251, 29))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_8 = QtGui.QLabel(self.bottom_frame)
        self.label_8.setGeometry(QtCore.QRect(11, 46, 324, 21))
        self.label_8.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_5 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 46, 251, 29))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_10 = QtGui.QLabel(self.bottom_frame)
        self.label_10.setGeometry(QtCore.QRect(11, 81, 392, 21))
        self.label_10.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_6 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(490, 81, 251, 29))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_7 = QtGui.QLabel(self.bottom_frame)
        self.label_7.setGeometry(QtCore.QRect(11, 116, 374, 21))
        self.label_7.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(490, 116, 251, 29))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_11 = QtGui.QLabel(self.bottom_frame)
        self.label_11.setGeometry(QtCore.QRect(11, 151, 461, 21))
        self.label_11.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_7 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(630, 150, 111, 29))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_13 = QtGui.QLabel(self.bottom_frame)
        self.label_13.setGeometry(QtCore.QRect(11, 186, 198, 21))
        self.label_13.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_13 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(630, 186, 111, 29))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_5 = QtGui.QLabel(self.bottom_frame)
        self.label_5.setGeometry(QtCore.QRect(11, 221, 410, 21))
        self.label_5.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_14 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(630, 221, 111, 29))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_9 = QtGui.QLabel(self.bottom_frame)
        self.label_9.setGeometry(QtCore.QRect(11, 256, 518, 21))
        self.label_9.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_9 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(630, 256, 111, 29))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_16 = QtGui.QLabel(self.bottom_frame)
        self.label_16.setGeometry(QtCore.QRect(11, 291, 511, 21))
        self.label_16.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_10 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(630, 291, 111, 29))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_15 = QtGui.QLabel(self.bottom_frame)
        self.label_15.setGeometry(QtCore.QRect(11, 326, 501, 21))
        self.label_15.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_15 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(630, 326, 111, 29))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.label_12 = QtGui.QLabel(self.bottom_frame)
        self.label_12.setGeometry(QtCore.QRect(11, 361, 494, 21))
        self.label_12.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_16 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(630, 361, 111, 29))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_14 = QtGui.QLabel(self.bottom_frame)
        self.label_14.setGeometry(QtCore.QRect(11, 396, 463, 21))
        self.label_14.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_11 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(630, 396, 111, 29))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.pushButton = QtGui.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(330, 510, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 510, 105, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog2)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog2.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QtGui.QApplication.translate("Dialog2", "Analysis result of DoS attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog2", "SSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog2", "BSSID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog2", "MAC address of suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog2", "Type of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog2", "Start date of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog2", "End date of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog2", "Start date of sending NULL subtype of data frames", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog2", "End date of sending NULL subtype of data frames ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog2", "WAP\'s broadcast duration by  NULL subtype of data frames (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog2", "Attack duration (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog2", "Number of WAP\'s  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog2", "Number of NULL subtype of data frames sending by all stations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog2", "Number of NULL subtype of data frames before  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog2", "Number of NULL subtype of data frames during  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog2", "Number of NULL subtype of data frames after  broadcast deauthentification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog2", "Number of NULL subtype of data frames sending by suspect", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog2", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog2", "Print", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

