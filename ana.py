def checkAuto(a): 
	if a < 0: a = -a 
	squareNum = a*a 
	temp = a 
	count = 0
	while temp != 0: 
		count += 1
		temp = int(temp/10) 
	lastDigit = squareNum%pow(10, count) 
	if lastDigit == a: 
		return "Automorphic"
	else: 
		return "Not Automorphic"
num = -4
print(checkAuto(num))
