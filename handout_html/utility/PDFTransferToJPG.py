import os, sys, tqdm
from pdf2image import convert_from_path, convert_from_bytes
# reference: https://github.com/Belval/pdf2image

# Usage: python utility/PDFTransferToJPG.py
# .pdf put in the Directory "PDF"

# print("inputpath: {}, filename: {}".format(inputPath, fileName))

for __inputPath in os.listdir("./PDF"):
    if __inputPath[-4:] != ".pdf":
        continue
    fileName = __inputPath.split(".pdf")[0]
    inputPath = os.path.join("./PDF", __inputPath)
    print("inputpath: {}, filename: {}".format(inputPath, fileName))

    if not os.path.exists("./JPG"):
        os.mkdir("./JPG")
    if not os.path.exists("./JPG/{}".format(fileName)):
        os.mkdir("./JPG/{}".format(fileName))

    images = convert_from_path(inputPath)
    for i, img in enumerate(images):
        img.save("./JPG/{}/{}_{}.jpg".format(fileName, fileName, i))