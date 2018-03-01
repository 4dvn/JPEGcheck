import os
def checkifjpeg(fp):
	file = open(fp,'rb')
	bytevals = file.read()
	hexvals = bytevals.hex()
	if(hexvals[:6] == 'ffd8ff'):   # Check if the first few bytes match
		return True
	else:
		return False


