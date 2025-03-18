# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_users_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from resources.icons import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 389)
        MainWindow.setMaximumSize(QSize(402, 389))
        icon = QIcon()
        icon.addFile(u":/newPrefix/barcode.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 16777215))
        self.top_frame.setStyleSheet(u"background-color: rgb(40, 38, 39);\n"
"color: white;\n"
"")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.top_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.top_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(57, 123, 201);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 4, 0, 4)
        self.horizontalSpacer = QSpacerItem(116, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.user_code_entry = QLineEdit(self.frame)
        self.user_code_entry.setObjectName(u"user_code_entry")
        self.user_code_entry.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.user_code_entry.setFont(font)
        self.user_code_entry.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"color: black;")
        self.user_code_entry.setMaxLength(3)
        self.user_code_entry.setAlignment(Qt.AlignCenter)
        self.user_code_entry.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout.addWidget(self.user_code_entry)

        self.search_button = QPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/procurar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QSize(25, 25))
        self.search_button.setFlat(True)

        self.horizontalLayout.addWidget(self.search_button)

        self.clear_button = QPushButton(self.frame)
        self.clear_button.setObjectName(u"clear_button")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/apagar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon2)
        self.clear_button.setIconSize(QSize(25, 25))
        self.clear_button.setFlat(True)

        self.horizontalLayout.addWidget(self.clear_button)

        self.add_user_button = QPushButton(self.frame)
        self.add_user_button.setObjectName(u"add_user_button")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/add_user", QSize(), QIcon.Normal, QIcon.Off)
        self.add_user_button.setIcon(icon3)
        self.add_user_button.setIconSize(QSize(25, 25))
        self.add_user_button.setFlat(True)

        self.horizontalLayout.addWidget(self.add_user_button)

        self.horizontalSpacer_2 = QSpacerItem(116, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.top_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 4)
        self.horizontalSpacer_3 = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.id_input = QLineEdit(self.frame_3)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setMaximumSize(QSize(16777215, 16777215))
        self.id_input.setLayoutDirection(Qt.LeftToRight)
        self.id_input.setStyleSheet(u"background-color: white;\n"
"border-radius: 4px;\n"
"color: black;")
        self.id_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.id_input)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.name_input = QLineEdit(self.frame_3)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setStyleSheet(u"background-color: white;\n"
"border-radius: 4px;\n"
"color: black;")
        self.name_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.name_input)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.password_input = QLineEdit(self.frame_3)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setStyleSheet(u"background-color: white;\n"
"border-radius: 4px;\n"
"color: black;")
        self.password_input.setMaxLength(6)
        self.password_input.setFrame(True)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.password_input)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.horizontalSpacer_4 = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.top_frame)

        self.table_frame = QFrame(self.centralwidget)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setStyleSheet(u"background-color: rgb(57, 123, 201);\n"
"color: white;")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.table_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.table_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb( 245, 190, 11);\n"
"color: black;")
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.table_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etiquetas | Gerenciamento de permiss\u00f5es", None))
        self.user_code_entry.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.user_code_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3d.", None))
        self.search_button.setText("")
        self.clear_button.setText("")
        self.add_user_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.id_input.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.password_input.setInputMask("")
        self.password_input.setPlaceholderText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Reimpress\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Users", None));
    # retranslateUi

