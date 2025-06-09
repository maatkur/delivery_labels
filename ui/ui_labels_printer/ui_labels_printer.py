# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_labels_printer.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from resources.icons import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QSize(600, 200))
        icon = QIcon()
        icon.addFile(u":/newPrefix/barcode.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(40, 38, 39);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 40))
        self.top_frame.setSizeIncrement(QSize(0, 0))
        self.top_frame.setStyleSheet(u"background-color: rgb(57, 123, 201);")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu = QFrame(self.top_frame)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setMinimumSize(QSize(50, 0))
        self.top_menu.setMaximumSize(QSize(40, 16777215))
        self.top_menu.setStyleSheet(u"background-color: rgb(245, 190, 11);")
        self.top_menu.setFrameShape(QFrame.StyledPanel)
        self.top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.top_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.top_menu)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(25, 25))
        self.menu_button.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon1)
        self.menu_button.setIconSize(QSize(25, 25))
        self.menu_button.setFlat(True)

        self.verticalLayout.addWidget(self.menu_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.top_menu)

        self.frame_4 = QFrame(self.top_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.order_entry = QLineEdit(self.frame_4)
        self.order_entry.setObjectName(u"order_entry")
        self.order_entry.setMinimumSize(QSize(0, 25))
        self.order_entry.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.order_entry.setFont(font)
        self.order_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.order_entry.setInputMethodHints(Qt.ImhNone)
        self.order_entry.setMaxLength(10)
        self.order_entry.setFrame(False)
        self.order_entry.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.order_entry)

        self.search_button = QPushButton(self.frame_4)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setEnabled(False)
        self.search_button.setMinimumSize(QSize(0, 25))
        self.search_button.setMaximumSize(QSize(30, 30))
        self.search_button.setStyleSheet(u"background-color: rgb(57, 123, 201);")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/procurar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon2)
        self.search_button.setIconSize(QSize(25, 25))
        self.search_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.search_button, 0, Qt.AlignTop)

        self.clear_button = QPushButton(self.frame_4)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setEnabled(False)
        self.clear_button.setMinimumSize(QSize(0, 25))
        self.clear_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/apagar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon3)
        self.clear_button.setIconSize(QSize(25, 25))
        self.clear_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.clear_button)

        self.print_button = QPushButton(self.frame_4)
        self.print_button.setObjectName(u"print_button")
        self.print_button.setEnabled(False)
        self.print_button.setMinimumSize(QSize(0, 25))
        self.print_button.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/imprimir.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.print_button.setIcon(icon4)
        self.print_button.setIconSize(QSize(25, 25))
        self.print_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.print_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(25, 25))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_6.setFont(font1)
        self.label_6.setPixmap(QPixmap(u":/newPrefix/avatar.ico"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.logged_user_label = QLabel(self.frame_4)
        self.logged_user_label.setObjectName(u"logged_user_label")
        font2 = QFont()
        font2.setBold(True)
        self.logged_user_label.setFont(font2)
        self.logged_user_label.setStyleSheet(u"font-size: 13px;")

        self.horizontalLayout_3.addWidget(self.logged_user_label)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.left_menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.drawer = QFrame(self.left_menu)
        self.drawer.setObjectName(u"drawer")
        self.drawer.setMinimumSize(QSize(0, 0))
        self.drawer.setMaximumSize(QSize(0, 16777215))
        self.drawer.setStyleSheet(u"background-color: rgb(228, 60, 47);")
        self.drawer.setFrameShape(QFrame.StyledPanel)
        self.drawer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.drawer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.users_menu_button = QPushButton(self.drawer)
        self.users_menu_button.setObjectName(u"users_menu_button")
        self.users_menu_button.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/usuarios.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.users_menu_button.setIcon(icon5)
        self.users_menu_button.setIconSize(QSize(25, 25))
        self.users_menu_button.setFlat(True)

        self.verticalLayout_4.addWidget(self.users_menu_button, 0, Qt.AlignHCenter)

        self.reports_button = QPushButton(self.drawer)
        self.reports_button.setObjectName(u"reports_button")
        self.reports_button.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/numero-de-rastreio.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_button.setIcon(icon6)
        self.reports_button.setIconSize(QSize(25, 25))
        self.reports_button.setFlat(True)

        self.verticalLayout_4.addWidget(self.reports_button, 0, Qt.AlignHCenter)

        self.change_password_button = QPushButton(self.drawer)
        self.change_password_button.setObjectName(u"change_password_button")
        self.change_password_button.setMaximumSize(QSize(30, 30))
        self.change_password_button.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/reset-password.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.change_password_button.setIcon(icon7)
        self.change_password_button.setIconSize(QSize(25, 25))
        self.change_password_button.setFlat(True)

        self.verticalLayout_4.addWidget(self.change_password_button, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.drawer)

        self.frame_3 = QFrame(self.left_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(40, 38, 39);\n"
"color: white;\n"
"\n"
"\n"
"QLineEdit {\n"
"border: 1px solid rgb( 245, 190, 11);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 27))
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label)

        self.customer_field = QLineEdit(self.frame_2)
        self.customer_field.setObjectName(u"customer_field")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_field.sizePolicy().hasHeightForWidth())
        self.customer_field.setSizePolicy(sizePolicy)
        self.customer_field.setMinimumSize(QSize(0, 25))
        self.customer_field.setMaximumSize(QSize(16777215, 23))
        self.customer_field.setFont(font2)
        self.customer_field.setStyleSheet(u"background-color: rgb( 228, 60, 47);\n"
"border: 2px solid rgb( 228, 60, 47);\n"
"border-radius: 10px;\n"
"font-size: 13px;")
        self.customer_field.setReadOnly(True)
        self.customer_field.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.customer_field)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb( 57, 123, 201);\n"
