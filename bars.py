import json
import sys
import os
from math import sqrt


def input_file_name():
    if len(sys.argv) == 1:
        file_name = input("Введите название файла  ")
    else:
        file_name = sys.argv[1]
    return file_name


def input_geo_data():
    geo_data = []
    if len(sys.argv) == 2 or len(sys.argv) == 1:
        geo_data0, geo_data1 = input("Введите координаты  ").split()
        geo_data.append(float(geo_data0))
        geo_data.append(float(geo_data1))
    else:
        geo_data.append(float(sys.argv[2]))
        geo_data.append(float(sys.argv[3]))
    return geo_data


def file_exists(filepath):
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return True


def check_json(file_name):
    if file_name.endswith('.json'):
        return True


def search_bar_max(bars_list):
    bar_max = max(bars_list, key=lambda l: l['Cells']['SeatsCount'])
    print("%s %d: %s" % ("Бар с максимальным числом посадочных мест",
                         bar_max['Cells']['SeatsCount'],
                         bar_max['Cells']['Name']))


def search_bar_min(bars_list):
    bar_min = min(bars_list, key=lambda l: l['Cells']['SeatsCount'])
    print("%s %d: %s" % ("Бар с минимальным числом посадочных мест",
                         bar_min['Cells']['SeatsCount'],
                         bar_min['Cells']['Name']))


def search_bar_near(bars_list):
    geo_data = input_geo_data()
    x = sqrt(geo_data[0]**2 + geo_data[1]**2)
    bar_near = min(bars_list, key=lambda l:
                   abs(sqrt(l['Cells']['geoData']['coordinates'][0]**2 +
                       l['Cells']['geoData']['coordinates'][1]**2)-x))
    print("%s %s: %s" % ("Ближайший к Вам бар с координатами",
                         bar_near['Cells']['geoData']['coordinates'],
                         bar_near['Cells']['Name']))


def load_data(filepath):
    bars_list = json.load(filepath)
    search_bar_near(bars_list)
    search_bar_max(bars_list)
    search_bar_min(bars_list)


if __name__ == '__main__':
    file_name = input_file_name()
    if check_json(file_name) is None:
        print("Формат файла должен быть .json")
    elif file_exists(file_name) is None:
        print("Ошибка открытия файла")
    else:
        load_data(open(file_name, 'r'))
