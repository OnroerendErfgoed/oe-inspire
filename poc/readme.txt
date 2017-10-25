1. install stetl (http://www.stetl.org/en/latest/install.html)

2. place shapefile in shapes folder (name it aanduidingsobjecten.shp for the poc, name is still hardcoded in the script)

3. python inspire_shape2gjson.py from inside poc folder

4. stetl -c inspire_config.cfg (assuming stetl has been installed correctly)


ALTERNATIVE TO STETL INSTALLATION

1. docker pull justb4/stetl

2. place shapefile in shapes folder (name it aanduidingsobjecten.shp for the poc, name is still hardcoded in the script)

3. python inspire_shape2gjson.py from inside poc folder

4. in command line from directory with config file: 	
			WORK_DIR=`pwd` 
			sudo docker run -v ${WORK_DIR}:${WORK_DIR} -w ${WORK_DIR} justb4/stetl:latest -c inspire_config.cfg
