# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_workshopclass.ui'
#
# Created: Thu Nov  6 12:19:24 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WorkshopClass(object):
    def setupUi(self, WorkshopClass):
        WorkshopClass.setObjectName(_fromUtf8("WorkshopClass"))
        WorkshopClass.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(WorkshopClass)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(WorkshopClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), WorkshopClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), WorkshopClass.reject)
        QtCore.QMetaObject.connectSlotsByName(WorkshopClass)

    def retranslateUi(self, WorkshopClass):
        WorkshopClass.setWindowTitle(_translate("WorkshopClass", "WorkshopClass", None))

