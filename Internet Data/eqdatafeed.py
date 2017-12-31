# Parsing and processing JSON

import json
from urllib.request import urlopen

def printFormat(data):	
	# Create a dictionary object to use it later on to retrieve data
	theJSON = json.loads(data)

	# Now we can use theJSON object to retieve data
	if "title" in theJSON["metadata"]:
		print(theJSON["metadata"]["title"])
	
	# In metadata there is a count of event that occured to access it we do
	print(theJSON["metadata"]["count"]," event occured in past week" )
	
	# printing all events that occured, reported, and hass magnitude > 4.0
	for i in theJSON["features"]:
		# Only print those with magnitude > 4
		if i["properties"]["mag"] > 4.0:
			felt = i["properties"]["felt"]
			if (felt != None):
				if felt > 0:
					print("Place: ", i["properties"]["place"] , " Magnitude: " , i["properties"]["mag"], " reported ", i["properties"]["felt"], " times")


def main():
	
	# Earthquake json data url
	urljson = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson"
	
	# Open url	
	url = urlopen(urljson)

	if url.getcode() == 200:
		data = url.read()
		printFormat(data)
		
	else: 
		print("Error received from server. Error code: ", url.getcode())
if __name__ == "__main__":
	main()
