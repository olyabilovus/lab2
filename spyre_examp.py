# -*- coding: utf-8 -*-
from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import urllib2
import datetime

class WheatherApp(server.App):

	title = "VHI Data Representation"
	inputs = [{	"input_type":'dropdown',
				"label": 'Index', 
				"options":[
				{"label":"TCI", "value":"TCI"},
				{"label":"VCI", "value":"VCI"},
				{"label":"VHI","value":"VHI"}
				],
				"variable_name": 'index', 
				"action_id" : "update_data",
			},
			{	"input_type":'dropdown',
				"label": 'Area', 
				"options" : [
					#{"label": "Cherkasy", "value":"Черкаська"}, 
					#{"label":"Chernihiv", "value":"Чернігівська"},
					#{"label":"Chernivtsy", "value":"Чернівецька"},
					{"label":"Crimea", "value": u"Крим", "checked":True},
					{"label":"Dnipropetrovsk", "value": u'Дніпропетровська'},
					#{"label":"", "value":""}
				],
				"variable_name": 'area', 
				"action_id" : "update_data",
			},
			{	"input_type":'text',
				"label": 'Choose week interval: format:(start,end)', 
				"value": "1,10",
				"variable_name": "interval", 
				"action_id" : "update_data",
			}
			]
	tabs = ["Table","Plot"]
	controls = [{	"control_type" : "hidden",
					"control_id" : "update_data",
					"label" : "update",
				}]
	outputs = [{	"output_type" : "table",
					"output_id" : "table_id",
					"control_id" : "update_data",
					"tab": "Table",
					"on_page_load" : True,
				},
				{	"output_type" : "plot",
					"output_id" : "plot_id",
					"control_id" : "update_data",
					"tab":"Plot",
					"on_page_load" : True,
				}
				]

	def getPlot(self, params):
		index=params['index']
		df = self.getData(params)
		tmp = pd.DataFrame()
		grouped = df.groupby('year')
		plt = grouped.aggregate(np.mean)[index].plot(kind='bar')
		plt.set_ylabel(index + ' average per interval')
		#for name, group in grouped:
		#	med = group[].median()
		
		fig = plt.get_figure()
		return fig

	# def getHTML(self,params):
	# 	f = int(params['freq'])
	# 	time.sleep(f)
	# 	return "hello world"
	
	def getData(self,params):
		area = params['area']
		index = params['index']
		interval_st = int(params['interval'].split(',')[0])
		interval_end = int(params['interval'].split(',')[1])
		frames = self.load_frames()
		countrySearch = { 
		u"Черкаська":22, #Cherkasy
		u"Чернігівська":24,
		u'Крим': 23,
		u"Дніпропетровська":3,
		u"Донецька":4,
		u"Івано-Франківська":8,
		u"Харківська":19,
		u"Херсонська":20,
		u"Хмельницька":21,
		u"Київська":9,
		u"Кіровоградська":10,
		u"Луганська":11,
		u"Львівська":12,
		u"Миколаївська":13,
		u"Одеска":14,
		u"Полтавська":15,
		u"Рівненська":16,
		u"Сумська":17,
		u"Тернопільська":18,
		u"Закарпатська":6,
		u"Вінницька": 1,
		u"Волинська":2,
		u"Запорізька":7,
		u"Житомирська":5
		}
		temp_frame = frames[countrySearch[area]]
		week = temp_frame["week"]
		year = temp_frame['year']
		ind = temp_frame[index]
		df = pd.DataFrame()
		df.insert(0, 'week', week)
		df.insert(1, 'year', year)
		df.insert(2, index, ind)
		df1 = df[(df["week"] >= interval_st) & (df["week"] <= interval_end)]
		df1.set_index('year')
		return df1

	def load_frames(self):
		os.chdir('D:\\Data_lab1\\VHI')
		path = os.getcwd()
		data = []
		templist=os.listdir(path)
		templist.sort()
		for files in templist :
			df = pd.read_csv(files, index_col=False, header=1)
			data.append(df)
		return data


app = WheatherApp()
app.launch(port=8002)