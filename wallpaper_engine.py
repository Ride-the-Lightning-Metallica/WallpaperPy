import ctypes
import json
import requests
import os
import re
import winshell

from bs4 import BeautifulSoup
from random import randint
from getpass import getuser
from datetime import datetime


class WallpaperEngine:
    def __init__(self, url) -> None:
        self.root_url = url

    def get_file_abspath(self, filename: str) -> str:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(root_dir, filename)

        return file_path

    def get_wallpaper_categories(self) -> dict:
        response = requests.get(self.root_url)
        soup = BeautifulSoup(response.content, 'lxml')

        categories = {}
        for category in soup.select('.head_menu a'):
            categories[category.string] = category.get('href')

        return categories

    def get_random_page(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        paginator_string = soup.find(class_='paginator__page').string
        max_pages = re.findall('\d+', paginator_string)[-1]
        max_pages = int(max_pages)
        random_page_url = url + f'index-{randint(1, max_pages)}.html'

        return random_page_url

    def get_random_wallpaper(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        wallpapers = soup.select('.wallpapers__item__wall > a[itemprop="url"]')
        wallpaper_url = wallpapers[randint(0, len(wallpapers) - 1)].get('href')

        wallpaper_name = os.path.basename(wallpaper_url)
        wallpaper_name = os.path.splitext(wallpaper_name)[0]

        user32 = ctypes.windll.user32
        monitor_extension = f'{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}'
        wallpaper_url = (
            self.root_url + 'download/' +
            f'{wallpaper_name}/{monitor_extension}/'
        )

        response = requests.get(wallpaper_url)
        soup = BeautifulSoup(response.content, 'lxml')

        wallpaper = soup.select_one('a[id="im"]').get('href')

        return wallpaper

    def download_image(self, url: str, upload_to: str) -> str:
        response = requests.get(url)
        filename = os.path.basename(url)
        full_path = os.path.join(upload_to, filename)
        
        if not os.path.exists(upload_to):
            os.mkdir(upload_to)

        with open(full_path, 'wb') as file:
            file.write(response.content)

        return full_path

    def remove_image(self, path: str) -> None:
        try:
            os.remove(path)
        except OSError as error:
            print(error)
            print('File path can not be removed')

    def set_wallpaper_image(self, image: str) -> None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)

    def update_wallpaper(self, data: dict, data_path: str) -> None:
        if 'current_wallpaper' in data and not data['save_current_wallpaper']:
            self.remove_image(data['current_wallpaper'])

        random_page_url = self.get_random_page(
            data['wallpaper_category']['url']
        )
        wallpaper_url = self.get_random_wallpaper(random_page_url)
        wallpaper = self.download_image(
            wallpaper_url,
            upload_to=self.get_file_abspath('wallpapers')
        )
        self.set_wallpaper_image(wallpaper)

        current_datetime = datetime.today()

        data['current_wallpaper'] = wallpaper
        data['last_change'] = current_datetime.strftime('%c')
        data['save_current_wallpaper'] = False

        with open(data_path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=True)

    def add_to_startup(self, filename) -> None:
        USER_NAME = getuser()

        path = (
            rf'C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
        )

        path = os.path.join(path, filename) + '.lnk'
        file_path = self.get_file_abspath(filename) + '.pyw'

        winshell.CreateShortcut(Path=path, Target=file_path)

    def add_to_desktop(self, filename: str) -> None:
        destop_path = winshell.desktop()

        file_path = self.get_file_abspath(filename) + '.pyw'
        path = os.path.join(destop_path, filename) + '.lnk'
        icon_path = self.get_file_abspath('icon.ico')

        winshell.CreateShortcut(
            Path=path, Target=file_path, Icon=(icon_path, 0)
        )
