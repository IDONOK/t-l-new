import sys
import string

while True:
	line=sys.stdin.readline()
	if not line:
		break
	row=string.strip(line, "\n")
	year,month,maxtemp,mintemp,frostday,rainfall,sunshine= string.split(row, "\t")
	rainfall= float(rainfall)/25.4
	print "\t".join([year,month,maxtemp,mintemp,frostday,str(rainfall),sunshine])
