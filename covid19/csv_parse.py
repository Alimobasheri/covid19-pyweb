import re

def omitCommas(row):
	"""
	Locates data parts with double quotes and removes commas within them.
	
	Parameters:
		row (str): The csv string to be searched for double quotes.
	
	Returns:
		(str): The same string without double quotes and extra commas.
	"""
	cases = re.findall('"[^"]+"', row)
	replaced = [re.sub('[",]', '', cases[i]) for i in range(len(cases)) if i%2 is 0]
	for i in range(len(cases)):
		if i%2 is 0:
			row = row.replace(cases[i], replaced[i])
	return row

def csvToList(csv, delimiter=','):
	"""
	Turn CSV string into list.
	
	Each line is splitted with \n and turned into rows. If the row contains double quotes, they're removed by omitCommas to prevent conflicts with comma delimiting the rows. Then each row is turned into a list of columns by splitting strings by comma. 
	
	Parameters:
		csv (str): CSV data to be parsed.
		
	Returns:
		(list): A list containing all data rows and columns. 
	"""
	rows = csv.decode().split('\n')
	return [(row, omitCommas(row))['"' in row].split(delimiter) for row in rows]

def getHeaders(lst, filterOne, filterTwo):
	"""
	Find indexes of desired values.
	
	Gets a list and finds index for values which exist either in filter one or filter two.
	
	Parameters:
		lst (list): Main list which includes the values.
		
		filterOne (list): A list containing values to find indexes of in the main list.
		
		filterTwo (list): A list to check by for the same index of a value from filterOne if it does not exist in the main list. 
		
	Returns:
		(list): A list containing indexes of values either from filterOne or filterTwo.
	"""
	headers = []
	for i in range(len(filterOne)):
		if filterOne[i] in lst:
			headers.append(lst.index(filterOne[i]))
		else:
			headers.append(lst.index(filterTwo[i]))
	return headers
