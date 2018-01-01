# HTML parser

from html.parser import HTMLParser

class htmlParser(HTMLParser):

	# meta tag counter
	mcount = 0

	# handles comment
	def handle_comment(self, data):
		print( "Found comment: ", data)
		pos = self.getpos()
		print("At line ", pos[0], " position ", pos[1]) 


	# handles start tag and prints attributes if any
	def handle_starttag(self, tag, attrs):
		# returns a tuple with line and char position
		pos = self.getpos()
		print(tag, "at line ", pos[0], " position ", pos[1])
			
		if tag == "meta":
			mcount += 1
		if attrs != None and len(attrs) > 0:
			print("\t Attributes: ")
			for at in attrs:
				print("\t", at[0] , " = ", at[1])

		# handles endtag
		def handle_endtag(self, tag):
			pos = self.getpos()
			print("End tag ", tag, "at line ", pos[0], " position ", pos[1])
		
	# handles data
	def handle_data(self,data):
		print("Encountered text data: ", data)
		
	
def main():
	# parsing object
	hp = htmlParser()

	# open html file
	file = open("to-do.html")
	
	if file.mode == "r":
		html = file.read()
		# feed method is implemented in HTMLParser
		hp.feed(html)
	
	print("Meta tag count: ", hp.mcount)
				

if __name__ == "__main__":
	main()
