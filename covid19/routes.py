import asyncio
import json
from datetime import datetime

from flask import redirect, url_for, render_template, request, jsonify

from covid19 import app
from covid19 import csv_parse
from covid19 import fetch_data
from covid19 import utils
from covid19 import data_list

@app.route('/')
def index():
	today = datetime.utcnow()
	dateStr = request.args.get('date', default=utils.getLatestDate(today, -1))
	return redirect(url_for('tables', date=dateStr))

@app.route('/tables')
def tables():
	today = datetime.utcnow()
	dateStr = request.args.get('date', default=utils.getLatestDate(today, -1))
	with open('covid19/options.json', 'r') as options:
		appOptions = json.load(options)
		
		date = datetime.strptime(dateStr, '%m-%d-%Y')
		jsonDate = {'day': date.day, 'month': date.month, 'year': date.year}
		fileName = utils.parseDateToFilename(date, appOptions['DATA_FILE_FORMAT'])
		
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		data = loop.run_until_complete(fetch_data.getData(fileName, appOptions['COVID_DATA_BASE_URL']))
		loop.stop()
		
		dataList = csv_parse.csvToList(data)
		
		filteredIndices = csv_parse.getHeaders(dataList[0], appOptions['TABLE_TITLES_OLD'].split('+'), appOptions['TABLE_TITLES_NEW'].split('+'))
		
		tableHeaders = [dataList[0][x] for x in filteredIndices]
		
		sortedList = sorted(dataList[1:len(dataList)-2], key=lambda x: x[filteredIndices[0]])
		
		tableRows = [[x[y] for y in filteredIndices] for x in sortedList[1:]]
		
		groupedRows = data_list.groupBy(tableRows, 0)
		mergedRows = [data_list.dataMerge(group, [2, 3, 4], 0, lambda a, b : a+int(b)) for group in groupedRows]
		mergedRows = sorted(mergedRows, key=lambda x: x[2], reverse=True)
		
		return render_template(
		'index.html',
		title='Covid-19 App',
		chart_title='covid19 charts',
		chart_date=jsonDate,
		table_headers=tableHeaders,
		table_rows=mergedRows)
