# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_column_desc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_2.addWidget(self.listWidget_var)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_selected_add_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/arrow_right_hover.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add_2.setIcon(icon)
        self.pushButton_selected_add_2.setObjectName("pushButton_selected_add_2")
        self.verticalLayout_4.addWidget(self.pushButton_selected_add_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_group_add_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_group_add_2.setText("")
        self.pushButton_group_add_2.setIcon(icon)
        self.pushButton_group_add_2.setObjectName("pushButton_group_add_2")
        self.verticalLayout_16.addWidget(self.pushButton_group_add_2)
        self.verticalLayout.addLayout(self.verticalLayout_16)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget_selected = QtWidgets.QListWidget(self.tab)
        self.listWidget_selected.setObjectName("listWidget_selected")
        self.horizontalLayout_4.addWidget(self.listWidget_selected)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_selected_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pyqt/source/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_add.setIcon(icon1)
        self.pushButton_selected_add.setObjectName("pushButton_selected_add")
        self.verticalLayout_6.addWidget(self.pushButton_selected_add)
        self.pushButton_selected_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_up.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pyqt/source/images/up1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_up.setIcon(icon2)
        self.pushButton_selected_up.setObjectName("pushButton_selected_up")
        self.verticalLayout_6.addWidget(self.pushButton_selected_up)
        self.pushButton_selected_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_down.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pyqt/source/images/down1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_down.setIcon(icon3)
        self.pushButton_selected_down.setObjectName("pushButton_selected_down")
        self.verticalLayout_6.addWidget(self.pushButton_selected_down)
        self.pushButton_selected_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_selected_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_selected_del.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_selected_del.setIcon(icon4)
        self.pushButton_selected_del.setObjectName("pushButton_selected_del")
        self.verticalLayout_6.addWidget(self.pushButton_selected_del)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_group = QtWidgets.QListWidget(self.tab)
        self.listWidget_group.setObjectName("listWidget_group")
        self.horizontalLayout_2.addWidget(self.listWidget_group)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_group_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_group_add.setText("")
        self.pushButton_group_add.setIcon(icon1)
        self.pushButton_group_add.setObjectName("pushButton_group_add")
        self.verticalLayout_7.addWidget(self.pushButton_group_add)
        self.pushButton_group_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_group_up.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_up.setText("")
        self.pushButton_group_up.setIcon(icon2)
        self.pushButton_group_up.setObjectName("pushButton_group_up")
        self.verticalLayout_7.addWidget(self.pushButton_group_up)
        self.pushButton_group_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_group_down.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_down.setText("")
        self.pushButton_group_down.setIcon(icon3)
        self.pushButton_group_down.setObjectName("pushButton_group_down")
        self.verticalLayout_7.addWidget(self.pushButton_group_down)
        self.pushButton_group_del = QtWidgets.QPushButton(self.tab)
        self.pushButton_group_del.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_group_del.setText("")
        self.pushButton_group_del.setIcon(icon4)
        self.pushButton_group_del.setObjectName("pushButton_group_del")
        self.verticalLayout_7.addWidget(self.pushButton_group_del)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget_dataset = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_dataset.setObjectName("tableWidget_dataset")
        self.tableWidget_dataset.setColumnCount(0)
        self.tableWidget_dataset.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget_dataset)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_13.addWidget(self.tabWidget)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_code = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_code.setObjectName("pushButton_code")
        self.horizontalLayout_3.addWidget(self.pushButton_code)
        self.pushButton_help = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_help.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pyqt/source/images/lc_helpindex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon5)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据-列出数据"))
        self.label_3.setText(_translate("Form", "全部变量:"))
        self.label.setText(_translate("Form", "已选变量:"))
        self.label_2.setText(_translate("Form", "分组变量:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "基本"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "数据"))
        self.pushButton_code.setText(_translate("Form", "代码"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc
