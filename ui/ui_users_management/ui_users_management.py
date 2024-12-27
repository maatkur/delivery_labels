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
    QHeaderView, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from resources.icons import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 389)
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
        self.top_frame.setMaximumSize(QSize(16777215, 50))
        self.top_frame.setStyleSheet(u"background-color: rgb(57, 123, 201);\n"
"color: white;\n"
"")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.user_code_entry = QLineEdit(self.top_frame)
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

        self.search_button = QPushButton(self.top_frame)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/procurar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QSize(25, 25))
        self.search_button.setFlat(True)

        self.horizontalLayout.addWidget(self.search_button)

        self.clear_button = QPushButton(self.top_frame)
        self.clear_button.setObjectName(u"clear_button")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/apagar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon2)
        self.clear_button.setIconSize(QSize(25, 25))
        self.clear_button.setFlat(True)

        self.horizontalLayout.addWidget(self.clear_button)

        self.add_user_button = QPushButton(self.top_frame)
        self.add_user_button.setObjectName(u"add_user_button")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/add_user", QSize(), QIcon.Normal, QIcon.Off)
        self.add_user_button.setIcon(icon3)
        self.add_user_button.setIconSize(QSize(25, 25))
        self.add_user_button.setFlat(True)

        self.horizontalLayout.addWidget(self.add_user_button)

        self.horizontalSpacer_2 = QSpacerItem(123, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.top_frame)

        self.table_frame = QFrame(self.centralwidget)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setStyleSheet(u"background-color: rgb(40, 38, 39);\n"
"color: white;")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.table_frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb( 245, 190, 11);\n"
"color: black;")
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.tableWidget)


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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Reimpress\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios", None));
    # retranslateUi

