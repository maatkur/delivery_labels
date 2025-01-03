# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from resources.icons import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(182, 210)
        icon = QIcon()
        icon.addFile(u":/newPrefix/barcode.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(40, 38, 39);\n"
"QLineEdit {\n"
"    background-color: white;\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.current_password_input = QLineEdit(self.main_frame)
        self.current_password_input.setObjectName(u"current_password_input")
        self.current_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.current_password_input.setEchoMode(QLineEdit.Password)
        self.current_password_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.current_password_input)

        self.label_2 = QLabel(self.main_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.new_password_input = QLineEdit(self.main_frame)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.new_password_input.setEchoMode(QLineEdit.Password)
        self.new_password_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.new_password_input)

        self.label_3 = QLabel(self.main_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.password_confirmation_input = QLineEdit(self.main_frame)
        self.password_confirmation_input.setObjectName(u"password_confirmation_input")
        self.password_confirmation_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.password_confirmation_input.setEchoMode(QLineEdit.Password)
        self.password_confirmation_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.password_confirmation_input)

        self.echo_mode_button = QPushButton(self.main_frame)
        self.echo_mode_button.setObjectName(u"echo_mode_button")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/show.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.echo_mode_button.setIcon(icon1)
        self.echo_mode_button.setFlat(True)

        self.verticalLayout_2.addWidget(self.echo_mode_button)

        self.bot_frame = QFrame(self.main_frame)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bot_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_button = QPushButton(self.bot_frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setEnabled(False)
        self.save_button.setMinimumSize(QSize(100, 20))
        self.save_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.save_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.bot_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etiquetas | Troca de senha", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Senha atual:", None))
        self.current_password_input.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nova senha:", None))
        self.new_password_input.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirmar:", None))
        self.password_confirmation_input.setInputMask("")
        self.echo_mode_button.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

