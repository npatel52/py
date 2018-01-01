# Operate on XML dom in memory
from xml.dom.minidom import parse

def main():
	# load and parse XML
	xmldoc = parse("sample.xml")
	
	# Print nodename and first child name
	print(xmldoc.nodeName)
	print(xmldoc.firstChild.tagName)
	
	
	# adding new tag to XML document
	# Create tag
	lan = xmldoc.createElement("language")
	# Set tag
	lan.setAttribute("name", "C")
	# append tag
	xmldoc.firstChild.appendChild(lan)

	# Getting attributes value by tag name
	languages = xmldoc.getElementsByTagName("language")

	print(len(languages), " languages.")

	for language in languages:
		print("Language: ", language.getAttribute("name"))

if __name__ == "__main__":
	main()