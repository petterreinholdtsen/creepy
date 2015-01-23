# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Development/python/creepy/gui/aboutDialog.ui'
#
# Created: Thu Oct 16 21:10:48 2014
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(519, 729)
        aboutDialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/creepy/creepy")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        aboutDialog.setModal(False)
        self.verticalLayoutWidget = QtGui.QWidget(aboutDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 478, 706))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), aboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About", None))
        self.label.setText(_translate("aboutDialog", "<html><head/><body><p align=\"center\"><img src=\":/creepy/creepy\"/></p><p><br/></p><p align=\"center\"><span style=\" font-size:9pt;\">Creepy is a geolocation OSINT tool. </span></p><p><br/></p><p><span style=\" font-weight:600;\">Version : </span>1.2 - Codename &quot;<span style=\" font-style:italic;\">SKUP</span>&quot;</p><p><span style=\" font-weight:600;\">Author</span> : Ioannis Kakavas &lt; jkakavas@gmail.com &gt;</p><p><span style=\" font-weight:600;\">Website</span>: www.geocreepy.com</p></body></html>", None))

import creepy_resources_rc
