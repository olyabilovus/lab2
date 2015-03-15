__author__ = 'Olia'

import pandas as pd
import urllib2
import datetime
import os
import csv


id_list = [24, 25, 5, 6, 27, 23, 26, 7, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 8, 9, 10, 1, 3, 2, 4, 12, 20]

dict = {24: "Vinnytsya", 25: "Volyn", 5: "Dnipropetrovs'k",
        6: "Donets'k", 27: "Zhytomyr", 23: "Transcarpathia",
        26: "Zaporizhzhya", 7: "Ivano-Frankivs'k", 11: "Kiev",
        13: "Kirovohrad", 14: "Luhans'k", 15: " L'viv",
        16: "Mykolayiv", 17: "Odessa", 18: "Poltava",
        19: " Rivne", 21: "Sumy", 22:"Ternopil'",
        8: "Kharkiv", 9: "Kherson", 10:"Khmel'nyts'kyy",
        1: "Cherkasy", 3: "Chernivci", 2:"Chernihiv",
        4: "Crimea", 12: "Kiev City", 20: "Sevastopol"}

def download_vhi_files():
    os.chdir('D:\\Data_lab1\\VHI')
    format = '%Y-%m-%d %H-%M'
    for id in id_list:
        if id < 10:
            id = '0'+str(id)
        current_time = datetime.datetime.now()
        time_string = current_time.strftime(format)
        begin = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
        end = ".txt"
        url = begin+str(id)+end
        #url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+str(id)+".txt"
        vhi_url = urllib2.urlopen(url)
        out = open('vhi_id_'+str(id)+' '+time_string+'.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        print "VHI "+str(id)+" is downloaded..."
        print 'vhi_id_' + str(id) + ' ' + time_string + '.csv'

def read_csv(path_to_dir):
    data = []
    templist=os.listdir(path_to_dir)
    templist.sort()
    for files in templist :
        df = pd.read_csv(files, index_col=False, header=1)
        data.append(df)
        print files.title()
    return data


def print_vhi_year(data, id, year):
    region_data = data[id]
    list_1 = region_data.VHI[(region_data['year']==year) & (region_data['year'] != 0) &
                               (region_data['VHI'] > 0) & (region_data['week'] > 0) ].tolist()
    print 'VHI for region '+str(id)+' for the year '+str(year)
    print', '.join(str(x) for x in list_1)
    print 'max = ' + str(max(list_1))
    print 'min = ' + str(min(list_1))
    print

def print_vhi_extreme_drought(data, id, percent):
    region_data = data[id]
    list_1 = region_data.VHI[0:]
    print 'VHI for province ' + str(id)
    print ', '.join(str(x) for x in list_1)
    list_2 = region_data.year[(region_data['%Area_VHI_LESS_15'] > percent)].unique().tolist()
    print 'years with extreme drought(less than '+str(percent)+'):'
    print ', '.join(str(x) for x in list_2)
    print

def print_vhi_temperate_drought(data, id, percent):
    region_data = data[id]
    list_1 = region_data.VHI[0:]
    print 'VHI for province ' + str(id)
    print ', '.join(str(x) for x in list_1)
    list_2 = region_data.year[(region_data['%Area_VHI_LESS_35'] > percent) & (region_data['year'] > 0)
    ].unique().tolist()
    print 'years with temperate drought(less than '+str(percent)+'):'
    print ', '.join(str(x) for x in list_2)
    print


os.chdir('D:\\Data_lab1\\VHI')
path = os.getcwd()
download_vhi_files()
data = read_csv(path)
print_vhi_year(data, 24, 1994)
print_vhi_extreme_drought(data, 24, 0.02)
print_vhi_temperate_drought(data, 24, 0.02)
