@outputSchema("heathrow:{(Year:chararray,Month:float,maxtemp:float,mintemp:float,frostday:chararray,rainfall:chararray,sunshine:chararray)}")
def fahrenheit(heathrow):
	Year,Month,maxtemp,mintemp,frostday,rainfall,sunshine = heathrow.split(' ')
	maxtemp_1 = float(maxtemp) * 9/5 + 32
	mintemp_1 = float(mintemp) * 9/5 + 32
	return Year,Month,maxtemp_1,mintemp_1,frostday,rainfall,sunshine
