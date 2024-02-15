# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 700, 500))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_import = QPushButton(self.tab)
        self.pushButton_import.setObjectName(u"pushButton_import")
        self.pushButton_import.setGeometry(QRect(10, 10, 100, 24))
        self.comboBox_setname = QComboBox(self.tab)
        self.comboBox_setname.addItem("")
        self.comboBox_setname.setObjectName(u"comboBox_setname")
        self.comboBox_setname.setGeometry(QRect(130, 10, 120, 24))
        self.comboBox_setname.setCurrentText(u"\u4e0d\u9650")
        self.comboBox_position = QComboBox(self.tab)
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.setObjectName(u"comboBox_position")
        self.comboBox_position.setGeometry(QRect(270, 10, 120, 24))
        self.comboBox_config = QComboBox(self.tab)
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.addItem("")
        self.comboBox_config.setObjectName(u"comboBox_config")
        self.comboBox_config.setGeometry(QRect(410, 10, 120, 24))
        self.pushButton_calscore = QPushButton(self.tab)
        self.pushButton_calscore.setObjectName(u"pushButton_calscore")
        self.pushButton_calscore.setGeometry(QRect(550, 10, 100, 24))
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 650, 375))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u9057\u5668\u6570\u636e", None))
        self.comboBox_setname.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0d\u9650", None))

        self.comboBox_position.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0d\u9650", None))
        self.comboBox_position.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5934", None))
        self.comboBox_position.setItemText(2, QCoreApplication.translate("MainWindow", u"\u624b", None))
        self.comboBox_position.setItemText(3, QCoreApplication.translate("MainWindow", u"\u8863\u670d", None))
        self.comboBox_position.setItemText(4, QCoreApplication.translate("MainWindow", u"\u978b", None))
        self.comboBox_position.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7403", None))
        self.comboBox_position.setItemText(6, QCoreApplication.translate("MainWindow", u"\u7ef3", None))

        self.comboBox_config.setItemText(0, QCoreApplication.translate("MainWindow", u"\u94f6\u72fc", None))
        self.comboBox_config.setItemText(1, QCoreApplication.translate("MainWindow", u"\u996e\u6708", None))
        self.comboBox_config.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9ed1\u5854", None))
        self.comboBox_config.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5e03\u6d1b\u59ae\u5a05", None))
        self.comboBox_config.setItemText(4, QCoreApplication.translate("MainWindow", u"\u505c\u4e91", None))
        self.comboBox_config.setItemText(5, QCoreApplication.translate("MainWindow", u"\u955c\u6d41", None))
        self.comboBox_config.setItemText(6, QCoreApplication.translate("MainWindow", u"\u962e\u6885", None))
        self.comboBox_config.setItemText(7, QCoreApplication.translate("MainWindow", u"\u7b26\u7384", None))

        self.pushButton_calscore.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8bc4\u5206", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6f5c\u529b", None))
    # retranslateUi

