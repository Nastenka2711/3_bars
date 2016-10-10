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
    return os.path.exists(filepath) and os.path.isfile(filepath)


def check_json(file_name):
    return file_name.endswith('.json')


def search_bar_max(bars_list):
    return max(bars_list, key=lambda l: l['Cells']['SeatsCount'])


def search_bar_min(bars_list):
    return min(bars_list, key=lambda l: l['Cells']['SeatsCount'])


def search_bar_near(bars_list):
    geo_data = input_geo_data()
    x = sqrt(geo_data[0]**2 + geo_data[1]**2)
    return min(bars_list, key=lambda l:
               abs(sqrt(l['Cells']['geoData']['coordinates'][0]**2 +
                        l['Cells']['geoData']['coordinates'][1]**2)-x))


def load_data(filepath):
    return json.load(filepath)


if __name__ == '__main__':
    file_name = input_file_name()
    if not check_json(file_name):
        print("Формат файла должен быть .json")
    elif not file_exists(file_name):
        print("Ошибка открытия файла")
    else:
        with open(file_name, 'r') as filepath:
            bars_list = load_data(filepath)
        bar_near = search_bar_near(bars_list)
        print("%s %s: %s" % ("Ближайший к Вам бар с координатами",
                             bar_near['Cells']['geoData']['coordinates'],
                             bar_near['Cells']['Name']))
        bar_max = search_bar_max(bars_list)
        print("%s %d: %s" % ("Бар с максимальным числом посадочных мест",
                             bar_max['Cells']['SeatsCount'],
                             bar_max['Cells']['Name']))

        bar_min = search_bar_min(bars_list)
        print("%s %d: %s" % ("Бар с минимальным числом посадочных мест",
                             bar_min['Cells']['SeatsCount'],
                             bar_min['Cells']['Name']))
