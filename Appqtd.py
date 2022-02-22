from PySide2 import QtCore, QtWidgets, QtGui
from pathlib import Path
import subprocess
import glob
import tornado

from mainwindow import Ui_MainWindow

import PlugStat


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    rpp_dir = ""
    td = ""
    nb_rpp = 0
    start_date = ""
    plug_list = []
    thr = 0.5
    image = ""
    searchedterm = ""

    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setStyleSheet('background-color: rgb(0,0,0);'
                           'color: white')
        self.setup_connections()

    def setup_connections(self):
        self.btn_filedialog.clicked.connect(self.select_rpp_dir)
        self.cal_startdate.clicked.connect(self.set_start_date)
        self.btn_copyfiles.clicked.connect(self.copy_files)
        self.btn_td.clicked.connect(self.open_td)
        self.btn_bar.clicked.connect(self.create_bar)
        self.dsb_threshold.valueChanged.connect(self.create_bar)
        self.btn_createtxt.clicked.connect(self.create_list_txt)
        self.le_search.returnPressed.connect(self.search_plug)
        self.btn_search.clicked.connect(self.search_plug)

    def select_rpp_dir(self):
        App.rpp_dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Reaper Project Folder')
        if App.rpp_dir:
            self.le_rppdir.setText(App.rpp_dir)

    def set_start_date(self):
        cal_date = self.cal_startdate.selectedDate().getDate()
        App.start_date = str(cal_date[2]) + "/" + str(cal_date[1]) + "/" + str(cal_date[0])
        self.le_selecteddate.setText(App.start_date)

    def copy_files(self):
        if not self.le_rppdir.text() or not self.le_selecteddate.text():
            message = QtWidgets.QMessageBox()
            message.information(self, "PlugStat", "Please select .rpp folder AND set a start date !")
        else:
            App.td = Path(App.rpp_dir) / "temp"
            if App.td.exists():
                PlugStat.del_temp_dir(App.td)
            App.td = PlugStat.create_temp_dir(App.rpp_dir)
            PlugStat.copy_files(App.start_date, App.rpp_dir, App.td)
            message = QtWidgets.QMessageBox()
            message.information(self, "PlugStat", PlugStat.copy_files(App.start_date, App.rpp_dir, App.td))
            App.nb_rpp = PlugStat.rpp_number(App.td)
            self.le_nbrpp.setText(str(App.nb_rpp))
            App.plug_list = PlugStat.create_plug_dict(App.td, App.nb_rpp)

    def open_td(self):
        if App.td:
            subprocess.Popen(f'explorer {App.td}')
        else:
            message = QtWidgets.QMessageBox()
            message.information(self, "PlugStat", "Please select the Reaper Projects folder first !")

    def create_bar(self):
        App.thr = self.dsb_threshold.value()

        try:
            PlugStat.create_bar(App.plug_list, App.thr, App.nb_rpp, App.td)
            l = glob.glob(f"{Path(App.td) / '*plugs.png'}")
            self.lab_image.setPixmap(str(l[0]))

        except ValueError:  # if plug_list is empty, value error is raised
            pass

    def create_list_txt(self):
        PlugStat.create_list_txt(App.td, App.plug_list)
        message = QtWidgets.QMessageBox()
        message.information(self, "PlugStat", f"Used plugins list created in {App.td}")

    def search_plug(self):
        App.searchedterm = self.le_search.text()
        result_list = PlugStat.search_plug(App.searchedterm, App.plug_list)
        message = QtWidgets.QMessageBox()
        message.information(self, "PlugStat", str(result_list))

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "Quit PlugStat ?",
                                               "Are you sure you want to quit ? Temp folder will be deleted.",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.setStyleSheet("color: rgb(255, 255, 255)")
        if close == QtWidgets.QMessageBox.Yes:
            App.td = Path(App.rpp_dir) / "temp"
            if App.td.exists():
                PlugStat.del_temp_dir(App.td)
            event.accept()
        else:
            event.ignore()


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
