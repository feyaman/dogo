from distutils.dir_util import copy_tree

f = open('setting.config')
for buf in f.readlines():
    if buf[:8] == 'homeDir=':
        inDir = buf[8:].strip('\n')
    elif buf[:10] == 'targetDir=':
        outDir = buf[10:].strip('\n')
print(inDir)
print(outDir)
copy_tree(inDir, outDir)
