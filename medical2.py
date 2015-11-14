# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical.ui'
#
# Created: Sat Nov 14 08:14:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
import datetime
DB_EXC = MySQLdb

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

def sysTime():
  t = datetime.datetime.now()
  time = str(t.hour) + ':'+str(t.minute)+':'+str(t.second)
  return time
def sysDate():
  t = datetime.datetime.now()
  date = str(t.year)+'-'+str(t.month)+'-'+str(t.day)
  return date

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(882, 771)
        TabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        TabWidget.setWhatsThis(_fromUtf8(""))
        self.db = SQL()
        self.prodTab = QtGui.QWidget()
        self.prodTab.setObjectName(_fromUtf8("prodTab"))
        self.pinsertButton = QtGui.QPushButton(self.prodTab)
        self.pinsertButton.setGeometry(QtCore.QRect(600, 370, 95, 31))
        self.pinsertButton.setToolTip(_fromUtf8(""))
        self.pinsertButton.setIconSize(QtCore.QSize(30, 30))
        self.pinsertButton.setObjectName(_fromUtf8("pinsertButton"))
        self.pidlabel = QtGui.QLabel(self.prodTab)
        self.pidlabel.setGeometry(QtCore.QRect(10, 380, 81, 21))
        self.pidlabel.setObjectName(_fromUtf8("pidlabel"))
        self.pnameEdir = QtGui.QLineEdit(self.prodTab)
        self.pnameEdir.setGeometry(QtCore.QRect(110, 430, 181, 33))
        self.pnameEdir.setObjectName(_fromUtf8("pnameEdir"))
        self.manuEdit = QtGui.QLineEdit(self.prodTab)
        self.manuEdit.setGeometry(QtCore.QRect(110, 490, 181, 33))
        self.manuEdit.setObjectName(_fromUtf8("manuEdit"))
        self.qtyEdit = QtGui.QLineEdit(self.prodTab)
        self.qtyEdit.setGeometry(QtCore.QRect(450, 430, 121, 33))
        self.qtyEdit.setObjectName(_fromUtf8("qtyEdit"))
        self.mrpEdit = QtGui.QLineEdit(self.prodTab)
        self.mrpEdit.setGeometry(QtCore.QRect(450, 490, 121, 33))
        self.mrpEdit.setObjectName(_fromUtf8("mrpEdit"))
        self.pnameLabel = QtGui.QLabel(self.prodTab)
        self.pnameLabel.setGeometry(QtCore.QRect(40, 440, 51, 21))
        self.pnameLabel.setObjectName(_fromUtf8("pnameLabel"))
        self.manuLabel = QtGui.QLabel(self.prodTab)
        self.manuLabel.setGeometry(QtCore.QRect(10, 500, 91, 21))
        self.manuLabel.setObjectName(_fromUtf8("manuLabel"))
        self.cateLabel = QtGui.QLabel(self.prodTab)
        self.cateLabel.setGeometry(QtCore.QRect(370, 380, 65, 21))
        self.cateLabel.setObjectName(_fromUtf8("cateLabel"))
        self.qtyLabel = QtGui.QLabel(self.prodTab)
        self.qtyLabel.setGeometry(QtCore.QRect(340, 440, 101, 21))
        self.qtyLabel.setObjectName(_fromUtf8("qtyLabel"))
        self.mrpLabel = QtGui.QLabel(self.prodTab)
        self.mrpLabel.setGeometry(QtCore.QRect(400, 500, 41, 21))
        self.mrpLabel.setObjectName(_fromUtf8("mrpLabel"))
        self.pdeletebutton = QtGui.QPushButton(self.prodTab)
        self.pdeletebutton.setGeometry(QtCore.QRect(600, 430, 95, 31))
        self.pdeletebutton.setToolTip(_fromUtf8(""))
        self.pdeletebutton.setObjectName(_fromUtf8("pdeletebutton"))
        self.pclearbutton = QtGui.QPushButton(self.prodTab)
        self.pclearbutton.setGeometry(QtCore.QRect(730, 370, 95, 31))
        self.pclearbutton.setToolTip(_fromUtf8(""))
        self.pclearbutton.setObjectName(_fromUtf8("pclearbutton"))
        self.pview = QtGui.QPushButton(self.prodTab)
        self.pview.setGeometry(QtCore.QRect(730, 430, 95, 31))
        self.pview.setToolTip(_fromUtf8(""))
        self.pview.setObjectName(_fromUtf8("pview"))
        self.pclosebutton = QtGui.QPushButton(self.prodTab)
        self.pclosebutton.setGeometry(QtCore.QRect(740, 680, 95, 31))
        self.pclosebutton.setObjectName(_fromUtf8("pclosebutton"))
        self.mfdLabel = QtGui.QLabel(self.prodTab)
        self.mfdLabel.setGeometry(QtCore.QRect(20, 540, 71, 51))
        self.mfdLabel.setObjectName(_fromUtf8("mfdLabel"))
        self.exdLabel = QtGui.QLabel(self.prodTab)
        self.exdLabel.setGeometry(QtCore.QRect(350, 560, 81, 21))
        self.exdLabel.setObjectName(_fromUtf8("exdLabel"))
        self.PInventTable = QtGui.QTableWidget(self.prodTab)
        self.PInventTable.setGeometry(QtCore.QRect(20, 30, 791, 321))
        self.PInventTable.setRowCount(100)
        self.PInventTable.setColumnCount(100)
        self.PInventTable.setObjectName(_fromUtf8("PInventTable"))
        self.PInventBrowser = QtGui.QTextBrowser(self.prodTab)
        self.PInventBrowser.setGeometry(QtCore.QRect(10, 660, 671, 61))
        self.PInventBrowser.setObjectName(_fromUtf8("PInventBrowser"))
        self.didLabel = QtGui.QLabel(self.prodTab)
        self.didLabel.setGeometry(QtCore.QRect(20, 620, 65, 21))
        self.didLabel.setObjectName(_fromUtf8("didLabel"))
        self.mcompEdit = QtGui.QLineEdit(self.prodTab)
        self.mcompEdit.setGeometry(QtCore.QRect(450, 610, 141, 33))
        self.mcompEdit.setObjectName(_fromUtf8("mcompEdit"))
        self.mcompLabel = QtGui.QLabel(self.prodTab)
        self.mcompLabel.setGeometry(QtCore.QRect(320, 620, 111, 21))
        self.mcompLabel.setObjectName(_fromUtf8("mcompLabel"))
        self.pidEdit = QtGui.QLineEdit(self.prodTab)
        self.pidEdit.setGeometry(QtCore.QRect(110, 370, 181, 33))
        self.pidEdit.setObjectName(_fromUtf8("pidEdit"))
        self.mfdEdit = QtGui.QLineEdit(self.prodTab)
        self.mfdEdit.setGeometry(QtCore.QRect(110, 550, 113, 33))
        self.mfdEdit.setObjectName(_fromUtf8("mfdEdit"))
        self.exdEdit = QtGui.QLineEdit(self.prodTab)
        self.exdEdit.setGeometry(QtCore.QRect(450, 550, 113, 33))
        self.exdEdit.setObjectName(_fromUtf8("exdEdit"))
        self.didBox = QtGui.QComboBox(self.prodTab)
        self.didBox.setGeometry(QtCore.QRect(110, 610, 111, 29))
        self.didBox.setObjectName(_fromUtf8("didBox"))
        self.cateBox = QtGui.QComboBox(self.prodTab)
        self.cateBox.setGeometry(QtCore.QRect(450, 370, 121, 29))
        self.cateBox.setObjectName(_fromUtf8("cateBox"))
        self.cateBox.addItems(["Java", "C#", "Python"])
        self.cateBox.currentIndexChanged.connect(self.selectionchange)
        self.pupdate = QtGui.QPushButton(self.prodTab)
        self.pupdate.setGeometry(QtCore.QRect(600, 490, 95, 31))
        self.pupdate.setObjectName(_fromUtf8("pupdate"))
        self.psearch = QtGui.QPushButton(self.prodTab)
        self.psearch.setGeometry(QtCore.QRect(730, 490, 95, 31))
        self.psearch.setObjectName(_fromUtf8("psearch"))
        TabWidget.addTab(self.prodTab, _fromUtf8(""))
        self.cusTab = QtGui.QWidget()
        self.cusTab.setObjectName(_fromUtf8("cusTab"))
        self.cnamelineedit = QtGui.QLineEdit(self.cusTab)
        self.cnamelineedit.setGeometry(QtCore.QRect(160, 530, 201, 33))
        self.cnamelineedit.setText(_fromUtf8(""))
        self.cnamelineedit.setObjectName(_fromUtf8("cnamelineedit"))
        self.cnameLabel = QtGui.QLabel(self.cusTab)
        self.cnameLabel.setGeometry(QtCore.QRect(30, 540, 111, 21))
        self.cnameLabel.setObjectName(_fromUtf8("cnameLabel"))
        self.lineEdit_8 = QtGui.QLineEdit(self.cusTab)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 470, 201, 33))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.cidLabel = QtGui.QLabel(self.cusTab)
        self.cidLabel.setGeometry(QtCore.QRect(50, 480, 91, 21))
        self.cidLabel.setObjectName(_fromUtf8("cidLabel"))
        self.cnumEdit = QtGui.QLineEdit(self.cusTab)
        self.cnumEdit.setGeometry(QtCore.QRect(160, 590, 201, 33))
        self.cnumEdit.setObjectName(_fromUtf8("cnumEdit"))
        self.cnumLabel = QtGui.QLabel(self.cusTab)
        self.cnumLabel.setGeometry(QtCore.QRect(30, 600, 111, 21))
        self.cnumLabel.setObjectName(_fromUtf8("cnumLabel"))
        self.hdoption = QtGui.QCheckBox(self.cusTab)
        self.hdoption.setGeometry(QtCore.QRect(410, 460, 171, 26))
        self.hdoption.setToolTip(_fromUtf8(""))
        self.hdoption.setObjectName(_fromUtf8("hdoption"))
        self.cinsertbutton = QtGui.QPushButton(self.cusTab)
        self.cinsertbutton.setGeometry(QtCore.QRect(410, 550, 95, 31))
        self.cinsertbutton.setToolTip(_fromUtf8(""))
        self.cinsertbutton.setObjectName(_fromUtf8("cinsertbutton"))
        self.csearchbutton = QtGui.QPushButton(self.cusTab)
        self.csearchbutton.setGeometry(QtCore.QRect(520, 550, 95, 31))
        self.csearchbutton.setToolTip(_fromUtf8(""))
        self.csearchbutton.setObjectName(_fromUtf8("csearchbutton"))
        self.cpurchase = QtGui.QPushButton(self.cusTab)
        self.cpurchase.setGeometry(QtCore.QRect(410, 630, 95, 31))
        self.cpurchase.setToolTip(_fromUtf8(""))
        self.cpurchase.setObjectName(_fromUtf8("cpurchase"))
        self.cusListTable = QtGui.QTableWidget(self.cusTab)
        self.cusListTable.setGeometry(QtCore.QRect(35, 21, 801, 421))
        self.cusListTable.setRowCount(100)
        self.cusListTable.setColumnCount(100)
        self.cusListTable.setObjectName(_fromUtf8("cusListTable"))
        self.CusListBrowser = QtGui.QTextBrowser(self.cusTab)
        self.CusListBrowser.setGeometry(QtCore.QRect(10, 680, 691, 61))
        self.CusListBrowser.setObjectName(_fromUtf8("CusListBrowser"))
        self.cdeletebutton = QtGui.QPushButton(self.cusTab)
        self.cdeletebutton.setGeometry(QtCore.QRect(410, 590, 95, 31))
        self.cdeletebutton.setToolTip(_fromUtf8(""))
        self.cdeletebutton.setObjectName(_fromUtf8("cdeletebutton"))
        self.cclosebutton = QtGui.QPushButton(self.cusTab)
        self.cclosebutton.setGeometry(QtCore.QRect(740, 700, 95, 31))
        self.cclosebutton.setObjectName(_fromUtf8("cclosebutton"))
        self.cupdate = QtGui.QPushButton(self.cusTab)
        self.cupdate.setGeometry(QtCore.QRect(520, 590, 95, 31))
        self.cupdate.setObjectName(_fromUtf8("cupdate"))
        self.custextEdit = QtGui.QTextEdit(self.cusTab)
        self.custextEdit.setGeometry(QtCore.QRect(620, 480, 241, 171))
        self.custextEdit.setObjectName(_fromUtf8("custextEdit"))
        self.caddrlabel = QtGui.QLabel(self.cusTab)
        self.caddrlabel.setGeometry(QtCore.QRect(690, 460, 65, 21))
        self.caddrlabel.setObjectName(_fromUtf8("caddrlabel"))
        self.cclear = QtGui.QPushButton(self.cusTab)
        self.cclear.setGeometry(QtCore.QRect(520, 630, 95, 31))
        self.cclear.setObjectName(_fromUtf8("cclear"))
        TabWidget.addTab(self.cusTab, _fromUtf8(""))
        self.transTab = QtGui.QWidget()
        self.transTab.setObjectName(_fromUtf8("transTab"))
        self.transTable = QtGui.QTableWidget(self.transTab)
        self.transTable.setGeometry(QtCore.QRect(20, 30, 831, 381))
        self.transTable.setRowCount(100)
        self.transTable.setColumnCount(100)
        self.transTable.setObjectName(_fromUtf8("transTable"))
        self.tcidEdit = QtGui.QLineEdit(self.transTab)
        self.tcidEdit.setGeometry(QtCore.QRect(160, 460, 171, 33))
        self.tcidEdit.setObjectName(_fromUtf8("tcidEdit"))
        self.tcidLabel = QtGui.QLabel(self.transTab)
        self.tcidLabel.setGeometry(QtCore.QRect(30, 470, 81, 21))
        self.tcidLabel.setObjectName(_fromUtf8("tcidLabel"))
        self.tpidEdit = QtGui.QLineEdit(self.transTab)
        self.tpidEdit.setGeometry(QtCore.QRect(160, 530, 171, 33))
        self.tpidEdit.setObjectName(_fromUtf8("tpidEdit"))
        self.tpidLabel = QtGui.QLabel(self.transTab)
        self.tpidLabel.setGeometry(QtCore.QRect(40, 540, 81, 21))
        self.tpidLabel.setObjectName(_fromUtf8("tpidLabel"))
        self.tdidEdit = QtGui.QLineEdit(self.transTab)
        self.tdidEdit.setGeometry(QtCore.QRect(160, 610, 181, 33))
        self.tdidEdit.setObjectName(_fromUtf8("tdidEdit"))
        self.tdidLabel = QtGui.QLabel(self.transTab)
        self.tdidLabel.setGeometry(QtCore.QRect(50, 610, 65, 21))
        self.tdidLabel.setObjectName(_fromUtf8("tdidLabel"))
        self.tqtyEdit = QtGui.QLineEdit(self.transTab)
        self.tqtyEdit.setGeometry(QtCore.QRect(440, 530, 113, 33))
        self.tqtyEdit.setObjectName(_fromUtf8("tqtyEdit"))
        self.tqtyLabel = QtGui.QLabel(self.transTab)
        self.tqtyLabel.setGeometry(QtCore.QRect(360, 540, 65, 21))
        self.tqtyLabel.setObjectName(_fromUtf8("tqtyLabel"))
        self.taddButton = QtGui.QPushButton(self.transTab)
        self.taddButton.setGeometry(QtCore.QRect(440, 600, 95, 31))
        self.taddButton.setObjectName(_fromUtf8("taddButton"))
        self.tpurButton = QtGui.QPushButton(self.transTab)
        self.tpurButton.setGeometry(QtCore.QRect(450, 700, 95, 31))
        self.tpurButton.setObjectName(_fromUtf8("tpurButton"))
        self.transBrowser = QtGui.QTextBrowser(self.transTab)
        self.transBrowser.setGeometry(QtCore.QRect(40, 680, 321, 51))
        self.transBrowser.setObjectName(_fromUtf8("transBrowser"))
        self.tcostBrowser = QtGui.QTextBrowser(self.transTab)
        self.tcostBrowser.setGeometry(QtCore.QRect(590, 670, 151, 61))
        self.tcostBrowser.setObjectName(_fromUtf8("tcostBrowser"))
        self.tcostLabel = QtGui.QLabel(self.transTab)
        self.tcostLabel.setGeometry(QtCore.QRect(600, 640, 71, 21))
        self.tcostLabel.setObjectName(_fromUtf8("tcostLabel"))
        self.tclose = QtGui.QPushButton(self.transTab)
        self.tclose.setGeometry(QtCore.QRect(770, 700, 95, 31))
        self.tclose.setObjectName(_fromUtf8("tclose"))
        self.tclear = QtGui.QPushButton(self.transTab)
        self.tclear.setGeometry(QtCore.QRect(770, 590, 95, 31))
        self.tclear.setObjectName(_fromUtf8("tclear"))
        TabWidget.addTab(self.transTab, _fromUtf8(""))
        self.dealTab = QtGui.QWidget()
        self.dealTab.setObjectName(_fromUtf8("dealTab"))
        self.DealTable = QtGui.QTableWidget(self.dealTab)
        self.DealTable.setGeometry(QtCore.QRect(30, 30, 821, 411))
        self.DealTable.setRowCount(100)
        self.DealTable.setColumnCount(100)
        self.DealTable.setObjectName(_fromUtf8("DealTable"))
        self.ddidEdit = QtGui.QLineEdit(self.dealTab)
        self.ddidEdit.setGeometry(QtCore.QRect(100, 480, 151, 33))
        self.ddidEdit.setObjectName(_fromUtf8("ddidEdit"))
        self.dconumEdit = QtGui.QLineEdit(self.dealTab)
        self.dconumEdit.setGeometry(QtCore.QRect(390, 480, 191, 33))
        self.dconumEdit.setObjectName(_fromUtf8("dconumEdit"))
        self.dnameEdit = QtGui.QLineEdit(self.dealTab)
        self.dnameEdit.setGeometry(QtCore.QRect(100, 560, 151, 33))
        self.dnameEdit.setObjectName(_fromUtf8("dnameEdit"))
        self.dpidEdit = QtGui.QLineEdit(self.dealTab)
        self.dpidEdit.setGeometry(QtCore.QRect(390, 560, 113, 33))
        self.dpidEdit.setObjectName(_fromUtf8("dpidEdit"))
        self.ddidLabel = QtGui.QLabel(self.dealTab)
        self.ddidLabel.setGeometry(QtCore.QRect(10, 490, 65, 21))
        self.ddidLabel.setObjectName(_fromUtf8("ddidLabel"))
        self.dnameLabel = QtGui.QLabel(self.dealTab)
        self.dnameLabel.setGeometry(QtCore.QRect(30, 570, 65, 21))
        self.dnameLabel.setObjectName(_fromUtf8("dnameLabel"))
        self.dconumLabel = QtGui.QLabel(self.dealTab)
        self.dconumLabel.setGeometry(QtCore.QRect(270, 490, 111, 21))
        self.dconumLabel.setObjectName(_fromUtf8("dconumLabel"))
        self.dpidLabel = QtGui.QLabel(self.dealTab)
        self.dpidLabel.setGeometry(QtCore.QRect(300, 570, 71, 21))
        self.dpidLabel.setObjectName(_fromUtf8("dpidLabel"))
        self.daddrLabel = QtGui.QLabel(self.dealTab)
        self.daddrLabel.setGeometry(QtCore.QRect(600, 490, 65, 21))
        self.daddrLabel.setObjectName(_fromUtf8("daddrLabel"))
        self.daddrtextEdit = QtGui.QTextEdit(self.dealTab)
        self.daddrtextEdit.setGeometry(QtCore.QRect(660, 480, 201, 121))
        self.daddrtextEdit.setObjectName(_fromUtf8("daddrtextEdit"))
        self.dealBrowser = QtGui.QTextBrowser(self.dealTab)
        self.dealBrowser.setGeometry(QtCore.QRect(15, 611, 261, 91))
        self.dealBrowser.setObjectName(_fromUtf8("dealBrowser"))
        self.daddButon = QtGui.QPushButton(self.dealTab)
        self.daddButon.setGeometry(QtCore.QRect(530, 560, 95, 31))
        self.daddButon.setObjectName(_fromUtf8("daddButon"))
        self.dinsertButton = QtGui.QPushButton(self.dealTab)
        self.dinsertButton.setGeometry(QtCore.QRect(390, 640, 95, 31))
        self.dinsertButton.setObjectName(_fromUtf8("dinsertButton"))
        self.ddelete = QtGui.QPushButton(self.dealTab)
        self.ddelete.setGeometry(QtCore.QRect(510, 640, 95, 31))
        self.ddelete.setObjectName(_fromUtf8("ddelete"))
        self.dupdate = QtGui.QPushButton(self.dealTab)
        self.dupdate.setGeometry(QtCore.QRect(630, 640, 95, 31))
        self.dupdate.setObjectName(_fromUtf8("dupdate"))
        self.dsearch = QtGui.QPushButton(self.dealTab)
        self.dsearch.setGeometry(QtCore.QRect(760, 640, 95, 31))
        self.dsearch.setObjectName(_fromUtf8("dsearch"))
        self.dclose = QtGui.QPushButton(self.dealTab)
        self.dclose.setGeometry(QtCore.QRect(690, 700, 95, 31))
        self.dclose.setObjectName(_fromUtf8("dclose"))
        self.dclear = QtGui.QPushButton(self.dealTab)
        self.dclear.setGeometry(QtCore.QRect(530, 700, 95, 31))
        self.dclear.setObjectName(_fromUtf8("dclear"))
        TabWidget.addTab(self.dealTab, _fromUtf8(""))
        self.docTab = QtGui.QWidget()
        self.docTab.setObjectName(_fromUtf8("docTab"))
        self.docTable = QtGui.QTableWidget(self.docTab)
        self.docTable.setGeometry(QtCore.QRect(40, 30, 771, 411))
        self.docTable.setRowCount(100)
        self.docTable.setColumnCount(100)
        self.docTable.setObjectName(_fromUtf8("docTable"))
        self.docidEdit = QtGui.QLineEdit(self.docTab)
        self.docidEdit.setGeometry(QtCore.QRect(110, 480, 113, 33))
        self.docidEdit.setObjectName(_fromUtf8("docidEdit"))
        self.docnameEdit = QtGui.QLineEdit(self.docTab)
        self.docnameEdit.setGeometry(QtCore.QRect(110, 540, 181, 33))
        self.docnameEdit.setObjectName(_fromUtf8("docnameEdit"))
        self.disEdit = QtGui.QLineEdit(self.docTab)
        self.disEdit.setGeometry(QtCore.QRect(110, 600, 181, 33))
        self.disEdit.setObjectName(_fromUtf8("disEdit"))
        self.doctextEdit = QtGui.QTextEdit(self.docTab)
        self.doctextEdit.setGeometry(QtCore.QRect(380, 470, 341, 91))
        self.doctextEdit.setObjectName(_fromUtf8("doctextEdit"))
        self.docidLabel = QtGui.QLabel(self.docTab)
        self.docidLabel.setGeometry(QtCore.QRect(30, 490, 65, 21))
        self.docidLabel.setObjectName(_fromUtf8("docidLabel"))
        self.docnameLabel = QtGui.QLabel(self.docTab)
        self.docnameLabel.setGeometry(QtCore.QRect(40, 550, 65, 21))
        self.docnameLabel.setObjectName(_fromUtf8("docnameLabel"))
        self.disLabel = QtGui.QLabel(self.docTab)
        self.disLabel.setGeometry(QtCore.QRect(30, 610, 65, 21))
        self.disLabel.setObjectName(_fromUtf8("disLabel"))
        self.docaddr = QtGui.QLabel(self.docTab)
        self.docaddr.setGeometry(QtCore.QRect(290, 480, 81, 21))
        self.docaddr.setObjectName(_fromUtf8("docaddr"))
        self.docBrowser = QtGui.QTextBrowser(self.docTab)
        self.docBrowser.setGeometry(QtCore.QRect(30, 660, 251, 71))
        self.docBrowser.setObjectName(_fromUtf8("docBrowser"))
        self.docinsert = QtGui.QPushButton(self.docTab)
        self.docinsert.setGeometry(QtCore.QRect(370, 600, 95, 31))
        self.docinsert.setObjectName(_fromUtf8("docinsert"))
        self.docdelete = QtGui.QPushButton(self.docTab)
        self.docdelete.setGeometry(QtCore.QRect(500, 600, 95, 31))
        self.docdelete.setObjectName(_fromUtf8("docdelete"))
        self.docupdate = QtGui.QPushButton(self.docTab)
        self.docupdate.setGeometry(QtCore.QRect(630, 600, 95, 31))
        self.docupdate.setObjectName(_fromUtf8("docupdate"))
        self.docsearch = QtGui.QPushButton(self.docTab)
        self.docsearch.setGeometry(QtCore.QRect(750, 600, 95, 31))
        self.docsearch.setObjectName(_fromUtf8("docsearch"))
        self.doclose = QtGui.QPushButton(self.docTab)
        self.doclose.setGeometry(QtCore.QRect(680, 690, 95, 31))
        self.doclose.setObjectName(_fromUtf8("doclose"))
        self.doclear = QtGui.QPushButton(self.docTab)
        self.doclear.setGeometry(QtCore.QRect(540, 690, 95, 31))
        self.doclear.setObjectName(_fromUtf8("doclear"))
        self.clea = QtGui.QPushButton(self.docTab)
        
        self.docviewbut = QtGui.QPushButton(self.docTab)
        self.docviewbut.setGeometry(QtCore.QRect(370, 650, 95, 31))
        self.docviewbut.setObjectName(_fromUtf8("docviewbut"))
        TabWidget.addTab(self.docTab, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Medical Store DBMS", None))
        TabWidget.setToolTip(_translate("TabWidget", "<html><head/><body><p></p></body></html>", None))
        self.pinsertButton.setText(_translate("TabWidget", "insert", None))
        self.pidlabel.setText(_translate("TabWidget", "Product ID", None))
        self.pnameLabel.setText(_translate("TabWidget", "Name", None))
        self.manuLabel.setText(_translate("TabWidget", "Manufacturer", None))
        self.cateLabel.setText(_translate("TabWidget", "Category", None))
        self.qtyLabel.setText(_translate("TabWidget", "Stock quanity", None))
        self.mrpLabel.setText(_translate("TabWidget", "MRP", None))
        self.pdeletebutton.setText(_translate("TabWidget", "delete", None))
        self.pclearbutton.setText(_translate("TabWidget", "clear", None))
        self.pview.setText(_translate("TabWidget", "view", None))
        self.pclosebutton.setText(_translate("TabWidget", "close", None))
        self.pclosebutton.clicked.connect(self.close)
        self.mfdLabel.setText(_translate("TabWidget", "<html><head/><body><p>Mfg Date</p></body></html>", None))
        self.exdLabel.setText(_translate("TabWidget", "Expiry Date", None))
        self.didLabel.setText(_translate("TabWidget", "Dealer Id", None))
        self.mcompLabel.setText(_translate("TabWidget", "MainComponent", None))
        self.pupdate.setText(_translate("TabWidget", "update", None))
        self.psearch.setText(_translate("TabWidget", "Search", None))
        TabWidget.setTabText(TabWidget.indexOf(self.prodTab), _translate("TabWidget", "Product Inventory", None))
        self.cnameLabel.setText(_translate("TabWidget", "Customer name", None))
        self.cidLabel.setText(_translate("TabWidget", "Customer ID", None))
        self.cnumLabel.setText(_translate("TabWidget", "Contact Number", None))
        self.hdoption.setText(_translate("TabWidget", "Home Delivery option", None))
        self.cinsertbutton.setText(_translate("TabWidget", "Insert", None))
        self.csearchbutton.setText(_translate("TabWidget", "Search", None))
        self.cpurchase.setText(_translate("TabWidget", "Purchases", None))
        self.cdeletebutton.setText(_translate("TabWidget", "Delete", None))
        self.cclosebutton.setText(_translate("TabWidget", "Close", None))
        self.cclosebutton.clicked.connect(self.close)
        self.cupdate.setText(_translate("TabWidget", "Update", None))
        self.caddrlabel.setText(_translate("TabWidget", "Address", None))
        self.cclear.setText(_translate("TabWidget", "Clear", None))
        TabWidget.setTabText(TabWidget.indexOf(self.cusTab), _translate("TabWidget", "Customer List", None))
        self.tcidLabel.setText(_translate("TabWidget", "Customer ID", None))
        self.tpidLabel.setText(_translate("TabWidget", "Product ID", None))
        self.tdidLabel.setText(_translate("TabWidget", "Doctor ID", None))
        self.tqtyLabel.setText(_translate("TabWidget", "Quantity", None))
        self.taddButton.setText(_translate("TabWidget", "Add to kart", None))
        self.tpurButton.setText(_translate("TabWidget", "Purchase", None))
        self.tcostLabel.setText(_translate("TabWidget", "Total Cost", None))
        self.tclose.setText(_translate("TabWidget", "Close", None))
        self.tclose.clicked.connect(self.close)
        self.tclear.setText(_translate("TabWidget", "Clear", None))
        TabWidget.setTabText(TabWidget.indexOf(self.transTab), _translate("TabWidget", "Transaction", None))
        self.ddidLabel.setText(_translate("TabWidget", "Dealer ID", None))
        self.dnameLabel.setText(_translate("TabWidget", "Name", None))
        self.dconumLabel.setText(_translate("TabWidget", "Contact Number", None))
        self.dpidLabel.setText(_translate("TabWidget", "Product ID", None))
        self.daddrLabel.setText(_translate("TabWidget", "Address", None))
        self.daddButon.setText(_translate("TabWidget", "add", None))
        self.dinsertButton.setText(_translate("TabWidget", "Insert", None))
        self.ddelete.setText(_translate("TabWidget", "Delete", None))
        self.dupdate.setText(_translate("TabWidget", "Update", None))
        self.dsearch.setText(_translate("TabWidget", "Search", None))
        self.dclose.setText(_translate("TabWidget", "Close", None))
        self.dclose.clicked.connect(self.close)
        self.dclear.setText(_translate("TabWidget", "Clear", None))
        TabWidget.setTabText(TabWidget.indexOf(self.dealTab), _translate("TabWidget", "Dealer List", None))
        self.docidLabel.setText(_translate("TabWidget", "Doctor ID", None))
        self.docnameLabel.setText(_translate("TabWidget", "Name", None))
        self.disLabel.setText(_translate("TabWidget", "Discipine", None))
        self.docaddr.setText(_translate("TabWidget", "Work place", None))
        self.docinsert.setText(_translate("TabWidget", "Insert", None))
        self.docinsert.clicked.connect(self.docInsert)
        self.docdelete.setText(_translate("TabWidget", "Delete", None))
        self.docdelete.clicked.connect(self.docDelete)
        self.docupdate.setText(_translate("TabWidget", "Update", None))
        self.docupdate.clicked.connect(self.docUpdate)
        self.docsearch.setText(_translate("TabWidget", "Search", None))
        self.docsearch.clicked.connect(self.docSearch)
        self.doclose.setText(_translate("TabWidget", "Close", None))
        self.doclose.clicked.connect(self.close)
        self.doclear.setText(_translate("TabWidget", "Clear", None))
        self.doclear.clicked.connect(self.doClear)
        self.docviewbut.setText(_translate("TabWidget", "View", None))
        self.docviewbut.clicked.connect(self.docview)
        TabWidget.setTabText(TabWidget.indexOf(self.docTab), _translate("TabWidget", "Doctor List", None))
        
    def close(self):
      self.db.close()
      sys.exit(app.exec_())     
        
    def selectionchange(self,i):     
      return self.cateBox.currentText() 
    def doClear(self):
      self.docnameEdit.setText('')
      self.docidEdit.setText('')
      self.doctextEdit.setText('')
      self.disEdit.setText('')
      
    def docview(self):
        self.docBrowser.setText('')
	self.db.docview()
        
        for n, a in enumerate(sorted(self.db.docdata)):
	  for m, b in enumerate(a):
	    itm = QtGui.QTableWidgetItem(str(b))	   
	    self.docTable.setItem(n,m,itm)       
        self.docTable.setHorizontalHeaderLabels(self.db.dochorHeaders)
        self.docTable.resizeColumnsToContents()
        self.docTable.resizeRowsToContents()
      
    
        
    def docsearchnameview(self):
        self.docBrowser.setText('')
	self.db.docSearchname(self.docnameEdit.text())        
        for n, a in enumerate(sorted(self.db.docdata)):
	  for m, b in enumerate(a):
	    itm = QtGui.QTableWidgetItem(str(b))	   
	    self.docTable.setItem(n,m,itm)       
        self.docTable.setHorizontalHeaderLabels(self.db.dochorHeaders)
        self.docTable.resizeColumnsToContents()
        self.docTable.resizeRowsToContents()  
    def docsearchidview(self):
        self.docBrowser.setText('')
	self.db.docSearchid(self.docidEdit.text())        
        for n, a in enumerate(sorted(self.db.docdata)):
	  for m, b in enumerate(a):
	    itm = QtGui.QTableWidgetItem(str(b))	   
	    self.docTable.setItem(n,m,itm)       
        self.docTable.setHorizontalHeaderLabels(self.db.dochorHeaders)
        self.docTable.resizeColumnsToContents()
        self.docTable.resizeRowsToContents()  
    def docsearchdisview(self):
        self.docBrowser.setText('')
	self.db.docSearchdis(self.disEdit.text())        
        for n, a in enumerate(sorted(self.db.docdata)):
	  for m, b in enumerate(a):
	    itm = QtGui.QTableWidgetItem(str(b))	   
	    self.docTable.setItem(n,m,itm)       
        self.docTable.setHorizontalHeaderLabels(self.db.dochorHeaders)
        self.docTable.resizeColumnsToContents()
        self.docTable.resizeRowsToContents()  
    def  docInsert(self):
      if self.docnameEdit.text() == '' or self.docidEdit.text() == '' or self.doctextEdit.toPlainText() == '' or self.disEdit.text() == '' :
	 self.docBrowser.setText( 'Please fill in all the fields')	
	 return
      self.db.docInsert( self.docnameEdit.text(), self.docidEdit.text(), self.doctextEdit.toPlainText(), self.disEdit.text())
      self.docBrowser.setText(self.db.docinsertRes)
      self.doClear
      self.docview()
      
    def docSearch(self):
      if self.docidEdit.text() == '' and self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() == '' :
	 self.docBrowser.setText( 'Please fill in any one  field ')	
	 return
      if self.docidEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() == '' :
	 self.doClear
	 self.docsearchnameview()
      elif self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() == '' :
	self.doClear
	self.docsearchidview()
      elif self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.docidEdit.text() == '' :
	self.doClear
	self.docsearchdisview()
    def docDelete(self):
      if self.docidEdit.text() == '':
	self.docBrowser.setText( 'Please fill in  Id  field ')	
	return
      self.db.docDelete(self.docidEdit.text())
      self.docBrowser.setText(self.db.docdeleteRes)
      self.doClear
      self.docview()
      
    def docUpdate(self):
      if self.docidEdit.text() == '' or self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() == ''  :
	 self.docBrowser.setText( 'Please fill in id field and any one of the other fields ')	
	 return
      if self.docnameEdit.text() != '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() == ''  :
	 self.db.docUpdatename(self.docidEdit.text(),self.docnameEdit.text());
	 self.docBrowser.setText(self.db.docUpdatenameRes)
         self.doClear
         self.docview()
      elif   self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() != '' and self.disEdit.text() == ''  :
	 
	 self.db.docUpdateaddr(self.docidEdit.text(),self.doctextEdit.toPlainText());
	 self.docBrowser.setText(self.db.docUpdateaddrRes)
         self.doClear
         self.docview()
      elif self.docnameEdit.text() == '' and self.doctextEdit.toPlainText() == '' and self.disEdit.text() != ''  :
	
	 self.db.docUpdatedis(self.docidEdit.text(),self.disEdit.text());
	 self.docBrowser.setText(self.db.docUpdatedisRes)
         self.doClear
         self.docview()
	
class SQL(object):
  def __init__(self):
    self.cxn = MySQLdb.connect('localhost','root','dhureenmysql','mydatabase2')
    self.cur = self.cxn.cursor()
   
  
  def close(self):
    self.cur.close()
    self.cxn.commit()
    self.cxn.close()
  def docUpdatename(self,docid,name): 
      try:
	  self.cur.execute("update doctor set name = '%s' where id = '%d'" % (name,int(docid)) )
      except DB_EXC.Error, e :
        self.docUpdatenameRes = "update error"+str(e)
      except ValueError, e :
	self.docUpdatenameRes = 'update error'
      else:
        self.docUpdatenameRes = "record updated"
        
  def docUpdateaddr(self,docid,addr): 
      try:
	  self.cur.execute("update doctor set addr = '%s' where id = '%d'" % (addr,int(docid)) )
      except DB_EXC.Error, e :
        self.docUpdateaddrRes = "update error"+str(e)
      except ValueError, e :
	self.docUpdateaddrRes = 'update error'
      else:
        self.docUpdateaddrRes = "record updated"
        
  def docUpdatedis(self,docid,dis): 
      try:
	  self.cur.execute("update doctor set dis = '%s' where id = '%d'" % (dis,int(docid)) )
      except DB_EXC.Error, e :
        self.docUpdatedisRes = "update error"+str(e)
      except ValueError, e :
	self.docUpdatedisRes = 'update error'
      else:
        self.docUpdatedisRes = "record updated"  
        
  def docDelete(self,docid):
      try:
	  self.cur.execute("delete from doctor where id = '%d'" % (int(docid)) )
      except DB_EXC.Error, e :
        self.dpcdeleteRes = "delete error"+str(e)
      except ValueError, e :
	self.docdeleteRes = 'delete error'
      else:
        self.docdeleteRes = "record deleted"
    
    
      
  def docSearchname(self,name):
      try:
	  self.cur.execute("select * from doctor where name = '%s'" % (name) )
      except DB_EXC.Error, e :
        self.docdata = None
      else:
        self.docdata = self.cur.fetchall()
        self.dochorHeaders = ['ID','Name','Discipline','Workplace']
  def docSearchid(self,id):
      try:
	  self.cur.execute("select * from doctor where id = '%d'" % (int(id)) )
      except DB_EXC.Error, e :
        self.docdata = None
      else:
        self.docdata = self.cur.fetchall()
        self.dochorHeaders = ['ID','Name','Discipline','Workplace']
  def docSearchdis(self,dis):
      try:
	  self.cur.execute("select * from doctor where dis = '%s'" % (dis) )
      except DB_EXC.Error, e :
        self.docdata = None
      else:
        self.docdata = self.cur.fetchall()
        self.dochorHeaders = ['ID','Name','Discipline','Workplace']
    
  def docInsert(self,name,docid,addr,dis):
	try:
	  self.cur.execute("insert into doctor values('%d','%s','%s','%s')" % (int(docid),name,dis,addr))			
	except DB_EXC.Error, e : 
	  self.docinsertRes = 'Insert error : '+ str(e)
	  print e
	except ValueError, e :
	  self.docinsertRes = 'Insert error' 
	else:
	  self.docinsertRes = 'New record inserted into DB'
  def docview(self):
      try:
	  self.cur.execute("select * from doctor") 
      except DB_EXC.Error, e :
        self.docdata = None
      else:
        self.docdata = self.cur.fetchall()
        self.dochorHeaders = ['ID','Name','Discipline','Workplace']
        
  def insert (self,pid,name,comp,cate,stk,mrp,mfg,exp,did,mcomp):  
    
    try: 
      sid=1   
      #self.cur.execute("insert into stockArrival(sid,pid,did,Date,Time,mfd,exd,qty)values('%d','%d','%d','%s','%s','%s','%s','%d')"%(int(sid),int(pid),int(did),sysDate(),sysTime(),mfg,exp,int(stk)))
      self.cur.execute("SELECT stk FROM  product where pid = '%d'")
      list = self.cur.fetchall
      for a in list:
	print a
      if list == None:
	 stk1 = 0
      else:
	 stk1 = int(list[0])
      if stk1 > 0:
	stk = int(stk) + stk1
      self.cur.execute("INSERT INTO product(pid,name,cate,comp,stk,mrp) VALUES('%d','%s','%s','%s','%d','%f')" % (int(pid),name,cate,comp,int(stk),float(mrp)))
     
    except DB_EXC.Error, e : 
      self.insertRes = 'Insert error : '+ str(e)
      print e
    except ValueError, e :
      self.insertRes = 'Insert error' 
    else:
      self.insertRes = 'New record inserted into DB'
   
  def view(self):
    try:
      self.cur.execute('SELECT * FROM  product')
    except DB_EXC.Error, e :
      Ui_TabWidget.data = None
    else:
      Ui_TabWidget.data = self.cur.fetchall()
      Ui_TabWidget.horHeaders = ['PID','Name','Category','Manufacturer','Quantity','MRP']
if __name__ == "__main__":
   import sys
   app = QtGui.QApplication(sys.argv)
   Dialog = QtGui.QTabWidget()
   ui = Ui_TabWidget()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())
