def parseDateToFilename(date, fExtension):
	return(f"{date.strftime('%m-%d-%Y')}.{fExtension}")

from datetime import datetime, timedelta

def getDiffDate(today, days):
	return today + timedelta(days=days)

def getLatestDate(today, diff):
	return getDiffDate(today, diff).strftime('%m-%d-%Y')
