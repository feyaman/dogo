with open('../caption/1.html', 'r') as myfile:
	data=myfile.read().replace('\n', '<br>\n')
	print(data)
file = open("../caption/1.html",'w')
file.write(data)
