import sys
template = open(sys.argv[1], "r").read()
content = open(sys.argv[2], "r").read().split("========")
for infos in content:
	template_copy = template
	infos = infos.split("\n")
	infos = [x for x in infos if x != ""]
	# print(infos)
	for i in range(len(infos)):
		if infos[i] == "<theImage>":
			template_copy = template_copy.replace("xxImagexx", infos[i + 1])
		elif infos[i] == "<theTitle>":
			template_copy = template_copy.replace("xxTitlexx", infos[i + 1])
		elif infos[i] == "<theDate>":
			template_copy = template_copy.replace("xxDatexx", infos[i + 1])
		elif infos[i] == "<theLocation>":
			template_copy = template_copy.replace("xxLocationxx", infos[i + 1])
		elif infos[i] == "<theContent>":
			template_copy = template_copy.replace("xxContentxx", infos[i + 1])
		elif infos[i] == "<theUrl>":
			template_copy = template_copy.replace("xxURLxx", infos[i + 1])
		elif infos[i] == "<theReadMe>":
			template_copy = template_copy.replace("xxReadMexx", infos[i + 1])
	print(template_copy, "========")
