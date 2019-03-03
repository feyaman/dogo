import os, sys, tqdm
from pdf2image import convert_from_path, convert_from_bytes
# reference: https://github.com/Belval/pdf2image

# Usage: python PDFTransferToJPG.py ./PDF/W1_Regression.pdf

inputPath = sys.argv[1]
fileName = inputPath.split("/")[-1].split(".pdf")[0]

print("inputpath: {}, filename: {}".format(inputPath, fileName))

if not os.path.exists("./JPG"):
	os.mkdir("./JPG")
if not os.path.exists("./JPG/{}".format(fileName)):
	os.mkdir("./JPG/{}".format(fileName))

images = convert_from_path(inputPath)
for i, img in enumerate(images):
	img.save("./JPG/{}/{}_{}.jpg".format(fileName, fileName, i))