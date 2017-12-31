import os
import shutil
from os import path

def main():
	# Verify if the path to the file exist	
	if path.exists("2018.txt"):
		# Actual path
		srcpath = path.realpath("2018.txt")
		
		# Create a backup file [just copy the content]
		dstpath = srcpath + ".bak"
		#shutil.copy(srcpath,dstpath)
		
		# Create a backup file with meta data information such as permissions, modification time etc
		shutil.copystat(srcpath,dstpath)	
		
		# Rename original file
		os.rename("2018.txt","2018_Calendar.txt")

if __name__ == "__main__":
	main()
