# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical.ui'
#
# Created: Thu Nov 12 17:03:55 2015
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
        self.db = SQL()
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(882, 771)
        TabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.data = []
        self.horHeaders = []
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(600, 370, 95, 31))
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 380, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 430, 181, 33))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 490, 181, 33))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 370, 121, 33))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 430, 121, 33))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 490, 121, 33))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 440, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 500, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(370, 380, 65, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(340, 440, 101, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(400, 500, 41, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(110, 370, 131, 33))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 410, 95, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 450, 95, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 490, 95, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 530, 95, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 550, 110, 33))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 550, 110, 33))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 540, 71, 51))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(350, 560, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 791, 321))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(100)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))        
                       
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(40, 660, 721, 81))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))   
        self.lineEdit_8 = QtGui.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 610, 181, 33))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 620, 65, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 610, 141, 33))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(320, 620, 111, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        TabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "Medical Store DBMS", None))
        TabWidget.setToolTip(_translate("TabWidget", "<html><head/><body><p>efefef</p></body></html>", None))
        self.pushButton.setText(_translate("TabWidget", "insert", None))
        self.pushButton.clicked.connect(self.insert)
        self.label.setText(_translate("TabWidget", "PID", None))
        self.label_2.setText(_translate("TabWidget", "Name", None))
        self.label_3.setText(_translate("TabWidget", "Manufacturer", None))
        self.label_4.setText(_translate("TabWidget", "Category", None))
        self.label_5.setText(_translate("TabWidget", "Stock quanity", None))
        self.label_6.setText(_translate("TabWidget", "MRP", None))
        self.pushButton_2.setText(_translate("TabWidget", "delete", None))
        self.pushButton_3.setText(_translate("TabWidget", "clear", None))
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.setText(_translate("TabWidget", "view", None))
        self.pushButton_4.clicked.connect(self.view)
        self.pushButton_5.setText(_translate("TabWidget", "close", None))
        self.pushButton_5.clicked.connect(self.close)
        self.label_7.setText(_translate("TabWidget", "<html><head/><body><p>Mfg Date</p></body></html>", None))
        self.label_8.setText(_translate("TabWidget", "Expiry Date", None))
        self.label_9.setText(_translate("TabWidget", "Dealer Id", None))
        self.label_10.setText(_translate("TabWidget", "MainComponent", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Product Inventory", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Customer List", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Purchase Bill", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Home Delivery", None))
    
    def clear(self):
       self.textBrowser.setText('')
       self.fieldClear()
      
    def close(self):
      self.db.close()
      sys.exit(app.exec_())
      
        
    def insert(self): 
	self.textBrowser.setText('')
	self.pid = self.lineEdit.text()
	self.name=self.lineEdit_2.text()
	self.comp=self.lineEdit_3.text()
	self.cate=self.lineEdit_4.text()
	self.stk=self.lineEdit_5.text()
	self.mrp=self.lineEdit_6.text()
	self.mfd=self.lineEdit_9.text()
	self.exd=self.lineEdit_10.text()
	self.did=self.lineEdit_8.text()
	self.mcomp=self.lineEdit_7.text()
	
	if self.pid == '' or self.name== '' or self.comp== '' or self.cate=='' or self.stk== '' or self.mrp== '' or self.mfd==''or self.exd ==''or self.mcomp=='':
	    self.textBrowser.setText( 'Please fill in all the fields')
	    return
	
        self.db.insert(self.pid , self.name,self.comp, self.cate,self.stk, self.mrp, self.mfd,self.exd,self.did, self.mcomp)
        
        self.textBrowser.setText(self.db.insertRes)
	self.fieldClear()
	self.view()
	
    def view(self):
	self.textBrowser.setText('')
	self.db.view()
        
        for n, a in enumerate(sorted(Ui_TabWidget.data)):
	  for m, b in enumerate(a):
	    itm = QtGui.QTableWidgetItem(str(b))	   
	    self.tableWidget.setItem(n,m,itm)       
        self.tableWidget.setHorizontalHeaderLabels(Ui_TabWidget.horHeaders)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    def fieldClear(self):  
	self.lineEdit.setText('')
	self.lineEdit_2.setText('')
	self.lineEdit_3.setText('')
	self.lineEdit_4.setText('')    
	self.lineEdit_5.setText('')
	self.lineEdit_6.setText('')
	self.lineEdit_7.setText('')
	self.lineEdit_8.setText('')
	self.lineEdit_9.setText('')
	self.lineEdit_10.setText('')
	 
    
class SQL(object):
  def __init__(self):
    self.cxn = MySQLdb.connect('localhost','root','dhureenmysql','mydatabase2')
    self.cur = self.cxn.cursor()
    try:
      self.cur.execute('CREATE TABLE product(pid int primary key,name varchar(10),cate varchar(10),comp varchar(10),stk int, mrp real)')
    except DB_EXC.OperationalError, e:
      self.createRes = 'Stock DB present'
    else:
      self.createRes = 'Stock DB not present, new DB created'
  
  def close(self):
    self.cur.close()
    self.cxn.commit()
    self.cxn.close()
    
  def checkStock(self):
    try:
      self.cur.execute("SELECT sid FROM stockArrival")
      
    except DB_EXC.Error, e :
      Ui_TabWidget.data = None 
      Ui_TabWidget.horHeaders = None 
    else:
      t = self.cur.fetchall()
      print t
      if t == []:
	return 0
	
      return int(t[-1]) + 1
      
      
  
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
      #print Ui_TabWidget.data
    
  
  def edit(self,Id,name,typ,manu,mdate,edate,qty,cost):
    try:
      if name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ!= '':
	self.cur.execute("UPDATE product SET name = '%s' , typ = '%s', manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,typ,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost== '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty== ''and cost== '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s' where Id = '%d'"  %(name,manu,mdate,edate,int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate== '' and qty== ''and cost== '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s' where Id = '%d'"  %(name,manu,mdate,int(Id)))
      elif name != '' and manu !=''and mdate==''and edate== '' and qty== ''and cost== '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s' where Id = '%d'"  %(name,manu,int(Id)))
      elif name != '' and manu ==''and mdate==''and edate== '' and qty== ''and cost== '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s'  where Id = '%d'"  %(name,int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost== '' and typ!= '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty== ''and cost== '' and typ!= '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
      elif name != '' and manu !=''and mdate!=''and edate!= '' and qty!= ''and cost!= '' and typ== '':
	self.cur.execute("UPDATE product SET name = '%s' ,  manu = '%s', mdate = '%s',edate = '%s',qty = '%d',cost ='%f' where Id = '%d'"  %(name,manu,mdate,edate,int(qty),float(cost),int(Id)))
	
	
    except DB_EXC.Error, e :
      self.editRes = 'Edit error : ' + str(e)
    else:
      self.editRes = 'Edit successful on record with Id = ' + Id        
if __name__ == "__main__":
   import sys
   app = QtGui.QApplication(sys.argv)
   Dialog = QtGui.QTabWidget()
   ui = Ui_TabWidget()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())
