from PyQt5 import QtCore, QtGui, QtWidgets
import json
from fpkmfetcher.processing.data_founder import GDCServer
from fpkmfetcher.help_gui import HelpWindow
import sys
import os


class UiMainWindow:
    def __init__(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(475, 379)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(457, 320))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 455, 318))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName("formLayout")

        # Header
        self.label_header = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.label_header
        )

        # label cancer type
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        # combo Box to check cancer type
        self.comboBox_cancer_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_cancer_type.setObjectName("comboBox_cancer_type")
        self.comboBox_cancer_type.addItems(["breast", "lung"])
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.comboBox_cancer_type
        )

        # label namber of files
        self.label_nuber_files = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nuber_files.setFont(font)
        self.label_nuber_files.setObjectName("label_nuber_files")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_nuber_files
        )

        # edit number of files to download
        self.lineEdit_number = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_number
        )

        # label for choose stages of tumor
        self.label_stages = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_stages.setFont(font)
        self.label_stages.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stages.setObjectName("label_stages")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.label_stages
        )

        # check box for stage1
        self.checkBox_stage1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_stage1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_stage1.setAutoFillBackground(False)
        self.checkBox_stage1.setChecked(True)
        self.checkBox_stage1.setObjectName("checkBox_stage1")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.checkBox_stage1
        )

        # check box for stage3
        self.checkBox_stage3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_stage3.setChecked(True)
        self.checkBox_stage3.setObjectName("checkBox_stage3")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.checkBox_stage3
        )

        # check box for stage2
        self.checkBox_stage2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_stage2.setChecked(True)
        self.checkBox_stage2.setObjectName("checkBox_stage2")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.checkBox_stage2
        )

        # check box for stage4
        self.checkBox_stage4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_stage4.setChecked(True)
        self.checkBox_stage4.setObjectName("checkBox_stage4")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.checkBox_stage4
        )

        # just line
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.line)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_2)

        # label for dir
        self.label_dir = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_dir)

        # type directory
        self.lineEdit_directory = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_directory.setObjectName("lineEdit_directory")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_directory
        )

        # choose directory
        self.pushButton_setDir = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_setDir.setObjectName("pushButton_setDir")
        self.pushButton_setDir.clicked.connect(self.set_dir)
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.pushButton_setDir
        )

        # checkbox if joining files
        self.checkBox_join_files = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_join_files.setFont(font)
        self.checkBox_join_files.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_join_files.setAutoFillBackground(False)
        self.checkBox_join_files.setChecked(True)
        self.checkBox_join_files.setObjectName("checkBox_join_files")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.checkBox_join_files
        )

        # joining file approach
        self.comboBox_join = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_join.setObjectName("comboBox_join")
        self.comboBox_join.addItems(["Merge", "Append"])
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.comboBox_join
        )

        self.justlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.justlabel.setText("")
        self.justlabel.setObjectName("justlabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.justlabel)

        # Execution button:
        self.pushButton_download = QtWidgets.QPushButton(
            self.scrollAreaWidgetContents_2
        )
        self.pushButton_download.setObjectName("pushButton_download")
        self.pushButton_download.clicked.connect(self.download_data)
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.pushButton_download
        )

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(main_window)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.show_help)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FPKM file downloader"))
        self.label_header.setText(_translate("MainWindow", "FPKM file downloader"))
        self.label.setText(_translate("MainWindow", "Cancer type:"))
        self.label_nuber_files.setText(
            _translate("MainWindow", "Number of files to download:")
        )
        self.lineEdit_number.setText(_translate("MainWindow", "15"))
        self.label_stages.setText(_translate("MainWindow", "Sages to download"))
        self.checkBox_stage1.setText(_translate("MainWindow", "Stage 1"))
        self.checkBox_stage3.setText(_translate("MainWindow", "Stage 3"))
        self.checkBox_stage2.setText(_translate("MainWindow", "Stage 2"))
        self.checkBox_stage4.setText(_translate("MainWindow", "Stage 4"))
        self.label_dir.setText(_translate("MainWindow", "Directory to save files"))
        self.lineEdit_directory.setText(
            _translate("MainWindow", os.path.expanduser("~"))
        )
        self.checkBox_join_files.setText(_translate("MainWindow", "Join files"))
        self.pushButton_download.setText(_translate("MainWindow", "Start downloading"))
        self.pushButton_setDir.setText(_translate("MainWindow", "Choose directory"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def set_dir(self):
        file_dir = str(QtWidgets.QFileDialog.getExistingDirectory())
        print(file_dir)
        self.lineEdit_directory.setText(file_dir)

    def download_data(self):
        self.number_to_download = self.lineEdit_number.text()
        self.cancer_type = self.comboBox_cancer_type.currentText()
        self.directory_to_save_files = self.lineEdit_directory.text()
        self.join_files = self.checkBox_join_files.isChecked()
        self.stage1 = self.checkBox_stage1.isChecked()
        self.stage2 = self.checkBox_stage2.isChecked()
        self.stage3 = self.checkBox_stage3.isChecked()
        self.stage4 = self.checkBox_stage4.isChecked()
        self.join_method = self.comboBox_join.currentText()

        self.create_and_save_configurations()

    def create_and_save_configurations(self):
        data = {}
        data["cases_endpt"] = "https://api.gdc.cancer.gov/cases"
        data["data_endpt"] = "https://api.gdc.cancer.gov/data/"
        data["primary_site"] = self.cancer_type
        data["expand"] = ["diagnoses", "files"]
        data["format"] = "JSON"
        data["size"] = self.number_to_download
        data["dir"] = self.directory_to_save_files
        data["tumor_stages"] = {}
        if self.stage1:
            data["tumor_stages"]["stage_1"] = ["Stage I", "Stage IA", "Stage IB"]
        if self.stage2:
            data["tumor_stages"]["stage_2"] = ["Stage II", "Stage IIA", "Stage IIB"]
        if self.stage3:
            data["tumor_stages"]["stage_3"] = [
                "Stage III",
                "Stage IIIA",
                "Stage IIIB",
                "Stage IIIC",
            ]
        if self.stage4:
            data["tumor_stages"]["stage_4"] = ["Stage IV"]

        if self.join_files:
            data["join_files"] = "True"
        else:
            data["join_files"] = "False"

        if self.join_method == "Merge":
            data["join_method"] = "merge"
        else:
            data["join_method"] = "append"

        self.data_config = data

        with open("./config.json", "w+") as json_file:
            json.dump(data, json_file)

        self.run_data_founder()

    def run_data_founder(self):
        gdc_server = GDCServer(self.data_config)
        gdc_server.get()

    def show_help(self):
        try:
            help_window = QtWidgets.QMainWindow()
            self.help_s = HelpWindow(help_window)
            help_window.show()
        except Exception as err:
            print(err)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
