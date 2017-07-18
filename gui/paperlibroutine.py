# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paperlibroutine.ui'
#
# Created by: PyQt5 UI code generator 5.9.dev1706151807
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_path_caption = QtWidgets.QLabel(self.centralwidget)
        self.lbl_path_caption.setObjectName("lbl_path_caption")
        self.horizontalLayout_2.addWidget(self.lbl_path_caption)
        self.edit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_path.setObjectName("edit_path")
        self.horizontalLayout_2.addWidget(self.edit_path)
        self.btn_file_dialog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file_dialog.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_file_dialog.setObjectName("btn_file_dialog")
        self.horizontalLayout_2.addWidget(self.btn_file_dialog)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_files = QtWidgets.QWidget()
        self.tab_files.setObjectName("tab_files")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_files)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.table_files_view = QtWidgets.QTableView(self.tab_files)
        self.table_files_view.setObjectName("table_files_view")
        self.gridLayout_3.addWidget(self.table_files_view, 0, 1, 1, 2)
        self.btn_start_reading = QtWidgets.QPushButton(self.tab_files)
        self.btn_start_reading.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_start_reading.setObjectName("btn_start_reading")
        self.gridLayout_3.addWidget(self.btn_start_reading, 1, 2, 1, 1)
        self.tab_widget.addTab(self.tab_files, "")
        self.tab_students = QtWidgets.QWidget()
        self.tab_students.setObjectName("tab_students")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_students)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.table_students_view = QtWidgets.QTableView(self.tab_students)
        self.table_students_view.setObjectName("table_students_view")
        self.gridLayout_4.addWidget(self.table_students_view, 0, 0, 1, 4)
        self.btn_save = QtWidgets.QPushButton(self.tab_students)
        self.btn_save.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_4.addWidget(self.btn_save, 1, 3, 1, 1)
        self.btn_back_choosing = QtWidgets.QPushButton(self.tab_students)
        self.btn_back_choosing.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_back_choosing.setObjectName("btn_back_choosing")
        self.gridLayout_4.addWidget(self.btn_back_choosing, 1, 1, 1, 1)
        self.btn_change = QtWidgets.QPushButton(self.tab_students)
        self.btn_change.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_change.setObjectName("btn_change")
        self.gridLayout_4.addWidget(self.btn_change, 1, 2, 1, 1)
        self.tab_widget.addTab(self.tab_students, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_widget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tab_widget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_path_caption.setText(_translate("MainWindow", "Исходная директория"))
        self.btn_file_dialog.setText(_translate("MainWindow", "..."))
        self.btn_start_reading.setText(_translate("MainWindow", "Далее"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_files), _translate("MainWindow", "Файлы"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_back_choosing.setText(_translate("MainWindow", "Назад"))
        self.btn_change.setText(_translate("MainWindow", "Изменить общее"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_students), _translate("MainWindow", "Студенты"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("MainWindow", "Страница"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

