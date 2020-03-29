import asyncio
import json

from flask import redirect, url_for, render_template

from covid19 import app
from covid19 import csv_parse
from covid19 import fetch_data
from covid19 import utils

@app.route('/')
def index():
	return redirect(url_for('tables', page=1))

@app.route('/tables/<page>')
def tables(page):
	with open('covid19/options.json', 'r') as options:
		appOptions = json.load(options)
		
		date = {'day':28, 'month':3, 'year':2020}
		fileName = utils.parseDateToFilename(date, appOptions['DATA_FILE_FORMAT'])
		
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		data = loop.run_until_complete(fetch_data.getData(fileName, appOptions['COVID_DATA_BASE_URL']))
		loop.stop()
		
		dataList = csv_parse.csvToArray(data)
		sortedList = sorted(dataList[1:len(dataList)-1], key=lambda x: x[3])
		
		filteredIndices = [3, 4, 7, 8, 9]
		tableHeaders = [dataList[0][x] for x in filteredIndices]
		
		indexZero = (1, (int(page)-1)*50)[int(page) is not None]
		tableRows = [[x[y] for y in filteredIndices] for x in sortedList[indexZero: indexZero+50]]
		
		return render_template(
		'index.html',
		title='Covid-19 App',
		chart_title='covid19 charts',
		chart_date=date,
		table_headers=tableHeaders,
		table_rows=tableRows)
