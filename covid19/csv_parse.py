def csvToArray(csv, delimiter=','):
	rows = csv.decode().split('\n')
	return [row.split(delimiter) for row in rows]