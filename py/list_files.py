import os
import pprint
from os import listdir
from os.path import isfile, join

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

print dir_path
print cwd


path = "C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\0"
print path

files = [dir_path + f for f in listdir(path) if isfile(join(path, f))]

pprint.pprint(files)
