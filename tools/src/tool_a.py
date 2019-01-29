import sys
from tqdm import tqdm
import os
def parse_cfg():
	cfg_file_name = sys.argv[1]
	cfg = open(cfg_file_name, "r").read().split("\n")
	src = cfg[0].split("=")[1]
	des = cfg[1].split("=")[1]
	return src, des
def read_file(src):
	file_list, folder_list = [], []
	for root, d_names, f_names in os.walk(src):
		# print(root, d_names, f_names)
		for i in f_names:
			file_list.append(root + ('' if (root == src) else '/') + i)
		for i in d_names:
			folder_list.append(root + ('' if (root == src) else '/') + i)
	# print(folder_list, '\n', file_list)
	return folder_list, file_list
def process(folder_list, filelist, src, des):
	for i in folder_list:
		directory = i.replace(src, des)
		if not os.path.exists(directory):
			os.makedirs(directory)
	for i in filelist:
		file = open(i, "r").read()
		##################################
		### do something you want here ###
		##################################
		print("processing " + i.replace(src, des))
		##################################
		target_file = open(i.replace(src, des), "w")
		target_file.write(file)
if __name__ == "__main__":
	src, des = parse_cfg()
	folder_list, file_list = read_file(src)
	process(folder_list, file_list, src, des)
