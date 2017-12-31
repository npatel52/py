# urllib2 has been split across several modules in python 3
from urllib.request import urlopen

def main():
	# open url
	url = urlopen("https://google.com")
	
	# print result code 200: for eeverything is ok, 404: if not found etc
	print("Request code: ", url.getcode())
	
	# read the html data from the url
	html = url.read()
	print(html)

if __name__ == "__main__":
	main()