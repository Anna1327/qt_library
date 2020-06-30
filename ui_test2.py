# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(850, 600)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 211, 461))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SQLite = QPushButton(self.layoutWidget)
        self.SQLite.setObjectName(u"SQLite")
        self.SQLite.setIcon(QIcon('img/ph.jpg'))
        self.SQLite.setIconSize(QSize(142, 92))
        self.horizontalLayout.addWidget(self.SQLite)

        self.Add_book = QPushButton(self.layoutWidget)
        self.Add_book.setObjectName(u"Add_book")
        self.Add_book.setIcon(QIcon('img/add.jpg'))
        self.Add_book.setIconSize(QSize(142, 92))
        self.horizontalLayout.addWidget(self.Add_book)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        # загрузить в виде таблицы
        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.horizontalSpacer_4)

        # очистить таблицу
        self.clear_table = QPushButton(parent=None)
        self.clear_table.setObjectName(u"clear_table")

        # удалить таблицу
        self.delete_table = QPushButton(parent=None)
        self.delete_table.setObjectName(u"delete_table")

        self.verticalLayout_5.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(230, 10, 611, 461))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.Upload = QPushButton(self.layoutWidget1)
        self.Upload.setObjectName(u"Upload")
        self.Upload.setIcon(QIcon('img/file_upload.jpg'))
        self.Upload.setIconSize(QSize(92, 92))
        self.horizontalLayout_2.addWidget(self.Upload)

        self.Delete_book = QPushButton(self.layoutWidget1)
        self.Delete_book.setObjectName(u"Delete_book")
        self.Delete_book.setObjectName(u"Delete_book")
        self.Delete_book.setIcon(QIcon('img/del.jpg'))
        self.Delete_book.setIconSize(QSize(142, 92))
        self.horizontalLayout_2.addWidget(self.Delete_book)

        self.Download = QPushButton(self.layoutWidget1)
        self.Download.setObjectName(u"Download")
        self.Download.setIcon(QIcon('img/file_download.jpg'))
        self.Download.setIconSize(QSize(142, 92))
        self.horizontalLayout_2.addWidget(self.Download)

        self.Update_book = QPushButton(self.layoutWidget1)
        self.Update_book.setObjectName(u"Update_book")
        self.Update_book.setIcon(QIcon('img/update.png'))
        self.Update_book.setIconSize(QSize(142, 92))
        self.horizontalLayout_2.addWidget(self.Update_book)

        self.Help = QPushButton(self.layoutWidget1)
        self.Help.setObjectName(u"Help")
        self.Help.setIcon(QIcon('img/help.png'))
        self.Help.setIconSize(QSize(142, 92))
        self.horizontalLayout_2.addWidget(self.Help)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        # текстовое поле
        self.textEdit = QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)

        #здесь моя таблица
        self.tableEdit = QTableWidget(parent=None)
        # self.verticalLayout_3.addWidget(self.tableEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        # self.Enter кнопка Ввод на главном экране
        self.Enter = QPushButton(self.layoutWidget1)
        self.Enter.setObjectName(u"Enter")
        self.Enter.setIconSize(QSize(20, 20))

        self.Cancel = QPushButton(self.layoutWidget1)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.Enter)
        self.verticalLayout_2.addWidget(self.Cancel)

        # self.verticalSpacer вставка для нормального расположения кнопки Ввод
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"My library", None))
        self.SQLite.setText("")
        self.Add_book.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.pushButton_3.setText("Загрузить в виде таблицы")
        self.clear_table.setText("Очистить таблицу")
        self.delete_table.setText("Удалить таблицу")
        self.Upload.setText("")
        self.Delete_book.setText("")
        self.Download.setText("")
        self.Update_book.setText("")
        self.Help.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a:", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.Enter.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u043e\u0434", None))
        self.Cancel.setText("Отмена")
    # retranslateUi

