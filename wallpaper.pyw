import sys
import os
import json

from PyQt5 import QtGui, QtWidgets
from wallpaper_interface import *
from wallpaper_engine import WallpaperEngine


class Wallpaper(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.wallpaper_engine = WallpaperEngine('https://www.goodfon.ru/')
        self.data_path = self.wallpaper_engine.get_file_abspath(
            'data.json'
        )
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_2.clicked.connect(self.update_wallpaper)
        self.run()

    def run(self):
        with open(self.data_path, 'r') as file:
            self.data = json.load(file)

        self.wallpaper_categories = self.wallpaper_engine.get_wallpaper_categories()
        for category in self.wallpaper_categories:
            self.ui.comboBox.addItem(category)
        self.set_settings()

    def update_wallpaper(self):
        self.wallpaper_engine.update_wallpaper(self.data, self.data_path)
        self.set_settings()

    def set_settings(self):
        self.ui.comboBox.setCurrentText(
            self.data['wallpaper_category']['name']
        )
        self.ui.comboBox_2.setCurrentText(self.data['update_frequency'])

        if 'current_wallpaper' in self.data:
            wallpaper_directory, wallpaper_filename = (
                os.path.split(self.data['current_wallpaper'])
            )
            self.ui.label_5.setText(
                f'{wallpaper_directory}\\\n{wallpaper_filename}'
            )

    def get_settings(self):
        category_name = self.ui.comboBox.currentText()
        category = {
            'name': category_name,
            'url': self.wallpaper_categories[category_name]
        }
        update_frequency = self.ui.comboBox_2.currentText()
        current_wallpaper = self.ui.label_5.text().replace('\n', '')
        save_current_wallpaper = self.ui.checkBox.isChecked()

        settings = {
            'wallpaper_category': category,
            'update_frequency': update_frequency,
            'current_wallpaper': current_wallpaper,
            'save_current_wallpaper': save_current_wallpaper
        }

        return settings

    def save(self):
        if not self.data['is_auto_run']:
            self.wallpaper_engine.add_to_startup('wallpaper_auto')
            self.wallpaper_engine.add_to_desktop('wallpaper')
            self.data['is_auto_run'] = True

        settings = self.get_settings()
        self.data = {**self.data, **settings}

        with open(self.data_path, 'w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = Wallpaper()
    my_app.show()
    my_app.setWindowTitle('WallpaperPy')
    icon = QtGui.QIcon('icon.ico')
    my_app.setWindowIcon(icon)
    sys.exit(app.exec_())
