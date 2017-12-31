
import os
from os import path
from datetime import date,time,timedelta
import datetime
import time

def main():
	# Print OS name, prints nt for windows
	print(os.name)
	
	# File existence and type check
	print("File 2018 exist: ", path.exists("2018.txt"))
	print("File 2018 is a file: ", path.isfile("2018.txt"))
	print("File 2018 is a directory: ", path.isdir("2018.txt"))

	# Actual path 
	print("File is located @ ", path.realpath("2018.txt"))
	print("File path and file name", path.split(path.realpath("2018.txt")))
	
	# Get time the file was modified last 
	# ctime to get readable time format
	mt = time.ctime(path.getmtime("2018.txt"))
	print(mt)
	
	# different format
	print(datetime.datetime.fromtimestamp(path.getmtime("2018.txt")))

	# prints the time duration the file was last modified
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("2018.txt"))
	
	print("File was modified ",td, " ago")
	print("File was modified ",td.total_seconds(), " seconds ago")
	
		

if __name__ == "__main__":
	main()