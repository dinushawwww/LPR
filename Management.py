# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Management.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManagementWIndow(object):
    def setupUi(self, ManagementWIndow):
        ManagementWIndow.setObjectName("ManagementWIndow")
        ManagementWIndow.resize(981, 815)
        self.centralwidget = QtWidgets.QWidget(ManagementWIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.MgtTab = QtWidgets.QTabWidget(self.centralwidget)
        self.MgtTab.setGeometry(QtCore.QRect(0, 0, 1251, 811))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MgtTab.setFont(font)
        self.MgtTab.setObjectName("MgtTab")
        self.TabUsers = QtWidgets.QWidget()
        self.TabUsers.setObjectName("TabUsers")
        self.FmCusers = QtWidgets.QFrame(self.TabUsers)
        self.FmCusers.setGeometry(QtCore.QRect(10, 30, 441, 271))
        self.FmCusers.setFrameShape(QtWidgets.QFrame.Box)
        self.FmCusers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FmCusers.setLineWidth(2)
        self.FmCusers.setObjectName("FmCusers")
        self.LblUname = QtWidgets.QLabel(self.FmCusers)
        self.LblUname.setGeometry(QtCore.QRect(10, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblUname.setFont(font)
        self.LblUname.setObjectName("LblUname")
        self.LblPasswd = QtWidgets.QLabel(self.FmCusers)
        self.LblPasswd.setGeometry(QtCore.QRect(10, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblPasswd.setFont(font)
        self.LblPasswd.setObjectName("LblPasswd")
        self.LblRpasswd = QtWidgets.QLabel(self.FmCusers)
        self.LblRpasswd.setGeometry(QtCore.QRect(10, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblRpasswd.setFont(font)
        self.LblRpasswd.setObjectName("LblRpasswd")
        self.PbAdd = QtWidgets.QPushButton(self.FmCusers)
        self.PbAdd.setGeometry(QtCore.QRect(350, 220, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PbAdd.setFont(font)
        self.PbAdd.setObjectName("PbAdd")
        self.LeUname = QtWidgets.QLineEdit(self.FmCusers)
        self.LeUname.setGeometry(QtCore.QRect(130, 20, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeUname.setFont(font)
        self.LeUname.setObjectName("LeUname")
        self.LePasswd = QtWidgets.QLineEdit(self.FmCusers)
        self.LePasswd.setGeometry(QtCore.QRect(130, 140, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LePasswd.setFont(font)
        self.LePasswd.setObjectName("LePasswd")
        self.LeRpasswd = QtWidgets.QLineEdit(self.FmCusers)
        self.LeRpasswd.setGeometry(QtCore.QRect(130, 180, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeRpasswd.setFont(font)
        self.LeRpasswd.setObjectName("LeRpasswd")
        self.LblDesc = QtWidgets.QLabel(self.FmCusers)
        self.LblDesc.setGeometry(QtCore.QRect(10, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblDesc.setFont(font)
        self.LblDesc.setObjectName("LblDesc")
        self.LeUname_4 = QtWidgets.QLineEdit(self.FmCusers)
        self.LeUname_4.setGeometry(QtCore.QRect(130, 60, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeUname_4.setFont(font)
        self.LeUname_4.setObjectName("LeUname_4")
        self.LblMessage = QtWidgets.QLabel(self.FmCusers)
        self.LblMessage.setGeometry(QtCore.QRect(130, 50, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblMessage.setFont(font)
        self.LblMessage.setText("")
        self.LblMessage.setObjectName("LblMessage")
        self.LblRole = QtWidgets.QLabel(self.FmCusers)
        self.LblRole.setGeometry(QtCore.QRect(10, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblRole.setFont(font)
        self.LblRole.setObjectName("LblRole")
        self.CmbRole = QtWidgets.QComboBox(self.FmCusers)
        self.CmbRole.setGeometry(QtCore.QRect(130, 100, 171, 22))
        self.CmbRole.setToolTip("")
        self.CmbRole.setCurrentText("")
        self.CmbRole.setObjectName("CmbRole")
        self.LblUcreate = QtWidgets.QLabel(self.TabUsers)
        self.LblUcreate.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblUcreate.setFont(font)
        self.LblUcreate.setObjectName("LblUcreate")
        self.LblCPasswd = QtWidgets.QLabel(self.TabUsers)
        self.LblCPasswd.setGeometry(QtCore.QRect(510, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblCPasswd.setFont(font)
        self.LblCPasswd.setObjectName("LblCPasswd")
        self.FmMusers = QtWidgets.QFrame(self.TabUsers)
        self.FmMusers.setGeometry(QtCore.QRect(510, 30, 441, 231))
        self.FmMusers.setFrameShape(QtWidgets.QFrame.Box)
        self.FmMusers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FmMusers.setLineWidth(2)
        self.FmMusers.setObjectName("FmMusers")
        self.CmbUsers = QtWidgets.QComboBox(self.FmMusers)
        self.CmbUsers.setGeometry(QtCore.QRect(100, 20, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CmbUsers.setFont(font)
        self.CmbUsers.setObjectName("CmbUsers")
        self.LblUnameM = QtWidgets.QLabel(self.FmMusers)
        self.LblUnameM.setGeometry(QtCore.QRect(10, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblUnameM.setFont(font)
        self.LblUnameM.setObjectName("LblUnameM")
        self.LblDescM = QtWidgets.QLabel(self.FmMusers)
        self.LblDescM.setGeometry(QtCore.QRect(10, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblDescM.setFont(font)
        self.LblDescM.setObjectName("LblDescM")
        self.LeDescM = QtWidgets.QLineEdit(self.FmMusers)
        self.LeDescM.setGeometry(QtCore.QRect(100, 60, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeDescM.setFont(font)
        self.LeDescM.setObjectName("LeDescM")
        self.LblPasswdM = QtWidgets.QLabel(self.FmMusers)
        self.LblPasswdM.setGeometry(QtCore.QRect(10, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblPasswdM.setFont(font)
        self.LblPasswdM.setObjectName("LblPasswdM")
        self.LePasswdM = QtWidgets.QLineEdit(self.FmMusers)
        self.LePasswdM.setGeometry(QtCore.QRect(100, 100, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LePasswdM.setFont(font)
        self.LePasswdM.setObjectName("LePasswdM")
        self.LblRpasswdM = QtWidgets.QLabel(self.FmMusers)
        self.LblRpasswdM.setGeometry(QtCore.QRect(10, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblRpasswdM.setFont(font)
        self.LblRpasswdM.setObjectName("LblRpasswdM")
        self.LeRpasswdM = QtWidgets.QLineEdit(self.FmMusers)
        self.LeRpasswdM.setGeometry(QtCore.QRect(100, 140, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeRpasswdM.setFont(font)
        self.LeRpasswdM.setObjectName("LeRpasswdM")
        self.PbUpdate = QtWidgets.QPushButton(self.FmMusers)
        self.PbUpdate.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.PbUpdate.setObjectName("PbUpdate")
        self.LblDelete = QtWidgets.QLabel(self.TabUsers)
        self.LblDelete.setGeometry(QtCore.QRect(10, 340, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LblDelete.setFont(font)
        self.LblDelete.setObjectName("LblDelete")
        self.FmRusers = QtWidgets.QFrame(self.TabUsers)
        self.FmRusers.setGeometry(QtCore.QRect(10, 360, 391, 131))
        self.FmRusers.setFrameShape(QtWidgets.QFrame.Box)
        self.FmRusers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FmRusers.setLineWidth(2)
        self.FmRusers.setObjectName("FmRusers")
        self.lblRusers = QtWidgets.QLabel(self.FmRusers)
        self.lblRusers.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblRusers.setFont(font)
        self.lblRusers.setObjectName("lblRusers")
        self.CmbRusers = QtWidgets.QComboBox(self.FmRusers)
        self.CmbRusers.setGeometry(QtCore.QRect(90, 20, 181, 22))
        self.CmbRusers.setObjectName("CmbRusers")
        self.PbDelete = QtWidgets.QPushButton(self.FmRusers)
        self.PbDelete.setGeometry(QtCore.QRect(300, 90, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PbDelete.setFont(font)
        self.PbDelete.setObjectName("PbDelete")
        self.MgtTab.addTab(self.TabUsers, "")
        self.TabAddLayout = QtWidgets.QWidget()
        self.TabAddLayout.setObjectName("TabAddLayout")
        self.CmbUserAl = QtWidgets.QComboBox(self.TabAddLayout)
        self.CmbUserAl.setGeometry(QtCore.QRect(100, 20, 271, 22))
        self.CmbUserAl.setObjectName("CmbUserAl")
        self.LblAlUname = QtWidgets.QLabel(self.TabAddLayout)
        self.LblAlUname.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.LblAlUname.setObjectName("LblAlUname")
        self.LblLayout = QtWidgets.QLabel(self.TabAddLayout)
        self.LblLayout.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.LblLayout.setObjectName("LblLayout")
        self.CmbLayout = QtWidgets.QComboBox(self.TabAddLayout)
        self.CmbLayout.setGeometry(QtCore.QRect(100, 70, 111, 22))
        self.CmbLayout.setObjectName("CmbLayout")
        self.LblPreview = QtWidgets.QLabel(self.TabAddLayout)
        self.LblPreview.setGeometry(QtCore.QRect(10, 120, 71, 20))
        self.LblPreview.setObjectName("LblPreview")
        self.PbSetLayout = QtWidgets.QPushButton(self.TabAddLayout)
        self.PbSetLayout.setGeometry(QtCore.QRect(870, 720, 75, 23))
        self.PbSetLayout.setObjectName("PbSetLayout")
        self.FmPreImageAdd = QtWidgets.QFrame(self.TabAddLayout)
        self.FmPreImageAdd.setGeometry(QtCore.QRect(30, 150, 911, 551))
        self.FmPreImageAdd.setFrameShape(QtWidgets.QFrame.Box)
        self.FmPreImageAdd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FmPreImageAdd.setLineWidth(2)
        self.FmPreImageAdd.setObjectName("FmPreImageAdd")
        self.LblPreImageAdd = QtWidgets.QLabel(self.FmPreImageAdd)
        self.LblPreImageAdd.setGeometry(QtCore.QRect(10, 10, 891, 541))
        self.LblPreImageAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.LblPreImageAdd.setObjectName("LblPreImageAdd")
        self.MgtTab.addTab(self.TabAddLayout, "")
        self.TabConfigLayout = QtWidgets.QWidget()
        self.TabConfigLayout.setObjectName("TabConfigLayout")
        self.LblUnameCLay = QtWidgets.QLabel(self.TabConfigLayout)
        self.LblUnameCLay.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.LblUnameCLay.setObjectName("LblUnameCLay")
        self.CmbUnameClay = QtWidgets.QComboBox(self.TabConfigLayout)
        self.CmbUnameClay.setGeometry(QtCore.QRect(100, 20, 181, 22))
        self.CmbUnameClay.setObjectName("CmbUnameClay")
        self.LblLoc = QtWidgets.QLabel(self.TabConfigLayout)
        self.LblLoc.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.LblLoc.setObjectName("LblLoc")
        self.CmbLocation = QtWidgets.QComboBox(self.TabConfigLayout)
        self.CmbLocation.setGeometry(QtCore.QRect(100, 70, 131, 22))
        self.CmbLocation.setObjectName("CmbLocation")
        self.LblCamera = QtWidgets.QLabel(self.TabConfigLayout)
        self.LblCamera.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.LblCamera.setObjectName("LblCamera")
        self.CmbCamera = QtWidgets.QComboBox(self.TabConfigLayout)
        self.CmbCamera.setGeometry(QtCore.QRect(100, 120, 131, 22))
        self.CmbCamera.setObjectName("CmbCamera")
        self.PbSetConfigLay = QtWidgets.QPushButton(self.TabConfigLayout)
        self.PbSetConfigLay.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.PbSetConfigLay.setObjectName("PbSetConfigLay")
        self.LblPreLayCon = QtWidgets.QLabel(self.TabConfigLayout)
        self.LblPreLayCon.setGeometry(QtCore.QRect(10, 220, 71, 16))
        self.LblPreLayCon.setObjectName("LblPreLayCon")
        self.FmPreviewConf = QtWidgets.QFrame(self.TabConfigLayout)
        self.FmPreviewConf.setGeometry(QtCore.QRect(20, 260, 931, 461))
        self.FmPreviewConf.setFrameShape(QtWidgets.QFrame.Box)
        self.FmPreviewConf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FmPreviewConf.setLineWidth(2)
        self.FmPreviewConf.setObjectName("FmPreviewConf")
        self.LblImagePreConfig = QtWidgets.QLabel(self.FmPreviewConf)
        self.LblImagePreConfig.setGeometry(QtCore.QRect(0, 0, 931, 461))
        self.LblImagePreConfig.setAlignment(QtCore.Qt.AlignCenter)
        self.LblImagePreConfig.setObjectName("LblImagePreConfig")
        self.MgtTab.addTab(self.TabConfigLayout, "")
        ManagementWIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagementWIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName("menubar")
        ManagementWIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagementWIndow)
        self.statusbar.setObjectName("statusbar")
        ManagementWIndow.setStatusBar(self.statusbar)

        self.retranslateUi(ManagementWIndow)
        self.MgtTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ManagementWIndow)

    def retranslateUi(self, ManagementWIndow):
        _translate = QtCore.QCoreApplication.translate
        ManagementWIndow.setWindowTitle(_translate("ManagementWIndow", "MainWindow"))
        self.LblUname.setText(_translate("ManagementWIndow", "User name:"))
        self.LblPasswd.setText(_translate("ManagementWIndow", "Password:"))
        self.LblRpasswd.setText(_translate("ManagementWIndow", "Re type password:"))
        self.PbAdd.setText(_translate("ManagementWIndow", "Add"))
        self.LblDesc.setText(_translate("ManagementWIndow", "Description:"))
        self.LblRole.setText(_translate("ManagementWIndow", "Password:"))
        self.LblUcreate.setText(_translate("ManagementWIndow", "Create User(s):"))
        self.LblCPasswd.setText(_translate("ManagementWIndow", "Modify User:"))
        self.LblUnameM.setText(_translate("ManagementWIndow", "User name:"))
        self.LblDescM.setText(_translate("ManagementWIndow", "Description:"))
        self.LblPasswdM.setText(_translate("ManagementWIndow", "Password:"))
        self.LblRpasswdM.setText(_translate("ManagementWIndow", "Password:"))
        self.PbUpdate.setText(_translate("ManagementWIndow", "Update"))
        self.LblDelete.setText(_translate("ManagementWIndow", "Remove User(s):"))
        self.lblRusers.setText(_translate("ManagementWIndow", "User name:"))
        self.PbDelete.setText(_translate("ManagementWIndow", "Remove"))
        self.MgtTab.setTabText(self.MgtTab.indexOf(self.TabUsers), _translate("ManagementWIndow", "Users(s)"))
        self.LblAlUname.setText(_translate("ManagementWIndow", "User name:"))
        self.LblLayout.setText(_translate("ManagementWIndow", "Layout:"))
        self.LblPreview.setText(_translate("ManagementWIndow", "Preview:"))
        self.PbSetLayout.setText(_translate("ManagementWIndow", "Set"))
        self.LblPreImageAdd.setText(_translate("ManagementWIndow", "PreImage"))
        self.MgtTab.setTabText(self.MgtTab.indexOf(self.TabAddLayout), _translate("ManagementWIndow", "Add Layouts"))
        self.LblUnameCLay.setText(_translate("ManagementWIndow", "User name:"))
        self.LblLoc.setText(_translate("ManagementWIndow", "Location:"))
        self.LblCamera.setText(_translate("ManagementWIndow", "Camera:"))
        self.PbSetConfigLay.setText(_translate("ManagementWIndow", "Set"))
        self.LblPreLayCon.setText(_translate("ManagementWIndow", "Preview:"))
        self.LblImagePreConfig.setText(_translate("ManagementWIndow", "TextLabel"))
        self.MgtTab.setTabText(self.MgtTab.indexOf(self.TabConfigLayout), _translate("ManagementWIndow", "Configure Layout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementWIndow = QtWidgets.QMainWindow()
    ui = Ui_ManagementWIndow()
    ui.setupUi(ManagementWIndow)
    ManagementWIndow.show()
    sys.exit(app.exec_())