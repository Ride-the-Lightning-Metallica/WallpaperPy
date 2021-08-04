import json
from datetime import datetime

from wallpaper_engine import WallpaperEngine

wallpaper_engine = WallpaperEngine('https://www.goodfon.ru/')

data_path = wallpaper_engine.get_file_abspath('data.json')

with open(data_path, 'r') as file:
    data = json.load(file)

update_frequency = data['update_frequency']

if update_frequency != 'Never':
    current_datetime = datetime.today()
    last_change = datetime.strptime(data['last_change'], '%c')

    update_frequency_choices = {
        'One day': 1,
        'Two days': 2,
        'Three days': 3,
        'Week': 7,
        'Month': 30
    }

    update_frequency = update_frequency_choices[update_frequency]

    if (current_datetime.day - last_change.day) >= update_frequency:
        wallpaper_engine.update_wallpaper(data, data_path)
