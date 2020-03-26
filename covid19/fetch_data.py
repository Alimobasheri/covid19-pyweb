import urllib.request
import asyncio

async def getData(fileName, baseUrl, fn=None):
		path = f"{baseUrl}/{fileName}"
		with urllib.request.urlopen(path) as response:
			data = response.read()
			return data