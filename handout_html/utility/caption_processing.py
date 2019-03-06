with open('../caption/filelist', 'r') as fp:  
	line = fp.readline()
	cnt = 0
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		cnt += 1
		with open('../caption/' + line.strip("\n"), 'r') as myfile:
			data="<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'></head>\n" + myfile.read().replace('\n', '<br>\n')
			print(data)
		file = open("../caption/" + str(cnt) + ".html",'w')
		file.write(data)
