# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrencyConverterMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from CurrencyConverterClass import *


class Ui_CurrencyConverterMain(object):
    def setupUi(self, CurrencyConverterMain):
        CurrencyConverterMain.setObjectName("CurrencyConverterMain")
        CurrencyConverterMain.resize(355, 442)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CurrencyConverterMain.sizePolicy().hasHeightForWidth())
        CurrencyConverterMain.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(CurrencyConverterMain)
        self.centralwidget.setObjectName("centralwidget")
        self.lblCurrencyFrom = QtWidgets.QLabel(self.centralwidget)
        self.lblCurrencyFrom.setGeometry(QtCore.QRect(10, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrencyFrom.setFont(font)
        self.lblCurrencyFrom.setTextFormat(QtCore.Qt.AutoText)
        self.lblCurrencyFrom.setObjectName("lblCurrencyFrom")
        self.lblCurrencyTo = QtWidgets.QLabel(self.centralwidget)
        self.lblCurrencyTo.setGeometry(QtCore.QRect(10, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrencyTo.setFont(font)
        self.lblCurrencyTo.setTextFormat(QtCore.Qt.AutoText)
        self.lblCurrencyTo.setObjectName("lblCurrencyTo")
        self.cboCurrencyFrom = QtWidgets.QComboBox(self.centralwidget)
        self.cboCurrencyFrom.setGeometry(QtCore.QRect(200, 30, 141, 21))
        self.cboCurrencyFrom.setObjectName("cboCurrencyFrom")
        self.cboCurrencyTo = QtWidgets.QComboBox(self.centralwidget)
        self.cboCurrencyTo.setGeometry(QtCore.QRect(200, 70, 141, 21))
        self.cboCurrencyTo.setObjectName("cboCurrencyTo")
        self.lblAmountFrom = QtWidgets.QLabel(self.centralwidget)
        self.lblAmountFrom.setGeometry(QtCore.QRect(10, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblAmountFrom.setFont(font)
        self.lblAmountFrom.setTextFormat(QtCore.Qt.AutoText)
        self.lblAmountFrom.setObjectName("lblAmountFrom")
        self.txtAmount = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtAmount.setGeometry(QtCore.QRect(150, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtAmount.setFont(font)
        self.txtAmount.setAcceptDrops(True)
        self.txtAmount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtAmount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txtAmount.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtAmount.setObjectName("txtAmount")
        self.lblConvertedAmount_Header = QtWidgets.QLabel(self.centralwidget)
        self.lblConvertedAmount_Header.setGeometry(QtCore.QRect(10, 240, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblConvertedAmount_Header.setFont(font)
        self.lblConvertedAmount_Header.setTextFormat(QtCore.Qt.AutoText)
        self.lblConvertedAmount_Header.setWordWrap(True)
        self.lblConvertedAmount_Header.setObjectName("lblConvertedAmount_Header")
        self.lblConvertedAmount = QtWidgets.QLabel(self.centralwidget)
        self.lblConvertedAmount.setGeometry(QtCore.QRect(170, 250, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblConvertedAmount.setFont(font)
        self.lblConvertedAmount.setTextFormat(QtCore.Qt.AutoText)
        self.lblConvertedAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblConvertedAmount.setObjectName("lblConvertedAmount")
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(10, 160, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.btnConvert.setFont(font)
        self.btnConvert.setObjectName("btnConvert")
        self.lblConversionRate_Header = QtWidgets.QLabel(self.centralwidget)
        self.lblConversionRate_Header.setGeometry(QtCore.QRect(10, 310, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblConversionRate_Header.setFont(font)
        self.lblConversionRate_Header.setTextFormat(QtCore.Qt.AutoText)
        self.lblConversionRate_Header.setObjectName("lblConversionRate_Header")
        self.lblConversionRate = QtWidgets.QLabel(self.centralwidget)
        self.lblConversionRate.setGeometry(QtCore.QRect(220, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblConversionRate.setFont(font)
        self.lblConversionRate.setTextFormat(QtCore.Qt.AutoText)
        self.lblConversionRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblConversionRate.setObjectName("lblConversionRate")
        self.lblLastConversionRateUpdate_Header = QtWidgets.QLabel(self.centralwidget)
        self.lblLastConversionRateUpdate_Header.setGeometry(QtCore.QRect(10, 360, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblLastConversionRateUpdate_Header.setFont(font)
        self.lblLastConversionRateUpdate_Header.setTextFormat(QtCore.Qt.AutoText)
        self.lblLastConversionRateUpdate_Header.setObjectName("lblLastConversionRateUpdate_Header")
        self.lblLastConversionRateUpdate = QtWidgets.QLabel(self.centralwidget)
        self.lblLastConversionRateUpdate.setGeometry(QtCore.QRect(170, 360, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblLastConversionRateUpdate.setFont(font)
        self.lblLastConversionRateUpdate.setTextFormat(QtCore.Qt.AutoText)
        self.lblLastConversionRateUpdate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLastConversionRateUpdate.setObjectName("lblLastConversionRateUpdate")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(10, 390, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        CurrencyConverterMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CurrencyConverterMain)
        self.statusbar.setObjectName("statusbar")
        CurrencyConverterMain.setStatusBar(self.statusbar)

        self.retranslateUi(CurrencyConverterMain)
        QtCore.QMetaObject.connectSlotsByName(CurrencyConverterMain)

    def retranslateUi(self, CurrencyConverterMain):
        _translate = QtCore.QCoreApplication.translate
        CurrencyConverterMain.setWindowTitle(_translate("CurrencyConverterMain", "Currency Converter"))
        self.lblCurrencyFrom.setText(_translate("CurrencyConverterMain", "Currency From:"))
        self.lblCurrencyTo.setText(_translate("CurrencyConverterMain", "Currency To:"))
        self.lblAmountFrom.setText(_translate("CurrencyConverterMain", "Amount:"))
        self.lblConvertedAmount_Header.setText(_translate("CurrencyConverterMain", "Converted Amount:"))
        self.lblConvertedAmount.setText(_translate("CurrencyConverterMain", "0"))
        self.btnConvert.setText(_translate("CurrencyConverterMain", "Convert"))
        self.lblConversionRate_Header.setText(_translate("CurrencyConverterMain", "Conversion Rate:"))
        self.lblConversionRate.setText(_translate("CurrencyConverterMain", "0"))
        self.lblLastConversionRateUpdate_Header.setText(_translate("CurrencyConverterMain", "Last Conversion Rate Update:"))
        self.lblLastConversionRateUpdate.setText(_translate("CurrencyConverterMain", "--"))
        self.btnUpdate.setText(_translate("CurrencyConverterMain", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyConverterMain = QtWidgets.QMainWindow()
    ui = Ui_CurrencyConverterMain()
    ui.setupUi(CurrencyConverterMain)
    ccc = CurrencyConverterClass(ui)
    ccc.Setup(True)
    CurrencyConverterMain.show()
    sys.exit(app.exec_())