"border: 2px solid rgb( 57, 123, 201);\n"
"border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 27))
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.service_store_field = QLineEdit(self.frame_5)
        self.service_store_field.setObjectName(u"service_store_field")
        self.service_store_field.setMinimumSize(QSize(0, 25))
        self.service_store_field.setFont(font2)
        self.service_store_field.setStyleSheet(u"font-size: 13px;")
        self.service_store_field.setReadOnly(True)
        self.service_store_field.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.service_store_field)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 27))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font-size: 13px;")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_date_field = QLineEdit(self.frame_5)
        self.label_date_field.setObjectName(u"label_date_field")
        self.label_date_field.setMinimumSize(QSize(0, 25))
        self.label_date_field.setFont(font2)
        self.label_date_field.setStyleSheet(u"font-size: 13px;")
        self.label_date_field.setAlignment(Qt.AlignCenter)
        self.label_date_field.setReadOnly(True)
        self.label_date_field.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.label_date_field)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb( 245, 190, 11);\n"
"border: 2px solid rgb( 245, 190, 11);\n"
"border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 27))
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.checker_field = QLineEdit(self.frame_6)
        self.checker_field.setObjectName(u"checker_field")
        self.checker_field.setMinimumSize(QSize(0, 25))
        self.checker_field.setMaximumSize(QSize(50, 50))
        self.checker_field.setFont(font2)
        self.checker_field.setStyleSheet(u"font-size: 13px;\n"
"color: black;")
        self.checker_field.setAlignment(Qt.AlignCenter)
        self.checker_field.setReadOnly(True)
        self.checker_field.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.checker_field)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 27))
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.decrement_button = QPushButton(self.frame_6)
        self.decrement_button.setObjectName(u"decrement_button")
        self.decrement_button.setMinimumSize(QSize(0, 25))
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/subtrair.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.decrement_button.setIcon(icon8)
        self.decrement_button.setIconSize(QSize(25, 25))
        self.decrement_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.decrement_button)

        self.label_quantity_display = QLineEdit(self.frame_6)
        self.label_quantity_display.setObjectName(u"label_quantity_display")
        self.label_quantity_display.setMinimumSize(QSize(0, 25))
        self.label_quantity_display.setMaximumSize(QSize(50, 50))
        self.label_quantity_display.setFont(font2)
        self.label_quantity_display.setStyleSheet(u"font-size: 13px;\n"
"color: black;")
        self.label_quantity_display.setMaxLength(32767)
        self.label_quantity_display.setAlignment(Qt.AlignCenter)
        self.label_quantity_display.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.label_quantity_display)

        self.increment_button = QPushButton(self.frame_6)
        self.increment_button.setObjectName(u"increment_button")
        self.increment_button.setMinimumSize(QSize(0, 25))
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/adicionar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.increment_button.setIcon(icon9)
        self.increment_button.setIconSize(QSize(25, 25))
        self.increment_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.increment_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.reprint_frame = QFrame(self.frame_3)
        self.reprint_frame.setObjectName(u"reprint_frame")
        self.reprint_frame.setMinimumSize(QSize(0, 0))
        self.reprint_frame.setMaximumSize(QSize(16777215, 0))
        self.reprint_frame.setFrameShape(QFrame.StyledPanel)
        self.reprint_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.reprint_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.reprint_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 27))
        self.label_7.setMaximumSize(QSize(100, 16777215))
        self.label_7.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.reasons_combo_box = QComboBox(self.reprint_frame)
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.addItem("")
        self.reasons_combo_box.setObjectName(u"reasons_combo_box")
        self.reasons_combo_box.setMinimumSize(QSize(211, 0))
        self.reasons_combo_box.setMaximumSize(QSize(20, 16777215))
        self.reasons_combo_box.setStyleSheet(u"background-color: rgb( 57, 123, 201);\n"
"border: 2px solid rgb( 57, 123, 201);\n"
"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.reasons_combo_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(self.reprint_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 27))
        self.label_8.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.complement_id_combo_box = QComboBox(self.reprint_frame)
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.addItem("")
        self.complement_id_combo_box.setObjectName(u"complement_id_combo_box")
        self.complement_id_combo_box.setEnabled(False)
        self.complement_id_combo_box.setMinimumSize(QSize(100, 0))
        self.complement_id_combo_box.setMaximumSize(QSize(50, 16777215))
        self.complement_id_combo_box.setStyleSheet(u"background-color: rgb( 57, 123, 201);\n"
"border: 2px solid rgb( 57, 123, 201);\n"
"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.complement_id_combo_box)

        self.interval_entry = QLineEdit(self.reprint_frame)
        self.interval_entry.setObjectName(u"interval_entry")
        self.interval_entry.setEnabled(False)
        self.interval_entry.setStyleSheet(u"background-color: rgb( 57, 123, 201);\n"
"border: 2px solid rgb( 57, 123, 201);\n"
"border-radius: 10px;")
        self.interval_entry.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.interval_entry)


        self.verticalLayout_3.addWidget(self.reprint_frame)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 20))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.quantity_label = QLabel(self.frame_7)
        self.quantity_label.setObjectName(u"quantity_label")
        self.quantity_label.setMaximumSize(QSize(16777215, 20))
        self.quantity_label.setFont(font)
        self.quantity_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.quantity_label)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.left_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etiquetas | Impress\u00e3o", None))
        self.menu_button.setText("")
        self.order_entry.setInputMask(QCoreApplication.translate("MainWindow", u"9999999999", None))
        self.order_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PEDIDO", None))
        self.search_button.setText("")
        self.clear_button.setText("")
        self.print_button.setText("")
        self.label_6.setText("")
        self.logged_user_label.setText(QCoreApplication.translate("MainWindow", u"15 - EZEQUIEL", None))
        self.users_menu_button.setText("")
        self.reports_button.setText("")
        self.change_password_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CLIENTE:", None))
        self.customer_field.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ATENDIMENTO:", None))
        self.service_store_field.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EMISS\u00c3O DA ETIQUETA:", None))
        self.label_date_field.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SEPARADOR:", None))
        self.checker_field.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VOLUMES:", None))
        self.decrement_button.setText("")
