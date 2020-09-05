#! /usr/local/bin/python3
import datetime,sys

numRect = []
dateRect = []

def calcNum(size): 
	for line in range(1, size + 1):
		numRect.append([str(num) for num in listRec(size, line)])

def calcDate(size, date):
	for line in range(1, size + 1):
		dateRect.append([(date + datetime.timedelta(days=num)).strftime('%Y-%m-%d') for num in listRec(size, line)])

	
def listRec(size, line):
	if size == 1:
		return [1]
	if line == 1:
		return [i for i in range(size * size - 2*size + 2, size * size - 2*size + 2 - size, -1)]
	if line == size:
		return [i for i in range(size * size - size + 1, size * size + 1)]
	result = []
	result.append(size * size - 2*size + 2 + line - 1)
	result += listRec(size - 2, line - 1)
	result.append(size * size - 3*size + 3 - line + 1)
	return result


normal = '\033[0m%s\033[0m'
yellow = '\033[33m%s\033[0m'
red = '\033[31m%s\033[0m'
blue = '\033[34m%s\033[0m'


if __name__=="__main__":
	size = int(sys.argv[1])
	baseday = datetime.datetime.strptime('2019-12-31', '%Y-%m-%d')
	today = datetime.datetime.today()
	
	stoday = today.strftime('%Y-%m-%d')
	elapsedDays = (today - baseday).days
	print('今天日期:',yellow % stoday)
	print('今年已经过了:', (yellow % (elapsedDays)), '天')
	print()

	calcNum(size)
	calcDate(size, baseday)


	
	for i in range(size):
		for j in range(size):
			numRect[i][j] = numRect[i][j].rjust(3, '0')

	for i in range(size):
		numRect[i][i] = red % numRect[i][i]
		numRect[i][-i - 1] = red % numRect[i][-i - 1]
		numRect[-i - 1][i] =red % numRect[-i - 1][i]
		numRect[size // 2][i] = blue % numRect[size // 2][i]
		numRect[i][size // 2] = blue % numRect[i][size // 2]
		dateRect[i][i] = red % dateRect[i][i]
		dateRect[i][-i - 1] = red % dateRect[i][-i - 1]
		dateRect[-i - 1][i] =red % dateRect[-i - 1][i]
		dateRect[size // 2][i] = blue % dateRect[size // 2][i]
		dateRect[i][size // 2] = blue % dateRect[i][size // 2]

	for i in range(size):
		for j in range(size):
			if numRect[i][j].find(str(elapsedDays)) != -1: numRect[i][j] = yellow % numRect[i][j]
			if stoday in dateRect[i][j]:dateRect[i][j]= yellow % dateRect[i][j]


	for row in range(size):
		print('|'.join(numRect[row]))
	print()
	print()
	for row in range(size):
		print('|'.join(dateRect[row]))


	



