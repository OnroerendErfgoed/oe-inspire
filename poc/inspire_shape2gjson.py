# -*- coding: utf-8 -*-

import os
import subprocess
import io
import unicodedata

dir1 = os.path.dirname(os.path.abspath(__file__))
dir2 = os.getcwd()

filename = 'aanduidingsobjecten'
origShp = dir1+'/shapes/'+filename+'.shp'
outputShp = dir1+'/shapes/'+filename+'_etrs89.shp'
gjsonfile = r'input/'+filename+'.json'
finalgjsonfile = 'input/'+filename+'_processed.json'
srcsrs = 'http://spatialreference.org/ref/epsg/31370/'
tgtsrs = 'http://spatialreference.org/ref/epsg/3043/'

# shape = ogr.Open(origShp)

command = ['/usr/bin/ogr2ogr', '-f', 'ESRI Shapefile', outputShp, origShp, '-s_srs', srcsrs, '-t_srs', tgtsrs]
subprocess.check_call(command)

command2 = ['/usr/bin/ogr2ogr', '-f', 'GeoJSON', '-nlt', 'MULTIPOLYGON', gjsonfile, outputShp]
subprocess.check_call(command2)

gjson = io.open(gjsonfile, 'r', encoding="utf-8")
finalgjson = open(finalgjsonfile, 'w')

for line in gjson:
    templ = unicodedata.normalize('NFD', line).encode('ascii', 'ignore')
    finalgjson.write(templ)

gjson.close()
finalgjson.close()
