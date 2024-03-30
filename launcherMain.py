# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QWidget)
import rc_ner_rec
from minecraftFunctions import runGame






class GameThread(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        runGame()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/rec/pixel-cat.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QLabel#minRAMText, QLabel#maxRAMText{\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget#JavaTab , QWidget#MCTab{\n"
"\n"
"background:qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(186, 87, 255, 255), stop:0.12 rgba(217, 88, 199, 255), stop:1 rgba(254, 90, 129, 255))\n"
"}\n"
"QLineEdit#lineEdit , QLineEdit#lineEdit_2{\n"
"border-radius: 10px;\n"
"width: 196px;\n"
"height: 25px;\n"
"background: #fff;\n"
"\n"
"font-family: var(--font-family);\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #000;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel#shade {\n"
"background: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QLabel#registerBox{\n"
"border-radius: 14px;\n"
"width: 404px;\n"
"height: 200px;\n"
"background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(186, 87, 255, 255), stop:0.12 rgba(217, 88, 199, 255), stop:1 rgba(254, 90, 129, 255))\n"
"}\n"
"QLabel#settingsBox{\n"
"border-radius: 14px;\n"
"width"
                        ": 359px;\n"
"height: 600px;\n"
"background:qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(186, 87, 255, 255), stop:0.12 rgba(217, 88, 199, 255), stop:1 rgba(254, 90, 129, 255))\n"
"}\n"
"QLabel#javaLabel{\n"
"border-radius: 10px;\n"
"width: 69px;\n"
"height: 25px;\n"
"background: #fff;\n"
"font-family: var(--font-family);\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #000;\n"
"}\n"
"QLabel#mcLabel{\n"
"border-radius: 10px;\n"
"width: 69px;\n"
"height: 25px;\n"
"background: #fff;\n"
"font-family: var(--font-family);\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #000;\n"
"}\n"
"QLabel#registerBoxText {\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"QPushButton#play,QPushButton#settings {\n"
"border-radius: 10px;\n"
"width: 196px;\n"
"height: 25px;\n"
"font-family: var(--font-family);\n"
"font-weight: 700;\n"
"font-size: 12px;\n"
"text-align: center;\n"
"color: #000;\n"
"ba"
                        "ckground: #fff\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 290, 222, 222))
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setPixmap(QPixmap(u":/circles/rec/scond_circle.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(31, 293, 196, 25))
        font = QFont()
        font.setBold(True)
        self.play.setFont(font)
        self.play.setStyleSheet(u"")
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(31, 347, 196, 25))
        self.settings.setFont(font)
        self.settings.setStyleSheet(u"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(31, 239, 196, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setMaxLength(24)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-33, 143, 325, 325))
        self.label.setPixmap(QPixmap(u":/circles/rec/first_circle.png"))
        self.label.setScaledContents(True)
        self.shade = QLabel(self.centralwidget)
        self.shade.setObjectName(u"shade")
        self.shade.setEnabled(False)
        self.shade.setGeometry(QRect(0, 0, 800, 600))
        self.shade.setMouseTracking(False)
        self.shade.setToolTipDuration(-1)
        self.shade.setAutoFillBackground(False)
        self.shade.setFrameShape(QFrame.NoFrame)
        self.shade.setScaledContents(False)
        self.shade.setWordWrap(False)
        self.registerFrame = QFrame(self.centralwidget)
        self.registerFrame.setObjectName(u"registerFrame")
        self.registerFrame.setEnabled(True)
        self.registerFrame.setGeometry(QRect(198, 198, 421, 221))
        self.registerFrame.setStyleSheet(u"")
        self.registerFrame.setFrameShape(QFrame.NoFrame)
        self.registerFrame.setFrameShadow(QFrame.Raised)
        self.registerBox = QLabel(self.registerFrame)
        self.registerBox.setObjectName(u"registerBox")
        self.registerBox.setGeometry(QRect(6, 7, 404, 200))
        self.git = QLabel(self.registerFrame)
        self.git.setObjectName(u"git")
        self.git.setGeometry(QRect(282, 184, 22, 22))
        self.git.setPixmap(QPixmap(u":/icons/rec/git.png"))
        self.git.setScaledContents(True)
        self.discord = QLabel(self.registerFrame)
        self.discord.setObjectName(u"discord")
        self.discord.setGeometry(QRect(339, 182, 25, 25))
        self.discord.setPixmap(QPixmap(u":/icons/rec/discord.png"))
        self.discord.setScaledContents(True)
        self.telega = QLabel(self.registerFrame)
        self.telega.setObjectName(u"telega")
        self.telega.setGeometry(QRect(369, 182, 25, 25))
        self.telega.setPixmap(QPixmap(u":/icons/rec/telega.png"))
        self.telega.setScaledContents(True)
        self.registerBoxText = QLabel(self.registerFrame)
        self.registerBoxText.setObjectName(u"registerBoxText")
        self.registerBoxText.setGeometry(QRect(114, 94, 187, 13))
        self.registerBoxText.setFont(font)
        self.registerBoxText.setAlignment(Qt.AlignCenter)
        self.youtube = QLabel(self.registerFrame)
        self.youtube.setObjectName(u"youtube")
        self.youtube.setGeometry(QRect(309, 182, 25, 25))
        self.youtube.setPixmap(QPixmap(u":/icons/rec/you_tube.png"))
        self.youtube.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.registerFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 60, 196, 25))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"")
        self.lineEdit_2.setMaxLength(24)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setDragEnabled(False)
        self.exitButton_2 = QPushButton(self.registerFrame)
        self.exitButton_2.setObjectName(u"exitButton_2")
        self.exitButton_2.setGeometry(QRect(10, 20, 30, 26))
        icon1 = QIcon()
        icon1.addFile(u":/icons/rec/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton_2.setIcon(icon1)
        self.settingsFrame = QFrame(self.centralwidget)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setGeometry(QRect(450, 0, 359, 600))
        self.settingsFrame.setStyleSheet(u"")
        self.settingsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Raised)
        self.settingsBox = QLabel(self.settingsFrame)
        self.settingsBox.setObjectName(u"settingsBox")
        self.settingsBox.setGeometry(QRect(0, 0, 359, 600))
        self.tabWidget = QTabWidget(self.settingsFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 10, 270, 500))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.JavaTab = QWidget()
        self.JavaTab.setObjectName(u"JavaTab")
        self.JavaTab.setStyleSheet(u"")
        self.minRAM = QSpinBox(self.JavaTab)
        self.minRAM.setObjectName(u"minRAM")
        self.minRAM.setGeometry(QRect(180, 50, 42, 22))
        self.maxRAM = QSpinBox(self.JavaTab)
        self.maxRAM.setObjectName(u"maxRAM")
        self.maxRAM.setGeometry(QRect(180, 80, 42, 22))
        self.minRAMText = QLabel(self.JavaTab)
        self.minRAMText.setObjectName(u"minRAMText")
        self.minRAMText.setGeometry(QRect(20, 50, 131, 16))
        self.maxRAMText = QLabel(self.JavaTab)
        self.maxRAMText.setObjectName(u"maxRAMText")
        self.maxRAMText.setGeometry(QRect(20, 80, 131, 16))
        self.tabWidget.addTab(self.JavaTab, "")
        self.MCTab = QWidget()
        self.MCTab.setObjectName(u"MCTab")
        self.tabWidget.addTab(self.MCTab, "")
        self.exitButton = QPushButton(self.settingsFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(0, 10, 30, 26))
        self.exitButton.setIcon(icon1)
        self.back = QLabel(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 800, 600))
        self.back.setPixmap(QPixmap(u":/back/rec/launchBack.jpg"))
        self.back.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.back.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.play.raise_()
        self.settings.raise_()
        self.lineEdit.raise_()
        self.shade.raise_()
        self.registerFrame.raise_()
        self.settingsFrame.raise_()
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.settings.clicked.connect(self.settingsFrame.show)
        self.exitButton.clicked.connect(self.settingsFrame.hide)
        self.exitButton_2.clicked.connect(self.registerFrame.hide)
        self.exitButton.clicked.connect(self.shade.hide)
        self.exitButton_2.clicked.connect(self.shade.hide)
        self.play.clicked.connect(self.gameSlot)
        self.settings.clicked.connect(self.shade.show)
        self.tabWidget.setCurrentIndex(0)

        self.discord.setOpenExternalLinks(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        self.gameThread = GameThread()
        self.registerFrame.hide()
        self.settingsFrame.hide()
        self.shade.hide()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Launcher", u"Launcher", None))
        self.label_2.setText("")
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0442\u0438\u043f\u043e", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText("")
        self.label.setText("")
        self.shade.setText("")
        self.registerBox.setText("")
        self.git.setText("")
        self.discord.setText("")
        self.telega.setText("")
        self.registerBoxText.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.youtube.setText("")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setPlaceholderText("")
        self.exitButton_2.setText("")
        self.settingsBox.setText("")
        self.minRAMText.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0443\u043c \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u044b", None))
        self.maxRAMText.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JavaTab), QCoreApplication.translate("MainWindow", u"Java", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MCTab), QCoreApplication.translate("MainWindow", u"MC", None))
        self.exitButton.setText("")
        self.back.setText("")
    # retranslateUi
    def gameSlot(self):
        self.shade.show()
        self.registerFrame.show()
        self.gameThread.start()

