def parseDateToFilename(date, fExtension):
	return(f"{date['month']:02d}-{date['day']:02d}-{date['year']:04d}.{fExtension}")