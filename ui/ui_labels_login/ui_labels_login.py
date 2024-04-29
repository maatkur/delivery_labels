# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_labels_login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from resources.icons import icons
from helpers.path_helper import PathHelper

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 353)
        icon = QIcon()
        icon.addFile(u":/newPrefix/barcode.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(f"{PathHelper.resolve()}resources/img/black_and_white_logo_only.png"))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(116, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(116, 35, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(122, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(122, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(113, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.user_entry = QLineEdit(self.frame_4)
        self.user_entry.setObjectName(u"user_entry")
        self.user_entry.setGeometry(QRect(0, 10, 113, 21))
        font = QFont()
        font.setBold(True)
        self.user_entry.setFont(font)
        self.user_entry.setStyleSheet(u"QLineEdit {\n"
"color: #ffffff;\n"
"}")
        self.user_entry.setInputMethodHints(Qt.ImhNone)
        self.user_entry.setMaxLength(3)
        self.user_entry.setAlignment(Qt.AlignCenter)
        self.password_entry = QLineEdit(self.frame_4)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setGeometry(QRect(0, 40, 113, 21))
        self.password_entry.setFont(font)
        self.password_entry.setStyleSheet(u"QLineEdit {\n"
"color: #ffffff;\n"
"}")
        self.password_entry.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_entry.setMaxLength(10)
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 2)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 38))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.login_button = QPushButton(self.frame_5)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(20, 3, 75, 24))
        self.login_button.setFont(font)
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	color: rbg(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb( 115,115, 115);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 15))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 71, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #ffffff;")

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.password_entry.returnPressed.connect(self.login_button.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etiquetas | Login", None))
        self.label.setText("")
        self.user_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.password_entry.setText("")
        self.password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9MKOTECH", None))
    # retranslateUi

