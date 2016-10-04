import json

n_max_bar = 0
n_min_bar = 10000
geo_min = 100
my_geo = [37.621587946152017,55.765366956608390] #совсем рядом с Юнион Джек
name_max_bar = []
name_min_bar = []

def load_data(filepath):
	list_info_bars = json.load(filepath)
	for list_info_bar in list_info_bars:
		get_biggest_bar(list_info_bar)
		get_smallest_bar(list_info_bar)
		get_closest_bar(list_info_bar, my_geo[0], my_geo[1])
	print("Closest bar: " + name_geo)
	print("Max:", n_max_bar)
	for name in name_max_bar:
		if name['number'] == n_max_bar:
			print(name['name'])
	print("Min:", n_min_bar)
	for name in name_min_bar:
		if name['number'] == n_min_bar:
			print(name['name'])


def get_biggest_bar(data):
	global n_max_bar
	global name_max_bar
	if data['Cells']['SeatsCount'] >= n_max_bar:
		n_max_bar = data['Cells']['SeatsCount']
		name_max_bar.append({'name': data['Cells']['Name'], 'number': n_max_bar})


def get_smallest_bar(data):
	global n_min_bar
	global name_min_bar
	if data['Cells']['SeatsCount'] <= n_min_bar:
		n_min_bar = data['Cells']['SeatsCount']
		name_min_bar.append({'name': data['Cells']['Name'], 'number': n_min_bar})


def get_closest_bar(data, longitude, latitude):
	global geo_min 
	global name_geo
	x = data['Cells']['geoData']['coordinates'][0] - longitude
	y = data['Cells']['geoData']['coordinates'][1] - latitude
	xy = x ** 2 + y ** 2
	if xy < geo_min:
		geo_min = xy
		name_geo = data['Cells']['Name']	


if __name__ == '__main__':
	load_data(open('bars.json','r'))
