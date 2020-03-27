import asyncio
from flask import render_template
import json

from covid19 import app
from covid19 import csv_parse
from covid19 import fetch_data
from covid19 import utils

@app.route('/')
def index():
	with open('covid19/options.json', 'r') as options:
	  appOptions = json.load(options)
	  
	  date = {'day':25, 'month':3, 'year':2020}
	  fileName = utils.parseDateToFilename(date, appOptions['DATA_FILE_FORMAT'])
	  
	  loop = asyncio.get_event_loop()
	  data = loop.run_until_complete(fetch_data.getData(fileName, appOptions['COVID_DATA_BASE_URL']))
	  loop.stop()
	  dataList = csv_parse.csvToArray(data)
	  tableHeaders = dataList[0]
	  tableRows = dataList[1:5]
	  return render_template(
	  	'index.html', 
	  	title='Covid-19 App',
	  	chart_title='covid19 charts', 
	  	chart_date=date,
	  	table_headers=tableHeaders, 
	  	table_rows=tableRows)
