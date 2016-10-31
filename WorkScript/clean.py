# code=utf-8
import os
import shutil

def clear_directory(path):
    path = unicode(path , "utf8")
    if (os.path.exists(path)):
        for dir in os.listdir(path):
            dirPath = path + "\\" + dir
            print "Remove the item in %s" % dirPath
            if os.path.isfile(dirPath):
                os.remove(dirPath)
            else:
                shutil.rmtree(dirPath)
            print dir
    else:
        print 'This path(%s) is not exit' % path


configpath = r"clean_config.txt"
fp = open(configpath)
directories = []

try:
    for line in fp.readlines():
        line = line.replace("\n", "")
        directories.append(line)
finally:
    fp.close()

for line in directories:
    clear_directory(line)
