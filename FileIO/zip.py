import os
from os import path
import shutil
from zipfile import ZipFile

def archive():
	if path.exists("2018_Calendar.txt"):
		# Get root path and file name
		root_path,filename = path.split(path.realpath("2018_Calendar.txt"))
		
		# Create an archive (compress every file in directory)
		# File name, file type could be RAR, tar etc, destination path
		shutil.make_archive(filename,"zip",root_path)

		# Specific file compression
		# with construct in python creates its own local scope for working with objects
		# w for write permission
		# In this scope block python closes the file once task is completed
		with ZipFile("2018.zip","w") as newzip:
			# newzip is now a file object
			# Pass file name as an argument to add it to the zip folder 
			newzip.write("2018_Calendar.txt")
			newzip.write("2018.txt.bak")


if __name__ == "__main__":
	archive()