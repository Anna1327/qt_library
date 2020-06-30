# -*- coding: utf-8 -*-

import sys
import os
import sqlite3
import ui_test2
import qt_data_base
import PySide2
from pathlib import Path
from PyQt5 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (QMainWindow, QFileDialog,  QTableWidgetItem, QLabel)
import json
import pandas as pd


class Mistakes(PySide2.QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Mistakes, self).__init__(parent)
        self.parent = parent
        self.mistake_db_file()

    def mistake_db_file(self):
        message = QtWidgets.QLabel(self)
        message.setText('Файл должен быть с расширением db')
        mvbox = QtWidgets.QVBoxLayout()
        mvbox.addWidget(message)


class MyWindow(PySide2.QtWidgets.QWidget, ui_test2.Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.SQLite.clicked.connect(self.btn_win)
        self.Upload.clicked.connect(self.openfile)
        self.clear_table.clicked.connect(self.clear_data_from_table)
        self.delete_table.clicked.connect(self.del_table)
        self.Add_book.clicked.connect(self.btn_clk)
        self.Delete_book.clicked.connect(self.btn_del)
        self.Update_book.clicked.connect(self.btn_up)
        self.Enter.clicked.connect(self.choice_of_main_param)
        self.Cancel.clicked.connect(self.cancel)
        self.Help.clicked.connect(self.btn_help)
        self.Download.clicked.connect(self.btn_download)

        self.open_name, self.suffix = '', ''
        self.data_base = ''
        self.new_data_base = ''
        self.new_data = []
        self.counter = 0
        self.import_lst = []
        self.table = self.listWidget
        self.data = []
        self.result = []
        self.output_on_display = []
        self.view = 'text'
        self.column_names = []
        self.failed_load_txt_file = ''
        self.add = AddBook()
        self.delete = DelBook()
        self.update = UpdateBook()
        self.helper = Help()
        self.creation = CreateNewDB()
        self.download = Download()

    def btn_clk(self):
        if len(window.data) == 0:
            print('Сначала загрузите таблицу!')
        else:
            self.add = AddBook()
            self.add.build_widgets()
            self.add.show()

    def btn_del(self):
        if len(window.data) == 0:
            print('Сначала загрузите таблицу!')
        else:
            self.delete = DelBook()
            self.delete.build_widgets()
            self.delete.show()

    def btn_up(self):
        if len(window.data) == 0:
            print('Сначала загрузите таблицу!')
        else:
            self.update = UpdateBook()
            self.update.build_widgets()
            self.update.show()

    def btn_help(self):
        self.helper = Help()
        self.helper.build_widgets()
        self.helper.show()

    def btn_win(self):
        self.creation = CreateNewDB()
        self.creation.build_widgets()
        self.creation.show()

    def btn_download(self):
        if len(window.data) == 0:
            print('Сначала загрузите таблицу!')
        else:
            self.download = Download()
            self.download.build_widgets()
            self.download.show()

    def openfile(self):
        self.open_name = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.suffix = self.open_name.split('.')
        for i in self.suffix:
            self.suffix = i
        if self.suffix == 'txt':
            self.open_txt_file()
        if self.suffix == 'db':
            self.open_db()

    def open_txt_file(self):
        if self.suffix == 'txt':
            f = open(self.open_name, 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
        else:
            self.failed_load_txt_file = Mistakes()
            self.failed_load_txt_file.show()

    def open_db(self):
        self.data_base = self.open_name

        self.data_base = str(self.data_base)
        self.new_data_base = self.parse(self.data_base)

        self.new_data = self.update_list_tables(self.new_data_base)

        self.new_data.clear()

    @staticmethod
    def parse(database_path):
        new_path = database_path.split('/')
        database_file_name = './' + new_path[-1]

        return database_file_name

    def update_list_tables(self, data_base):
        data_for_list_of_table = qt_data_base.MyDataBase.get_inform_from_db(data_base)

        self.pushButton_2.clicked.connect(self.text_view)
        self.pushButton_3.clicked.connect(self.table_view)
        self.listWidget.clear()
        for i in data_for_list_of_table:
            for j in i:
                self.listWidget.insertItem(self.counter, j)
                self.counter += 1
                self.new_data.append(j)

        return self.new_data

    def output(self):
        self.comboBox.clear()
        self.textEdit.clear()
        self.tableEdit.clear()

        self.clear_table.setParent(self.layoutWidget)
        self.verticalLayout.addWidget(self.clear_table)

        self.delete_table.setParent(self.layoutWidget)
        self.verticalLayout.addWidget(self.delete_table)

        self.import_lst.clear()

        try:
            self.table = self.listWidget.selectedItems()
            for i in self.table:
                self.table = i
                self.table = self.table.text()

        except TypeError:
            pass

        if type(self.table) is tuple:
            self.table = str(self.table[0])

        self.data = qt_data_base.MyDataBase.sqlite3_simple_read_db(self.data_base, self.table)
        self.new_data = self.data[0]

        for i in self.new_data:
            self.comboBox.addItem(i)
        full_str = ""
        count = 0
        self.output_on_display = self.data[1]
        self.tableEdit.setColumnCount(len(self.new_data))
        self.tableEdit.setRowCount(len(self.output_on_display))
        for i in self.output_on_display:
            self.import_lst.append(i)
            for j in i:
                if type(j) is not str:
                    j = str(j)
                full_str += j
                str_item = ''
                str_item += j
                item = QTableWidgetItem(str_item)
                self.tableEdit.setItem(0, count, item)
                count += 1
                full_str += ', '
            self.textEdit.append(full_str)
            full_str = ''

    def text_view(self):
        self.textEdit.setParent(self.layoutWidget1)
        self.verticalLayout_3.addWidget(self.textEdit)
        self.tableEdit.setParent(None)
        self.output()

    def table_view(self):
        self.textEdit.setParent(None)
        self.tableEdit.setParent(self.layoutWidget1)
        self.verticalLayout_3.addWidget(self.tableEdit)
        self.output()

    def clear_data_from_table(self):
        qt_data_base.MyDataBase.sqlite3_simple_clear_table(self.data_base, self.table)
        self.textEdit.clear()
        self.textEdit.setText('')
        return

    def del_table(self):
        try:
            qt_data_base.MyDataBase.sqlite3_simple_delete_table(self.data_base, self.table)
            list_tables = self.update_list_tables(self.data_base)
            list_tables.clear()
            self.textEdit.clear()
            self.textEdit.setText('')
            return
        except sqlite3.OperationalError:
            print('MISTAKE')

    def choice_of_main_param(self):
        self.result = self.get_result_from_db()
        if self.result != 'Значение не найдено в базе данных!':
            data = ''
            for i in self.result:
                for j in i:
                    data += str(j)
                    data += ', '
                data += '\n'

            self.textEdit.setText(data)
        else:
            self.textEdit.setText(self.result)

    def get_result_from_db(self):
        self.column_names = window.data[0]
        # получаем выбранный элемент из Combobox
        self.choice_row = self.comboBox.currentText()
        # записываем в переменную полученное значение из QLineEdit
        self.res = self.lineEdit.text()
        # проверяем, есть ли выбранный элемент во всех колонках
        if self.choice_row in self.column_names:
            # получаем инфу из бд, записываем ее в переменную
            self.result = qt_data_base.MyDataBase.simple_search_from_db(window.data_base, window.table,
                                                                        self.choice_row, self.res)
            print(f'self.result: {self.result}')

        return self.result

    def cancel(self):
        print("cancel")
        self.lineEdit.clear()
        self.textEdit.clear()


class AddBook(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.setWindowTitle('Добавить книгу')
        self.v_layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.v_layout)
        self.column_names = []
        self.widgets = []
        self.record = []
        self.enters_data = []
        self.create_enter_window()

    def create_enter_window(self):
        self.setLayout(self.main_layout)
        self.setLayout(self.v_layout)

    def build_widgets(self):
        self.column_names = window.data[0]

        for row, i in enumerate(self.column_names):
            label = QtWidgets.QLabel(i)
            self.main_layout.addWidget(label, row)

            line_edit = QtWidgets.QLineEdit(self)
            self.main_layout.addWidget(line_edit, row)

            self.widgets.append((label, line_edit))
        self.main_layout.addLayout(self.v_layout)

        show = QtWidgets.QPushButton('Ввод')
        show.clicked.connect(self.show_content)
        self.v_layout.addWidget(show, len(self.column_names) + 1)

        enter_btn = QtWidgets.QPushButton('Сброс')
        enter_btn.clicked.connect(self.add_clear)
        self.v_layout.addWidget(enter_btn, len(self.column_names) + 1)

        update_main = QtWidgets.QPushButton('Обновить')
        update_main.clicked.connect(self.update_main_window)
        self.v_layout.addWidget(update_main, len(self.column_names) + 1)

    def add_clear(self):
        for i in self.widgets:
            i[1].clear()

    def show_content(self):

        for label, line_edit in self.widgets:
            self.record.append(line_edit.text())
        print(self.record)

        self.get_item()

    def get_item(self):
        remember_table = window.table
        self.enters_data.clear()
        self.enters_data = self.record

        if len(self.enters_data) > 1:
            qt_data_base.MyDataBase.add_record_table(self.enters_data, window.data_base, window.table)

        if remember_table != window.table:
            self.record.clear()

    @staticmethod
    def update_main_window():
        if window.tableEdit.parent() is None:
            window.text_view()
        else:
            window.table_view()


class DelBook(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.v1_layout = QtWidgets.QVBoxLayout(self)
        self.v2_layout = QtWidgets.QVBoxLayout(self)
        self.v3_layout = QtWidgets.QVBoxLayout(self)
        self.textEdit = QtWidgets.QTextEdit()
        self.lineEdit = QtWidgets.QLineEdit()
        self.comboBox = QtWidgets.QComboBox()
        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)

        self.setWindowTitle('Удалить книгу')
        self.column_names = []
        self.result = []
        self.choice_row = ''
        self.res = ''
        self.create_del_window()

    def create_del_window(self):

        self.setLayout(self.main_layout)
        self.setLayout(self.v1_layout)
        self.setLayout(self.v2_layout)
        self.setLayout(self.v3_layout)

    def build_widgets(self):
        self.column_names = window.data[0]
        self.main_layout.addLayout(self.v1_layout)
        self.main_layout.addLayout(self.v2_layout)
        self.main_layout.addLayout(self.v3_layout)

        self.v1_layout.addWidget(self.comboBox)
        for i in self.column_names:
            self.comboBox.addItem(i)

        self.v1_layout.addItem(self.verticalSpacer)

        self.v2_layout.addWidget(self.lineEdit)
        self.v2_layout.addWidget(self.textEdit)

        show = QtWidgets.QPushButton('Ввод')
        show.clicked.connect(self.choice_of_param)
        self.v3_layout.addWidget(show, len(self.column_names) + 1)

        enter_btn = QtWidgets.QPushButton('Удалить')
        enter_btn.clicked.connect(self.delete_record)
        self.v3_layout.addWidget(enter_btn, len(self.column_names) + 1)

        cancel = QtWidgets.QPushButton('Отмена')
        cancel.clicked.connect(self.cancel)
        self.v3_layout.addWidget(cancel, len(self.column_names) + 1)

        update_main = QtWidgets.QPushButton('Обновить')
        update_main.clicked.connect(self.update_main_window)
        self.v3_layout.addWidget(update_main, len(self.column_names) + 1)
        self.v3_layout.addItem(self.verticalSpacer)

    def test(self):
        print('click')
        print(self.comboBox.currentText())

    def choice_of_param(self):
        self.result = self.get_result_from_db()
        if self.result != 'Значение не найдено в базе данных!':
            data = ''
            for i in self.result:
                for j in i:
                    data += str(j)
                    data += ', '

            self.textEdit.setText(data)
        else:
            self.textEdit.setText(self.result)

    def get_result_from_db(self):
        self.column_names = window.data[0]
        # получаем выбранный элемент из Combobox
        self.choice_row = self.comboBox.currentText()
        # записываем в переменную полученное значение из QLineEdit
        self.res = self.lineEdit.text()
        # проверяем, есть ли выбранный элемент во всех колонках
        if self.choice_row in self.column_names:
            # получаем инфу из бд, записываем ее в переменную
            self.result = qt_data_base.MyDataBase.simple_search_from_db(window.data_base, window.table,
                                                                        self.choice_row, self.res)
        return self.result

    def delete_record(self):
        self.choice_row = self.comboBox.currentText()
        qt_data_base.MyDataBase.sqlite3_simple_delete_record(window.data_base, window.table, self.choice_row, self.res)
        self.textEdit.clear()
        self.lineEdit.clear()

    def cancel(self):
        self.result = []
        self.textEdit.clear()
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)

    def update_main_window(self):
        self.result = []
        if window.tableEdit.parent() is None:
            window.text_view()
        else:
            window.table_view()


class UpdateBook(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.v1_layout = QtWidgets.QVBoxLayout(self)

        self.v2_layout = QtWidgets.QVBoxLayout(self)

        self.v3_layout = QtWidgets.QVBoxLayout(self)

        self.textEdit = QtWidgets.QTextEdit()

        self.lineEdit = QtWidgets.QLineEdit()

        self.comboBox = QtWidgets.QComboBox()

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.setWindowTitle('Редактировать книгу')
        self.create_up_window()
        self.column_names = []
        self.choice_row = ''
        self.res = []
        self.result = []
        self.zero = 0
        self.my_lst = []
        self.number_str = 0

    def create_up_window(self):
        self.setLayout(self.main_layout)
        self.setLayout(self.v1_layout)
        self.setLayout(self.v2_layout)
        self.setLayout(self.v3_layout)

    def build_widgets(self):
        self.column_names = window.data[0]
        self.main_layout.addLayout(self.v1_layout)
        self.main_layout.addLayout(self.v2_layout)
        self.main_layout.addLayout(self.v3_layout)

        self.v1_layout.addWidget(self.comboBox)
        self.v1_layout.addWidget(self.comboBox)
        for i in self.column_names:
            self.comboBox.addItem(i)

        self.v1_layout.addItem(self.verticalSpacer)

        self.v2_layout.addWidget(self.lineEdit)
        self.v2_layout.addWidget(self.textEdit)

        show = QtWidgets.QPushButton('Ввод')
        show.clicked.connect(self.choice_of_update_param)
        self.v3_layout.addWidget(show, len(self.column_names) + 1)

        enter_btn = QtWidgets.QPushButton('Редактировать')
        enter_btn.clicked.connect(self.update_record)
        self.v3_layout.addWidget(enter_btn, len(self.column_names) + 1)

        cancel = QtWidgets.QPushButton('Отмена')
        cancel.clicked.connect(self.cancel)
        self.v3_layout.addWidget(cancel, len(self.column_names) + 1)

        update_main = QtWidgets.QPushButton('Обновить')
        update_main.clicked.connect(self.test)
        self.v3_layout.addWidget(update_main, len(self.column_names) + 1)
        self.v3_layout.addItem(self.verticalSpacer)

    def test(self):
        print('click')
        print(self.comboBox.currentText())

    def choice_of_update_param(self):
        column_names = window.data[0]

        self.choice_row = self.comboBox.currentText()
        self.res = self.lineEdit.text()
        if self.choice_row in column_names:
            self.result = qt_data_base.MyDataBase.simple_search_from_db(window.data_base, window.table, self.choice_row, self.res)

            if self.result == 'Значение не найдено в базе данных!':
                window.textEdit.clear()

            self.textEdit.clear()
            my_data = []
            for i in self.result:
                for j in i:
                    my_data.append(str(j) + '\n')
                my_data.append('\n')
            test = ''
            for i in my_data:
                test += i
            self.textEdit.setText(test)

            if len(self.result) > 1:
                self.find_more_one_str()
        return self.result

    def find_more_one_str(self):
        print('Найдено более одной строки! Измените параметры поиска!')

    def cancel(self):
        self.result = []
        self.textEdit.clear()
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)

    def update_record(self):
        a = self.textEdit.toPlainText()

        changed_string = a.split('\n')
        changed_string = changed_string[0:-2]

        self.number_str = int(self.number_str) - 1
        source_string = []
        for i in self.result:
            for j in i:
                source_string.append(j)

        for i in range(0, len(window.data[0])):
            try:
                if changed_string[i] == source_string[i]:
                    pass
            except IndexError:
                pass
            else:
                param_value = changed_string[i]
                step = i
                param_column = self.column_names[step]
                qt_data_base.MyDataBase.sqlite3_update_record(window.data_base, window.table, param_column, param_value,
                                                              self.choice_row, self.res)
        self.textEdit.clear()


class CreateNewDB(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.create_db = QtWidgets.QPushButton()
        self.create_db.setText("Создать новую базу данных")
        self.create_db.clicked.connect(self.create_new_file_db)
        self.create_tbl = QtWidgets.QPushButton()
        self.create_tbl.setText("Создать новую таблицу")
        self.create_tbl.clicked.connect(self.create_win_create_table)
        self.delete_db = QtWidgets.QPushButton()
        self.delete_db.setText("Удалить базу данных")
        self.delete_db.clicked.connect(self.delete_file_db)
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.v1_layout = QtWidgets.QVBoxLayout(self)
        self.v2_layout = QtWidgets.QVBoxLayout(self)
        self.v3_layout = QtWidgets.QVBoxLayout(self)
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.label = QtWidgets.QLabel(self)
        self.label1 = QtWidgets.QLabel(self)
        self.enter = QtWidgets.QPushButton()
        self.data_base = ''

    def create_window(self):
        self.setLayout(self.main_layout)
        self.setLayout(self.v1_layout)
        self.setLayout(self.v2_layout)
        self.setLayout(self.v3_layout)

    def build_widgets(self):
        self.v1_layout.addWidget(self.create_db)
        self.v1_layout.addWidget(self.create_tbl)
        self.v1_layout.addWidget(self.delete_db)
        self.main_layout.addLayout(self.v1_layout)

    def create_new_file_db(self):
        self.data_base = QFileDialog.getSaveFileName(window, 'Open file', '')[0]
        self.new_data_base = window.parse(self.data_base)
        self.suffix = self.data_base.split('.')
        for i in self.suffix:
            self.suffix = i

            if self.suffix == 'db':
                window.data_base = self.data_base
                self.create_win_create_table()

            else:
                pass

    def create_win_create_table(self):
        if window.data_base == '':
            print('mistake')
        else:
            self.main_layout.addLayout(self.v2_layout)
            self.main_layout.addLayout(self.v3_layout)
            self.v2_layout.addWidget(self.label1)

            self.v2_layout.addWidget(self.line_edit)
            self.v2_layout.addWidget(self.label)
            self.v2_layout.addWidget(self.line_edit2)
            self.v3_layout.addWidget(self.enter)

            self.enter.setText("Ввод")
            self.enter.clicked.connect(self.get_create_data)
            self.label.setText("Введите через запятую: Название книги, \n Имя автора и Год публикации")
            self.label1.setText("Введите название таблицы")

    def get_create_data(self):
        window.table = self.line_edit.text()
        column_values = self.line_edit2.text()

        self.column_data = column_values
        self.column_data = self.column_data.split(',')

        self.create_table(window.data_base, window.table, self.column_data)
        window.update_list_tables(window.data_base)
        self.line_edit.clear()
        self.line_edit2.clear()

    @staticmethod
    def create_table(data_base, table, column_data):
        try:
            con = sqlite3.connect(data_base)
            cur = con.cursor()
            q = """
                    CREATE TABLE {table} ( 
                      Name {txt}, 
                      Author {txt}, 
                      Published year {txt})
                    """
            cur.execute(q.format(table=table, txt='TEXT'))
            cur.execute('INSERT INTO ' + table + ' VALUES(?, ?, ?)', column_data)
            con.commit()
            cur.close()
            con.close()
        except sqlite3.OperationalError:
            pass

    @staticmethod
    def delete_file_db():
        filename = QFileDialog.getOpenFileName(window, 'Open file', '')[0]
        if Path(filename).suffix == '.db':
            answer = True
            if answer is True:
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
                os.remove(path)
                if filename == window.data_base:
                    window.data_base = ''
                    window.textEdit.clear()


class Download(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.txt = QtWidgets.QPushButton()
        self.txt.setText("Выгрузить в .txt")
        self.json = QtWidgets.QPushButton()
        self.json.setText("Выгрузить в .json")
        self.create_download_window()

    def create_download_window(self):
        self.setLayout(self.main_layout)

    def build_widgets(self):
        self.main_layout.addWidget(self.txt)
        self.txt.clicked.connect(self.download_txt)
        self.main_layout.addWidget(self.json)
        self.json.clicked.connect(self.download_json)

    def download_txt(self):
        save_name = QFileDialog.getSaveFileName(window, 'Open file', '.txt')[0]
        if Path(save_name).suffix == '.txt':
            data_txt = window.textEdit.toPlainText()
            f = open(save_name, 'w')
            f.write(data_txt)
            f.close()

    @staticmethod
    def download_json():
        column_names = window.new_data
        step = len(column_names)
        save_name = QFileDialog.getSaveFileName(window, 'Open file', '.json')[0]
        data = window.import_lst
        print(f' data {data}')
        if len(data[0]) == step:
            pass
        else:
            data = window.import_lst[step::]

        data2 = list(map(list, zip(*data)))

        data3 = {key: value for key, value in zip(column_names, data2)}

        column = list(data3.keys())

        df = pd.DataFrame(data3, columns=column)

        data_dict = df.to_dict(orient="records")
        with open(save_name, "w+") as f:
            json.dump(data_dict, f, indent=4)

        data.clear()
        data2.clear()
        data3.clear()


class Help(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.v1_layout = QtWidgets.QVBoxLayout(self)
        self.v2_layout = QtWidgets.QVBoxLayout(self)
        self.v3_layout = QtWidgets.QVBoxLayout(self)

        self.help_window = QtWidgets.QTextEdit()
        self.picture_lst = []
        self.my_iterator = []
        self.forward_button = QtWidgets.QPushButton()

        self.create_help_window()
        self.main_win_button = QtWidgets.QPushButton()
        self.main_win_button.setText("Главное окно")
        self.add_db_table = QtWidgets.QPushButton()
        self.add_db_table.setText("Добавить таблицу")
        self.add_string_button = QtWidgets.QPushButton()
        self.add_string_button.setText("Добавить строку")
        self.load_file_button = QtWidgets.QPushButton()
        self.load_file_button.setText("Загрузить")
        self.del_string_button = QtWidgets.QPushButton()
        self.del_string_button.setText("Удалить строку")
        self.download_file_button = QtWidgets.QPushButton()
        self.download_file_button.setText("Выгрузить")
        self.update_string_button = QtWidgets.QPushButton()
        self.update_string_button.setText("Обновить строку")
        self.label = QLabel()
        self.label.setPixmap(QPixmap(':/img/kls.png'))
        self.fram = QtWidgets.QFrame()
        self.text = QtWidgets.QTextEdit()

    def create_help_window(self):
        self.setLayout(self.main_layout)
        self.setLayout(self.v1_layout)
        self.setLayout(self.v2_layout)
        self.setLayout(self.v3_layout)

    def build_widgets(self):
        self.main_layout.addLayout(self.v1_layout)
        self.main_layout.addLayout(self.v2_layout)
        self.v1_layout.addWidget(self.main_win_button)
        self.main_win_button.clicked.connect(self.main)

        self.v1_layout.addWidget(self.add_db_table)
        self.add_db_table.clicked.connect(self.add_db)

        self.v1_layout.addWidget(self.add_string_button)
        self.add_string_button.clicked.connect(self.add_string)

        self.v1_layout.addWidget(self.load_file_button)
        self.load_file_button.clicked.connect(self.load_file)

        self.v1_layout.addWidget(self.del_string_button)
        self.del_string_button.clicked.connect(self.del_string)

        self.v1_layout.addWidget(self.download_file_button)
        self.download_file_button.clicked.connect(self.download_file)

        self.v1_layout.addWidget(self.update_string_button)
        self.update_string_button.clicked.connect(self.update_string)

        self.v2_layout.addWidget(self.fram)
        self.v2_layout.addWidget(self.text)

    def main(self):
        self.text.clear()
        help_text = 'Чтобы воспользоваться функциями "добавить книгу", "удалить книгу", "выгрузить" и ' \
                    '"обновить книгу" предварительно необходимо загрузить базу данных и таблицу. На главном ' \
                    'экране можно пользоваться поиском по таблице, загружать таблицу в виде текста или в табличном виде'

        self.text.setText(help_text)

    def add_db(self):
        self.text.clear()
        help_text = 'Чтобы добавить новую базу данных или таблицу нажмите "добавить новую базу данных" и ' \
                    'следуйте инструкциям. В этом же разделе можно удалить файл базы данных'

        self.text.setText(help_text)

    def add_string(self):
        self.text.clear()
        help_text = 'Чтобы добавить книгу необходимо предварительно загрузить таблицу. Затем нажмите на ' \
                    'главном экране кнопку "добавить книгу", введите значения в соответствующие поля вашей ' \
                    'таблицы и нажмите ввод'

        self.text.setText(help_text)

    def load_file(self):
        self.text.clear()
        help_text = 'Чтобы загрузить существующий файл базы данных нажмите на главном экране кнопку "загрузить" ' \
                    'и выберите файл с раширением .db'

        self.text.setText(help_text)

    def del_string(self):
        self.text.clear()
        help_text = 'Чтобы удалить книгу необходимо предварительно загрузить таблицу. Затем нажмите на ' \
                    'главном экране кнопку "удалить книгу", выберите параметры поиска, найдите нужную книгу, ' \
                    'и нажмите удалить'

        self.text.setText(help_text)

    def download_file(self):
        self.text.clear()
        help_text = 'Чтобы сохранить информацию с главного экрана нажмите выгрузить. ' \
                    'Выгрузка доступна в форматах .txt и .json'

        self.text.setText(help_text)

    def update_string(self):
        self.text.clear()
        help_text = 'Чтобы отредактировать (обновить) книгу необходимо предварительно загрузить таблицу. ' \
                    'Затем нажмите на главном экране кнопку "обновить книгу", выберите параметры поиска, ' \
                    'найдите нужную книгу, введите новые значения прямо в окне вместо существующих и ' \
                    'нажмите редактировать'

        self.text.setText(help_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    window.show()

    sys.exit(app.exec_())

