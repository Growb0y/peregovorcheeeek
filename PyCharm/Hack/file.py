# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(925, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QSlider {\n"
"margin-left: 9px;\n"
"margin-right: 9px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"background: rgba(0, 0, 0, 0);\n"
"height: 10px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 1, y2: 1,\n"
"    stop: 0 #ffffff, stop: 1 #ff6b61);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"margin-left: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(217, 217, 217);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"margin-right: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 255), stop:0.3 rgba(255, 151, 151, 255), stop:0.4 rgba(255, 125, 125, 255), stop:0.5 rgba(255, 0, 4, 220), stop:0.54 rgba(255, 0, 4, 255), stop:0.6 rgba(255, 180, 180, 84), stop:0.95 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"border: 1px solid #fff;\n"
"width: 26px;\n"
"margin-top: -8px;\n"
"margin-bottom: -8px;\n"
"\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"border: 1px solid rgb(223, 223, 223);\n"
"}\n"
"\n"
"QGroupBox, QScrollArea, QPlainTextEdit {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 255, 255, 100),\n"
"stop:1 rgba(255, 255, 255, 30) );\n"
"border-radius: 10px;\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 255, 255, 255),\n"
"stop:1 rgba(255, 255, 255, 30) );\n"
"}\n"
"\n"
"QScrollArea QWidget QGroupBox {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 50),\n"
"stop:1 rgba(255, 94, 97, 5) );\n"
"border-radius: 10px;\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 150),\n"
"stop:1 rgba(255, 94, 97, 10) );\n"
"}\n"
"\n"
"QScrollArea QWidget QGroupBox QPlainTextEdit {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 100),\n"
"stop:1 rgba(255, 94, 97, 10) );\n"
"border-radius: 10px;\n"
"border: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 255),\n"
"stop:1 rgba(255, 94, 97, 30) );\n"
"}\n"
"\n"
"QScrollArea QWidget QGroupBox QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"stop:0 rgba(255, 62, 65, 255),\n"
"stop:1 rgba(255, 255, 255, 255) );\n"
"    border:3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 255),\n"
"stop:1 rgba(255, 94, 97, 30) );\n"
"}\n"
"\n"
"#groupBox_file {\n"
"border-radius: 36px;\n"
"}\n"
"#groupBox_export {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"font-family: Helvetica;\n"
"font-size: 14px;\n"
"font-weight: bold, italic;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    background: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0, y2:0,\n"
"stop:0 rgba(255, 62, 65, 200),\n"
"stop:1 rgba(255, 255, 255, 100) );\n"
"    border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(255, 180, 181, 255),\n"
"stop:1 rgba(255, 94, 97, 30) );\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0, y2:0,\n"
"stop:0 rgba(255, 62, 65, 150),\n"
"stop:1 rgba(255, 255, 255, 50) );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-width: 4px;\n"
"}\n"
"\n"
"#pushButton_play {\n"
"padding-left: 8px;\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"stop: 0 #ff0000,\n"
"stop: 0.7 #ff9092,\n"
"stop: 1 rgba(255, 255, 255, 0) );\n"
"border: none;\n"
"}\n"
"\n"
"#pushButton_play:hover {\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"stop: 0 #ff0000,\n"
"stop: 0.7 #ff9092,\n"
"stop: 1 rgba(255, 255, 255, 50) );\n"
"}\n"
"\n"
"#pushButton_play:pressed {\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"stop: 0 #ff0000,\n"
"stop: 0.5 #ff9092,\n"
"stop: 1 rgba(255, 255, 255, 0) );\n"
"}\n"
"\n"
"QMainWindow {\n"
"background: QLinearGradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 1 #ff797b,\n"
"stop: 0.8 #f0f0f0,\n"
"stop: 0.25 #f0f0f0,\n"
"stop: 0 #ff797b );\n"
"width: 30px;\n"
"}\n"
"\n"
"QScrollArea QWidget {\n"
"background: rgba(255, 255, 255, 100)\n"
"}\n"
"\n"
"QScrollArea QScrollBar {\n"
"background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 1 #ff2023,\n"
"stop: 0.5 #ffffff,\n"
"stop: 0 #ff393c );\n"
"width: 25px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(220, 220, 220);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 1 #ff2023,\n"
"stop: 0.5 #ffffff,\n"
"stop: 0 #ff393c );\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 1 #ff2023,\n"
"stop: 0.5 #ffffff,\n"
"stop: 0 #ff393c );\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 1 #ff2023,\n"
"stop: 0.5 #ffffff,\n"
"stop: 0 #ff393c );;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #ff051e,\n"
"stop: 0.5 #ffffff,\n"
"stop: 1 #ff585b );\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"")
        Form.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_export = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_export.setTitle("")
        self.groupBox_export.setObjectName("groupBox_export")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_export)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_export)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_export)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_export)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.gridLayout.addWidget(self.groupBox_export, 2, 0, 1, 1)
        self.groupBox_file = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_file.setStyleSheet("")
        self.groupBox_file.setTitle("")
        self.groupBox_file.setObjectName("groupBox_file")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_file)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox_file)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy)
        self.pushButton_play.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_play.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_play.setStyleSheet("QPushButton {\n"
"border-radius: 25px;\n"
"}")
        self.pushButton_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_6.addWidget(self.pushButton_play)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_file)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(999)
        self.horizontalSlider.setPageStep(50)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_6.addWidget(self.horizontalSlider)
        self.gridLayout.addWidget(self.groupBox_file, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 352, 201))
        scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        verticalLayout_2 = QtWidgets.QFormLayout(scrollAreaWidgetContents_2)
        verticalLayout_2.setObjectName("verticalLayout_2")

        violationTime = []
        violationText = []

        def addViolation():
                groupBox_violation = QtWidgets.QGroupBox(scrollAreaWidgetContents_2)
                groupBox_violation.setTitle("")
                groupBox_violation.setObjectName("groupBox_violation" + str(len(violationTime)))
                horizontalLayout = QtWidgets.QHBoxLayout(groupBox_violation)
                verticalLayout = QtWidgets.QVBoxLayout()
                verticalLayout.setSpacing(0)
                pushButton_violationTime = QtWidgets.QPushButton(groupBox_violation)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(pushButton_violationTime.sizePolicy().hasHeightForWidth())
                pushButton_violationTime.setSizePolicy(sizePolicy)
                pushButton_violationTime.setMinimumSize(QtCore.QSize(52, 0))
                pushButton_violationTime.setStyleSheet("")
                pushButton_violationTime.setObjectName("pushButton_violation" + str(len(violationTime)))
                verticalLayout.addWidget(pushButton_violationTime)
                spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
                verticalLayout.addItem(spacerItem1)
                horizontalLayout.addLayout(verticalLayout)
                plainTextEdit_violationText = QtWidgets.QPlainTextEdit(groupBox_violation)
                plainTextEdit_violationText.setObjectName("plainTextEdit_violation" + str(len(violationText)))
                horizontalLayout.addWidget(plainTextEdit_violationText)

                violationTime.append(pushButton_violationTime.text())
                violationText.append(plainTextEdit_violationText.toPlainText())

                verticalLayout_2.addRow(groupBox_violation)

        addViolation()
        addViolation()
        addViolation()
        addViolation()

        self.scrollArea_2.setWidget(scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Проверка файла"))
        self.pushButton_5.setText(_translate("Form", "Word"))
        self.pushButton_3.setText(_translate("Form", "Excel"))
        self.pushButton_4.setText(_translate("Form", "Отправить"))


def create_form(): ###
    form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()