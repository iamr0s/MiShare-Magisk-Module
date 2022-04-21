#!/usr/bin/python3
# -*- coding:utf-8 -*-

from array import array
import os
import shutil
from tokenize import String
import zipfile

projectDir = os.path.dirname(__file__)
cacheDir = projectDir + '/cache'
moduleDir = projectDir + '/module'

try:
    shutil.rmtree(cacheDir)
except Exception as e:
    print(e)


def getAllFiles(dir: String, path: String = ''):
    if os.path.isfile(dir + path):
        return [path]
    files = []
    for file in os.listdir(dir + path):
        files += getAllFiles(dir, path + '/' + file)
    return files


os.mkdir(cacheDir)

zip = zipfile.ZipFile(cacheDir + '/module.zip', 'w', zipfile.ZIP_DEFLATED)

for file in getAllFiles(moduleDir):
    zip.write(moduleDir + file, file)

zip.close()