#if QT_CONFIG(shortcut)
        self.decrement_button.setShortcut(QCoreApplication.translate("MainWindow", u"_, -", None))
#endif // QT_CONFIG(shortcut)
        self.label_quantity_display.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.increment_button.setText("")
#if QT_CONFIG(shortcut)
        self.increment_button.setShortcut(QCoreApplication.translate("MainWindow", u"+, =", None))
#endif // QT_CONFIG(shortcut)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MOTIVO:", None))
        self.reasons_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.reasons_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Pedido complementar/parcial", None))
        self.reasons_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Falha na impressora", None))
        self.reasons_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Impressora sem etiqueta", None))
        self.reasons_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Impressora sem tinta (Ribbon)", None))
        self.reasons_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"N\u00famero de volumes incorreto", None))
        self.reasons_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Etiqueta perdida", None))
        self.reasons_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Etiqueta danificada", None))
        self.reasons_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"Impresso anteriormente por engano", None))
        self.reasons_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"Pedido anteriormente cancelado", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"COMPL:", None))
        self.complement_id_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.complement_id_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.complement_id_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.complement_id_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.complement_id_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.complement_id_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.complement_id_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.complement_id_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.complement_id_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.complement_id_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.complement_id_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))

        self.interval_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.quantity_label.setText(QCoreApplication.translate("MainWindow", u"VOLUME \u00daNICO", None))
    # retranslateUi

